# System Imports
from tkinter import *

master = Tk()
master.title("5G Network Simulator for Autonomous Vehicles")
master.geometry("1630x560") # size of the window in px, the width is divided by 1.618 to calculate the height
colour = 'white'
master.configure(background = colour) # background colour
button_size = 18

decimal_places = 2


labels   = [
        "Carrier Frequency [GHz]", 
        "Bandwidth [MHz]", 
        "Number of Transmitters",
        "Number of Receivers",
        "TX-RX Distance [m]", 
        "TX Power [dB]",
        "TX Gain [dBi]",
        "RX Gain [dBi]",
        "Foilage depth [m] (0...400)", 
        "Rainfall [mm/hr]", 
        "Weather attenuation factor [1 . . 0]", 
        "Environment"
        ]

defaults = [ 
        28.0,            
        200.0,                   
        1,                       
        1,                    
        500.0,            
        30.0,         
        10.0,         
        10.0,         
        0.0,                 
        0.0,                  
        0.0,                                    
        None
        ]



environment = [["Urban LOS", "Urban NLOS", "Rural LOS", "Rural NLOS"],
               [2.0,            3.2,            2.16,       2.75],
               [4.0,            7.0,            4.0,        8.0]]


