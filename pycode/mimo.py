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
# I used a rayleigh fading model for implementing the Channel Matrix hence the random rayleigh numbers used.
def build_Channel_Matrix(nR, nT):
    a = np.empty([nR, nT])
    scale = np.sqrt(0.5)
    for x in np.nditer(a, op_flags=['readwrite']):
        x[...] = np.random.rayleigh(scale)
    return a



# this function calculates the implements the Channel Capacity formula for MIMO-Systems.
# it will return the maximum data rate the channel is capable of delivering measured in bits/s
# the value of C is multiplied by the frequency bandwidth because what we actually get isn't the max data rate, but the spectral efficiency measured in bits/s/Hz
# ideally we will have a range for the SNR (using the parameters input by the user for rain, weather, etc.) which we could then use to plot a graph that describe data rate in regards to SNR \
# using this function
def calculate_Channel_Capacity(avg_SNR):
    H = build_Channel_Matrix(nR, nT)
    I_nR = np.eye(nR, nR, dtype=int)
    A = I_nR + (avg_SNR / nT * (H * np.transpose(H)))
    tmp = np.linalg.det(A)
    C = np.log2(tmp)
    return f_Bandwidth * C

c = calculate_Channel_Capacity(20)
print(c)

def draw():
    x = np.arange(0, max_SNR, 2)
    y = calculate_Channel_Capacity(x)
    mp.plot(x, y)
    mp.ylabel('Channel Capacity in bits/s')
    mp.xlabel('SNR in dB')
    mp.show()
    return
