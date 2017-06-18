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

function h = plotPDP(FigVisibility,timeArray,multipathArray,TXPower,TRDistance,f,envType,PL_dB)

figure('visible',FigVisibility)
minPower = TXPower-180;

timeLine = min(timeArray):1:max(timeArray)+100;
Th = (TXPower-170).*ones(length(timeLine),1); % noise threshold for omniPDPs

% indNoise = find(multipathArray<10^((minPower+10)/10));
% multipathArray(indNoise) = []; timeArray(indNoise) = []; 

Pr_Lin = sum(multipathArray);
meanTau = sum(timeArray.*multipathArray)/sum(multipathArray);
meanTau_Sq=sum(timeArray.^2.*multipathArray)/sum(multipathArray);
RMSDelaySpread = sqrt(meanTau_Sq-meanTau^2);

stem(timeArray,10*log10(multipathArray),'BaseValue',minPower,'LineStyle','-','Marker','none','linewidth',1.5,'color','b');
hold on; plot(timeLine,Th, 'r-','linewidth',1.5);
xmaxInd = find(10*log10(multipathArray)>minPower+10);

%%% in case there is just one multipath, directly set its RMS value to 0
if numel(xmaxInd) == 1
    RMSDelaySpread=0;
else
end

hold on; grid on;
xlabel('Absolute Propagation Time (ns)','fontsize',16,'fontweight','bold')
ylabel('Received Power (dBm)','fontsize',16,'fontweight','bold')

titleName = 'Sample Omni. PDP Output Function';

title(titleName,'fontsize',20,'fontweight','bold')

set(gca,'fontweight','bold','fontsize',14)

yMax = max(10*log10(multipathArray))+5;
yMin = minPower;
ylim([yMin yMax ])

if ~isempty(xmaxInd)
xMax = timeArray(xmaxInd(end));
xMin = timeArray(xmaxInd(1));
xlim([.9*xMin 1.8*xMax])
%             set(gcf,'position',[ -883   514   560   420])


else
end

yLim = get(gca,'YLim');

gMax = yLim(2);
gMin = yLim(1);

deltaY = abs(yMax-yMin);
ratio = .08;

hMax = gMax - ratio*deltaY;
hMin = gMin+ratio*deltaY+.0045;


yarray = linspace(hMax,hMin,8);
text_pos = 1.1*xMax;

text(text_pos,yarray(2),[num2str(f),' GHz ',char(envType)],'fontsize',15,'fontweight','bold')
text(text_pos,yarray(3),[num2str(TRDistance,'%.1f'),' m T-R Separation'],'fontsize',15,'fontweight','bold')        

text(text_pos,yarray(4),['\sigma_{\tau} = ', num2str(RMSDelaySpread,'%.0f'),' ns'],'FontSize',15,'fontweight','bold')
text(text_pos,yarray(5),['P_r = ', num2str(10*log10(Pr_Lin),'%.1f'),' dBm'],'FontSize',15,'fontweight','bold')
text(text_pos,yarray(6),['PL = ', num2str(PL_dB,'%.1f'),' dB'],'FontSize',15,'fontweight','bold')

set(gcf,'color','w');
set(gcf,'Unit','Inches');
pos = get(gcf,'Position');
set(gcf','PaperPositionMode','Auto','PaperUnits','Inches','PaperSize',[pos(3) pos(4)]);

h = gcf;

end