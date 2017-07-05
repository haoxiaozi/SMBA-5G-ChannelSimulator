# TKinter Tool Kit Interface GUI

from tkinter import *
from tkinter import messagebox
from functions import *
from parameters import *
#from mimo import *
import matplotlib.pyplot as plt
import numpy as np

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
    message = "Norm PL:\t" + str(round(lognormal_path_loss(f, d, 1, 1), round_to_n)) + " Units Log" '\n' +\
              "FL:\t" + str(round(foilage_loss(f, d), round_to_n)) + " Units" + '\n' +\
              "PL:\t" + str(round(path_loss(f, d), round_to_n)) + " Units"
    messagebox.showinfo("Results", message)


def plot_func():
    d1 = np.arange(10, 400, 10) #start 0, end 400, step 10

    plt.figure(1)
    plt.subplot(211)
    plt.ylabel('Path Loss [dB]');
    plt.xlabel('distance [m]');
    print(d1);

    # Log Normal Path Loss
    dat1 = [];
    for d in d1:
        dat1.append( path_loss(d, 28, 2) );

    #plt.plot(d1, dat1, 'r.', label='LOS'); 

    # Log Normal Path Loss NLOS
    dat18 = [];
    for d in d1:
        dat18.append( path_loss(d, 28, 3.2) );

    plt.plot(d1, dat18, 'b.', label='NLOS'); 

    # Log Normal + Foilage Path Loss
    dat2 = [];
    for d in d1:
        dat2.append( path_loss(d, 28, 3.2) + foilage_loss(28, 10) );

    plt.plot(d1, dat2, 'g.', label='NLOS + 10m foliage');

    # Log Normal + Extreme Rain Loss 50mm/h 
    dat3 = [];
    for d in d1:
        dat3.append( path_loss(d, 28, 3.2) + rain_loss(50) );

    plt.plot(d1, dat3, 'y+', label='NLOS + 50mm/h rain');


    plt.legend(loc='upper right');


    #plt.subplot(212)
    #plt.ylabel('snr');

    dat10 = [];
    for d in d1:
        dat10.append(
                snr_db(
                    friis(path_loss(d, 28, 2), 30, 10, 10),
                    nyquist_noise(200e6)
                    )
                );
    #plt.plot(d1, dat10, 'r.', label='LOS');

    dat11 = [];
    for d in d1:
        dat11.append(
                snr_db(
                    friis(path_loss(d, 28, 2), 30, 10, 10) + foilage_loss(28, 10),
                    nyquist_noise(200e6)
                    )
                );
    #plt.plot(d1, dat11, 'g.', label='LOS');




    plt.subplot(212)
    plt.ylabel('Channel Capacity [b/s]');
    plt.xlabel('distance [m]');

    # Channel Capacity over Distance
    dat3 = [];
    for d in d1:
        dat3.append( 
            shannon_capacity(200e6, 
                snr( 
                    friis(path_loss(d, 28, 2) + 0, 10, 0, 0), 
                    nyquist_noise(200e6)
                    )
                ) 
            );

    #plt.plot(d1, dat3, 'r.', label='LOS');

    # Channel Capacity over Distance
    dat4 = [];
    for d in d1:
        dat4.append( 
            shannon_capacity(200e6, 
                snr( 
                    friis(path_loss(d, 28, 3.2) + foilage_loss(28, 10), 10, 0, 0), 
                    nyquist_noise(200e6)
                    )
                ) 
            );

    plt.plot(d1, dat4, 'g.', label='NLOS + 10m foliage');
    plt.legend(loc='upper right');
    
    plt.show()




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
button2 = Button(master, text="Plot", command = plot_func).grid(row = len(labels)+1, column = 1)




mainloop()
