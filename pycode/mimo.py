import numpy as np
import matplotlib.pyplot as mp

# this isn't complete yet. so it will not compile!


# numpy is the library used for mathematical functions

# Global variables
# nR = number of Receivers
# nT = number of Transmitters
# min_SNR and max_SNR are lower and upper bounds for the X-axis in the plot. they will be calculated in another module using the input parameters for rain,temprature,foilage, ...

nR = 4
nT = 4
f_Bandwidth = 80
min_SNR = 0
max_SNR = 30


# initializes the module with the values specified by the user
def init(num_receivers, num_transmitters, frequency_Bandwidth, lowerSNR, upperSNR):
    global nR
    nR = num_receivers
    global nT
    nT = num_transmitters
    global f_Bandwidth
    f_Bandwidth = frequency_Bandwidth
    global min_SNR
    min_SNR = lowerSNR
    global max_SNR
    max_SNR = upperSNR
    return


# builds Channel Matrix H.
# I used a rayleigh fading model for implementing the Channel Matrix hence the random rayleigh numbers used.
def generate_Channel_Matrix(nR, nT):
    H = np.zeros((nR, nT),dtype=complex)
    scale = np.sqrt(0.5)
    for x in np.nditer(H, op_flags=['readwrite']):
            x[...] = np.random.rayleigh(scale) + 1j*np.random.rayleigh(scale)
    return H

# this function calculates the implements the Channel Capacity formula for MIMO-Systems.
# it will return the maximum data rate the channel is capable of delivering measured in bits/s
# the value of C is multiplied by the frequency bandwidth because what we actually get isn't the max data rate, but the spectral efficiency measured in bits/s/Hz
# ideally we will have a range for the SNR (using the parameters input by the user for rain, weather, etc.) which we could then use to plot a graph that describe data rate in regards to SNR \
# using this function

H = generate_Channel_Matrix(nR, nT)

def calculate_Channel_Capacity(avg_SNR):
    I_nR = np.eye(nR, nR, dtype=int)
    A = I_nR + (avg_SNR / nT * (np.dot(H,np.matrix.getH(H))))
    tmp = np.linalg.det(A)
    C = np.real(np.log2(tmp))
    return f_Bandwidth * C

for i in range(1,30):
    c = calculate_Channel_Capacity(i)
    if c < 1000:
        print('SNR = '+str(i)+' dBm' + '     Channel Capacity = ' + str(c)+' Mbit/s')
    else:
        print('SNR = '+str(i)+' dBm' + '     Channel Capacity = ' + str(c/1000)+' Gbit/s')

