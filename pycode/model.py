# TKinter Tool Kit Interface GUI

from tkinter import *
from tkinter import messagebox
from functions import *
from parameters import *
#from mimo import *
#import matplotlib.pyplot as plot

#TODO add carrier frequency in GHz to parameters
#TODO: Complete 'snr_call' func parameters
#TODO: Plug in choices to the function callback
#TODO plot1
#capacity (in bits) vs SNR ()

#TODO plot2
#capacity (in bits) vs nT ()

#TODO plot3
#capacity (in bits) vs nR ()


# power = 100.00, distance = 50, freq_band = 200, vegetation = 0, buildings = 0, weatherAF = 0
def results_func():
    message = "Norm PL:\t" + str(round(lognormal_pl(f, d, 1, 1), round_to_n)) + " Units Log" '\n' +\
              "FL:\t" + str(round(fl(f, d), round_to_n)) + " Units" + '\n' +\
              "PL:\t" + str(round(pl(f, d), round_to_n)) + " Units"
    messagebox.showinfo("Results", message)






# Fill in Col = 0 with labels and Col = 1 with Entry fields
for i, label in enumerate(labels):
    Label(master, text=label, bg=colour).grid(row=i, column=0)
    if i == 5:
       a = OptionMenu(master,'Choose from list', *environment[0])
       a.config(width = 15)
       a.grid(row = i, column = 1)
    else:
        e = Entry(master, textvariable=StringVar())
        e.grid(row = i, column = 1)
        e.insert(0, defaults[i])  # index, default values


button = Button(master, text="Simulate", command = results_func).grid(row = len(labels), column = 1)


mainloop()