%%% NYUSIM - User License %%%

% Copyright (c) 2017 New York University and NYU WIRELESS

% Permission is hereby granted, free of charge, to any person obtaining a 
% copy of this software and associated documentation files (the “Software”),
% to deal in the Software without restriction, including without limitation 
% the rights to use, copy, modify, merge, publish, distribute, sublicense, 
% and/or sell copies of the Software, and to permit persons to whom the 
% Software is furnished to do so, subject to the following conditions:

% The above copyright notice and this permission notice shall be included
% in all copies or substantial portions of the Software. Users shall cite 
% NYU WIRELESS publications regarding this work.

% THE SOFTWARE IS PROVIDED “AS IS”, WITHOUTWARRANTY OF ANY KIND, EXPRESS OR 
% IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
% FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL 
% THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR 
% OTHER LIABILITY, WHETHER INANACTION OF CONTRACT TORT OR OTHERWISE, 
% ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR 
% OTHER DEALINGS IN THE SOFTWARE.

function subpathPowers = ...
    getSubpathPowers(rho_mn,clusterPowers,gamma,sigmaSubpath)
% Generate the subpath powers
%
% Inputs:
%   - rho_mn: a structure containing the intra-cluster subpath delays, in
%   ns
%   - clusterPowers: an array containing the time cluster powers, relative
%   to 1 mW
%   - gamma: subpath decay constant, in ns
%   - sigmaSubpath: per-subpath shadowing, in dB
%
% Output:
%   - subpathPowers: a structure containing the subpath powers, relative to
%   1 mW
%
% Copyright © 2016 NYU

%%% number of clusters
numberOfClusters = size(clusterPowers,2);

%%% initialize the structure that will contain component powers
subpathPowers = struct;   

for clusterIndex = 1:numberOfClusters
    
    %%% current intra-cluster delays
    rho = rho_mn.(['c',num2str(clusterIndex)]);
    
    %%% number of components in current cluster
    numberOfComponents = numel(rho);
    
    %%% per sub path shadowing
    U = sigmaSubpath*randn([1 numberOfComponents]);        
        
    %%% generate sub path ratios
    subPathRatios_temp = exp(-rho/gamma).*10.^(U/10);
    
    %%% cluster power
    clusterPower = clusterPowers(clusterIndex);

    %%% normalize subpath power ratios such that their sum equals 1
    subPathRatios = subPathRatios_temp/sum(subPathRatios_temp)*clusterPower;    
        
    powerTemp = subPathRatios;
    
    %%% store sub path powers    
    subpathPowers.(['c',num2str(clusterIndex)]) = powerTemp;
  
    
end



end
