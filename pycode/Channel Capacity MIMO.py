import numpy as np
import matplotlib.pyplot as mp

#this isn't complete yet. so it will not compile!


# numpy is the library used for mathematical functions

# Global variables
# nR = number of Receivers
# nT = number of Transmitters
# min_SNR and max_SNR are lower and upper bounds for the X-axis in the plot. they will be calculated in another module using the input parameters for rain,temprature,foilage, ...

nR = 0
nT = 0
f_Bandwidth = 0
min_SNR = 0
max_SNR = 0


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


# builds Channel Matrix H. Still needs to be implemented once I completely understand it.
# i'm currently working on understanding how to construct the channel matrix and what kind of input we need from the user to do so. Nothing is looking promising sofar unfortunatly.
# its a matrix with complex values though.
def build_Channel_Matrix(nR, nT):
    # Some code here to construct the matrix

    return


# this function calculates the implements the Channel Capacity formula for MIMO-Systems.
# it will return the maximum data rate the channel is capable of delivering measured in bits/s
# the value of C is multiplied by the frequency bandwidth because what we actually get isn't the max data rate, but the spectral efficiency measured in bits/s/Hz
# ideally we will have a range for the SNR (using the parameters input by the user for rain, weather, etc.) which we could then use to plot a graph that describe data rate in regards to SNR \
# using this function
def calculate_Channel_Capacity(avg_SNR):
    H = build_Channel_Matrix(nR, nT)
    I_nR = np.eye(nR, nT, dtype=int)
    H_conj_trans = np.H.getH()
    A = I_nR + (avg_SNR / nT * (H * H_conj_trans))
    tmp = np.linalg.det(A)
    C = np.log2(tmp)
    return f_Bandwidth * C


def draw():
    x = np.arange(0, max_SNR, 2)
    y = calculate_Channel_Capacity(x)
    mp.plot(x, y)
    mp.ylabel('Channel Capacity in bits/s')
    mp.xlabel('SNR in dB')
    mp.show()
    return