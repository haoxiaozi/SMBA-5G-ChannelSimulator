from tkinter import *

# frequency and distance passed to the function
f = 500
d = 100

# Round pinted numbers to 'n' decimal places
round_to_n = 2


#choices = {'Urban LOS','Urban NLOS','Rural LOS','Rural NLOS'}


"""
environment = [["Urban LOS", 2.0, 4.0],
               ["Urban NLOS", 3.2, 7.0],
               ["Rural LOS", 2.16, 4.0],
               ["Rural NLOS", 2.75, 8.0]]
"""

labels =   ["Number of Transmitters","Number of Receivers","Power in dB", "Distance in m", "Freq. Bandwidth in Hz", "Environment", "Vegetation [1 . . 0]", "Topology [1 . . 0]", "Weather attenuation factor [1 . . 0]"]
defaults = [ 1                      ,            1        ,   100.0,         50.0,            200.0,                   None,          0.0,                    0.0,                  0.0]

environment = [["Urban LOS", "Urban NLOS", "Rural LOS", "Rural NLOS"],
               [2.0,            3.2,            2.16,       2.75],
               [4.0,            7.0,            4.0,        8.0]]


# Urban LOS
#if environment[0][0]
def urban_los():
    environment[1][0]  # returns 2.0
    environment[2][0]  # returns 4.0


# Urban NLOS
#if environment[0][1]
def urban_nlos():
    environment[1][1] # returns 3.2
    environment[2][1] # returns 7.0


# Rural LOS
#if environment[0][2]:
def rural_los():
    environment[1][2] # returns 2.16
    environment[2][2] # returns 4.0


# Rural NLOS
#if environment[0][3]
def rural_nlos():
    environment[1][3] # returns 2.75
    environment[2][3] # returns 8.0



master = Tk()
master.title("5G Network Simulator for Autonomous Vehicles")
master.geometry("647x400") # size of the window in px
colour = 'snow'
master.configure(background = colour) # background colour