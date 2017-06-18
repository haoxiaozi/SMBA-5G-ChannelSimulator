%%% NYUSIM - User License %%%

% Copyright (c) 2017 New York University and NYU WIRELESS

% Permission is hereby granted, free of charge, to any person obtaining a 
% copy of this software and associated documentation files (the �Software�),
% to deal in the Software without restriction, including without limitation 
% the rights to use, copy, modify, merge, publish, distribute, sublicense, 
% and/or sell copies of the Software, and to permit persons to whom the 
% Software is furnished to do so, subject to the following conditions:

% The above copyright notice and this permission notice shall be included
% in all copies or substantial portions of the Software. Users shall cite 
% NYU WIRELESS publications regarding this work.

% THE SOFTWARE IS PROVIDED �AS IS�, WITHOUTWARRANTY OF ANY KIND, EXPRESS OR 
% IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
% FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL 
% THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR 
% OTHER LIABILITY, WHETHER INANACTION OF CONTRACT TORT OR OTHERWISE, 
% ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR 
% OTHER DEALINGS IN THE SOFTWARE.

% Defined Params
N = 1; % Number of Simulation Runs

dmin = 10; % TRDistance
dmax = 100; % TRDistance

freq = 28e9; % Carrier Freq
n = 2; % Path Loss Exponent (PLE)
SF = 3; % Shadow Factor (dB)
TXPower = 30; % Transmit Power (dB)
d0 = 1; % Free space reference distance, typically 1 meter


% getNumClusters_AOA_AOD::
% The number of time clusters ranges from 1 to 6, and the
% mean number of spatial lobes is about 2 and is upper-bounded
% by 5, which are obtained from field observations and are
% much smaller than those in the 3GPP channel model [32].
mu_AOA = 3; % mean number of spatial lobes at the RX 
mu_AOD = 4; % mean number of spatial lobes at the TX 

% getIntraClusterDelays::
X_max = 0.5; % a number between 0 and 1 ??

% getClusterExcessTimeDelays::
mu_tau = 1; % mean excess delay in ns
minVoidInterval = 25; % minimum inter-cluster void interval, typically set
% to 25 ns for outdoor environments

% getClusterPowers::
Gamma = ; % time cluster decay constant, in ns
sigmaCluster = ; % per-cluster shadowing, in dB

% getSubpathPowers::
gamma = ; % subpath decay constant, in ns
sigmaSubpath = ; % per-subpath shadowing, in dB


% Load desired parameters
%eval([sceType,'_',envType,'_',accessType,'_',freq,'_ChannelParams'])

% Output to command window
disp(['Generating ',num2str(N),' CIRs...'])

% structure containing generated CIRs
CIR_Struct = struct;

for CIRIdx = 1:N

    % Step 1: Generate T-R Separation distance (m) ranging from dmin - dmax.
    TRDistance = getTRSep(dmin,dmax);

    % Step 2: Generate the total received omnidirectional power (dBm) and 
    % path loss (dB) 
    [Pr_dBm, PL_dB]= getRXPower(freq,n,SF,TXPower,TRDistance,d0);

    % Step 3: Generate the number of time clusters N, and number of AOD and
    % AOA spatial lobes
    [numberOfTimeClusters,numberOfAOALobes,numberOfAODLobes] = ...
        getNumClusters_AOA_AOD(mu_AOA,mu_AOD);

    % Step 4: Generate the number of cluster subpaths M_n for each time
    % cluster
    numberOfClusterSubPaths = getNumberOfClusterSubPaths(numberOfTimeClusters);

    % Step 5: Generate the intra-cluster subpath delays rho_mn (ns)
    rho_mn = getIntraClusterDelays(numberOfClusterSubPaths,X_max);

    % Step 6: Generate the phases (rad) for each cluster
    phases_mn = getSubpathPhases(rho_mn);

    % Step 7: Generate the cluster excess time delays tau_n (ns)
    tau_n = getClusterExcessTimeDelays(mu_tau,rho_mn,minVoidInterval);

    % Step 8: Generate temporal cluster powers (mW)
    clusterPowers = getClusterPowers(tau_n,Gamma,sigmaCluster);

    % Step 9: Generate the cluster subpath powers (mW)
    subpathPowers = ...
        getSubpathPowers(rho_mn,clusterPowers,gamma,sigmaSubpath);

    % Step 10: Recover absolute propagation times t_mn (ns) of each subpath 
    % component
    t_mn = getAbsolutePropTimes(TRDistance,tau_n,rho_mn);

    % Step 11: Recover AODs and AOAs of the multipath components
    [subpath_AODs, cluster_subpath_AODlobe_mapping] = ...
        getSubpathAngles(numberOfAODLobes,numberOfClusterSubPaths,mean_ZOD,...
        sigma_ZOD,std_AOD_RMSLobeElevationSpread,std_AOD_RMSLobeAzimuthSpread,...
        distributionType_AOD);
    [subpath_AOAs, cluster_subpath_AOAlobe_mapping] = ...
        getSubpathAngles(numberOfAOALobes,numberOfClusterSubPaths,mean_ZOA,...
        sigma_ZOA,std_AOA_RMSLobeElevationSpread,std_AOA_RMSLobeAzimuthSpread,...
        distributionType_AOA);

    % Step 12: Construct the multipath parameters
    powerSpectrum = getPowerSpectrum(numberOfClusterSubPaths,t_mn,subpathPowers,phases_mn,...
        subpath_AODs,subpath_AOAs);

    % Construct the 3-D lobe power spectra at TX and RX
    AOD_LobePowerSpectrum = getLobePowerSpectrum(numberOfAODLobes,cluster_subpath_AODlobe_mapping,powerSpectrum,'AOD');
    AOA_LobePowerSpectrum = getLobePowerSpectrum(numberOfAOALobes,cluster_subpath_AOAlobe_mapping,powerSpectrum,'AOA');

    % Store CIR parameters
    CIR.pathDelays = powerSpectrum(:,1);
    CIR.pathPowers = powerSpectrum(:,2);
    CIR.pathPhases = powerSpectrum(:,3);
    CIR.AODs = powerSpectrum(:,4);
    CIR.ZODs = powerSpectrum(:,5);
    CIR.AOAs = powerSpectrum(:,6);
    CIR.ZOAs = powerSpectrum(:,7);

    % Various other information for this CIR
    CIR.frequency = freq;
    CIR.TXPower = TXPower;
    CIR.OmniPower = Pr_dBm;
    CIR.OmniPL = PL_dB;
    CIR.TRSep = TRDistance;
    CIR.environment = envType;
    CIR.scenario = sceType;
    CIR.accessType = accessType;
    CIR.HPBW_TX = [theta_3dB_TX phi_3dB_TX];
    CIR.HPBW_RX = [theta_3dB_RX phi_3dB_RX];
    
    % Store
    CIR_Struct.(['CIR_',num2str(CIRIdx)]) = CIR;

end% end of CIRIdx

% Output to command window
disp('Generating CIRs..Done.')

