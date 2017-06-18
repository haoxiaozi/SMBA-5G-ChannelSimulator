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

function PL_out = getFoliageAttenuatedPL(PL_in,folAtt,dFol)
% Generate the path loss in dB that is attenuated by the foliage
%
% Inputs:
%   - PL_in: path loss in dB
%   - folAtt: foliage attenuation in dB/m, which may range from 0 to 10 dB
%   - dFol: distance within foliage, which can be set to any non-negative 
%           number no larger than the lower bound of the T-R separation distance
% Output:
%   - PL_out: path loss in dB containing the foliage attenuation

        PL_out = PL_in+folAtt*dFol;
        