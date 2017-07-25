#
#  _____ _   _ __  __
# |_   _| | | |  \/  |
#   | | | | | | |\/| |
#   | | | |_| | |  | |
#   |_|  \___/|_|  |_|
#
#   ____  __  __ ____    _
#  / ___||  \/  | __ )  / \
#  \___ \| |\/| |  _ \ / _ \
#   ___) | |  | | |_) / ___ \       Created by H. Mirzai, Omar. , Martin  on 10th of May 2017
#  |____/|_|  |_|____/_/   \_\
#
#

# If the order of the imports is not respected the project does not compile. This should be fixed.
from tkinter import *
from model_functions import *
from project_constants import *
#from mimo import *
import matplotlib.pyplot as plt
import numpy as np
import os.path as path


#TODO: Replae 'snr_call' func parameters with the global variables

#TODO: Fix the crashing/freezing of the application by making smaller windows in the main window

#TODO: ROS integration

#TODO plot3
#capacity (in bits) vs SNR ()

#TODO plot4
#capacity (in bits) vs nT ()

#TODO plot5
#capacity (in bits) vs nR ()

#replace with defaults? might be a mad move in case of changing defaults

rostopic_name = "TestName"


carrier_freq    = defaults[0]
bandwidth       = defaults[1]
no_transmitters = defaults[2]
no_receivers    = defaults[3]
distance_m      = defaults[4]
tx_power_db     = defaults[5]
tx_gain         = defaults[6]
rx_gain         = defaults[7]
d_foilage       = defaults[8]
rainfall        = defaults[9]
weather_att     = defaults[10]
pl_exp  = environment[1][0]
pl_chi  = environment[2][0]

entry_list      = [] # the GUI form entries



def userinput():

    ros_console()

    for i, entry in enumerate(entry_list):
        if i == 0:
            global carrier_freq
            carrier_freq    = float(entry.get())
        if i == 1:
            global bandwidth
            bandwidth       = float(entry.get())
        if i == 2:
            global no_transmitters
            no_transmitters = int(entry.get())
        if i == 3:
            global no_receivers
            no_receivers    = int(entry.get())
        if i == 4:
            global distance_m
            distance_m      = float(entry.get())
        if i == 5:
            global tx_power_db
            tx_power_db     = float(entry.get())
        if i == 6:
            global tx_gain
            tx_gain         = float(entry.get())
        if i == 7:
            global rx_gain
            rx_gain         = float(entry.get())
        if i == 8:
            global d_foilage
            d_foilage       = float(entry.get())
        if i == 9:
            global rainfall
            rainfall        = float(entry.get())
        if i == 10:
            global weather_att
            weather_att     = float(entry.get())



def option_func(value):

    global environment
    global pl_exp
    global pl_chi

    if value == "Urban LOS":
        pl_exp = environment[1][0] # assigns 2.0
        pl_chi = environment[2][0] # assigns 4.0

    elif value == "Urban NLOS":
        pl_exp = environment[1][1] # returns 3.2
        pl_chi = environment[2][1] # returns 7.0

    elif value == "Rural LOS":
        pl_exp = environment[1][2] # returns 2.16
        pl_chi = environment[2][2] # returns 4.0

    else:
        pl_exp = environment[1][3]  # returns 2.75
        pl_chi = environment[2][3]  # returns 8.0




def plot_func():

    userinput()

    d1 = np.arange(10, distance_m, 10) # start 0, end 400, step 10

    plt.figure(1)
    plt.subplot(211)
    plt.ylabel('Path Loss [dB]')
    plt.xlabel('distance [m]')

    ### Path Loss Plots ###

    # Log Normal w/ Path Loss
    dat1 = []
    for d in d1:
        dat1.append( path_loss(d, carrier_freq, pl_exp) )

    plt.plot(d1, dat1, 'r.', label='Free Space Path Loss'); 

    # Log Normal + Foilage Path Loss
    dat2 = []
    for d in d1:
        dat2.append( path_loss(d, carrier_freq, pl_exp) + foilage_loss(carrier_freq, d_foilage) )

    plt.plot(d1, dat2, 'g.', label='PL + Foilage')

    # Log Normal + Rain Loss 
    dat3 = []
    for d in d1:
        dat3.append( path_loss(d, carrier_freq, pl_exp) + rain_loss(rainfall) )

    plt.plot(d1, dat3, 'y.', label='PL + Rain')

    plt.legend(loc='upper right')


    ### SNR Plots ###

    #plt.subplot(212)
    #plt.ylabel('snr');

    #dat10 = []
    #for d in d1:
    #    dat10.append(
    #            snr_db(
    #                friis(path_loss(d, carrier_freq, pl_exp), tx_power_db, 10, 10),
    #                nyquist_noise(bandwidth)
    #                )
    #            )
    #plt.plot(d1, dat10, 'r.', label='LOS');

    #dat11 = []
    #for d in d1:
    #    dat11.append(
    #            snr_db(
    #                friis(path_loss(d, carrier_freq, pl_exp), tx_power_db, 10, 10) + foilage_loss(carrier_freq, d_foilage),
    #                nyquist_noise(bandwidth)
    #                )
    #            )
    #plt.plot(d1, dat11, 'g.', label='LOS');

    ### Channel Capacity Plots ###

    plt.subplot(212)
    plt.ylabel('Channel Capacity [b/s]')
    plt.xlabel('distance [m]')

    # Path Loss 
    dat4 = []
    for d in d1:
        dat4.append( 
            shannon_capacity(bandwidth, 
                snr( 
                    friis(path_loss(d, carrier_freq, pl_exp),  tx_power_db, tx_gain, rx_gain), 
                    nyquist_noise(bandwidth)
                    )
                ) 
            )

    plt.plot(d1, dat4, 'r.', label='Free Space Path Loss');

    # Path Loss + Foilage
    dat5 = []
    for d in d1:
        dat5.append( 
            shannon_capacity(bandwidth, 
                snr( 
                    friis(path_loss(d, carrier_freq, pl_exp) + foilage_loss(carrier_freq, d_foilage), tx_power_db, tx_gain, rx_gain), 
                    nyquist_noise(bandwidth)
                    )
                ) 
            )

    plt.plot(d1, dat5, 'g.', label='PL + Foilage')

    # Path Loss + Rain
    dat6 = []
    for d in d1:
        dat6.append( 
            shannon_capacity(bandwidth, 
                snr( 
                    friis(path_loss(d, carrier_freq, pl_exp) + rain_loss(rainfall), tx_power_db, tx_gain, rx_gain), 
                    nyquist_noise(bandwidth)
                    )
                ) 
            )

    plt.plot(d1, dat6, 'y.', label='PL + Rain')


    plt.legend(loc='upper right')
    
    plt.show()


dir = path.dirname(__file__)
white_logo  = path.join(dir, 'imgs/logo_white.gif')
mini_orange = path.join(dir, 'imgs/mini_o.gif')
mini_red    = path.join(dir, 'imgs/mini_r.gif')
mini_green  = path.join(dir, 'imgs/mini_g.gif')


img1 = PhotoImage(file=white_logo)
panel1 = Label(master, image=img1, border=0).grid(row = 0, column = 2)


# TODO:this must be nested in the ROS functions
ros_ok      = 0
ros_message = 1

if ros_ok == True:
    status_img = PhotoImage(file=mini_green)
    status_spc = Label(master, image=status_img, border=0).grid(row=1, column=2)
else:
    if ros_message == True:
        status_img = PhotoImage(file=mini_orange)
        status_spc = Label(master, image=status_img, border=0).grid(row=1, column=2)
        Label(master, text="No ROS topic found", bg=colour).grid(row=2, column=2)
    else:
        status_img = PhotoImage(file=mini_red)
        status_spc = Label(master, image=status_img, border=0).grid(row=1, column=2)
        Label(master, text="ROS topic error", bg=colour).grid(row=2, column=2)


# Fill in Col = 0 with labels and Col = 1 with Entry fields
for i, label in enumerate(labels):
    Label(master, text=label, bg=colour, height = 1, width = 27).grid(row=i+1, column=0) # Place labels on column 0
    if i == len(labels) - 1:
       a = OptionMenu(master, StringVar(), *environment[0], command=option_func)
       a.config(width = 16)
       a.grid(row = i+1, column = 1)
    else:
        # e. stands for Entry
        e = Entry(master, textvariable=StringVar())
        e.grid(row = i+1, column = 1)
        e.insert(0, defaults[i])    # index, default values
        entry_list.append(e) # add the entry to the entry_list array so that it may be used in other parts of the app

    # This gets a new column section on the right for ROS and listening to the topic

#Label(master, text = "Listening to ROS topic '{}'\nTo change it type here: ".format(rostopic_name), bg = colour, justify=LEFT).grid(row=0, column=4, pady=5)
#Entry(master, textvariable=StringVar()).grid(row = 0, column = 5, padx = 8, pady = 6)
#button_listener = Button(master, text="Submit", command = change_ros_listener, height = 0,  width = 6).grid(row=0, column=6, padx=0, pady=0)


#Label(master, text = "ROS Integration".format(rostopic_name), bg = colour, justify=LEFT).grid(row=0, column=4, pady=5)


def ros_console():

    car1a = 5.1*np.random.rand()
    car1b = 4.9*np.random.rand()
    car2a = 2.2*np.random.rand()
    car2b = 2.2*np.random.rand()
    car3a = 7.3*np.random.rand()
    car3b = 0.25*np.random.rand()


    vehicles = [[0, 5.977*np.random.rand(), car1a, car1b, (car1a/car1b)*100, 5], [1, 2.34*np.random.rand(), car2a, car2b, (car2a/car2b)*100, 10], [2, 15.6*np.random.rand(), car3a, car3b, (car3a/car3b)*100, 10]]



    #TODO: THIS NEEDS TO BE PLUGGED INTO THE ROS SYSTEM
    for i, vehicle in enumerate(vehicles):

        if i % 2 == 0:
            colour = "light sky blue"
        else:
            colour = "white"


        Label(master, text = "ID",                                              bg=colour, height = 1, width = 2,  anchor='w').grid(row = i+1, column = 4)
        Label(master, text="{}".format(vehicle[0]),                             bg=colour, height = 1, width = 3,  anchor='w').grid(row = i+1, column = 5)

        Label(master, text = "Distance to Tx:",                                 bg=colour, height = 1, width = 11, anchor='w').grid(row = i+1, column = 6)
        Label(master, text="{} m".format(round(vehicle[1], decimal_places)),    bg=colour, height = 1, width = 8,  anchor='w').grid(row = i+1, column = 7)

        Label(master, text = "Vehicle Data:",                                   bg=colour, height = 1, width = 10, anchor='w').grid(row = i+1, column = 8)
        Label(master, text="{} Gb/s".format(round(vehicle[2], decimal_places)), bg=colour, height = 1, width = 10, anchor='w').grid(row = i+1, column = 9)

        Label(master, text = "Uplink to Tx:",                                   bg=colour, height = 1, width = 10, anchor='w').grid(row = i+1, column = 10)
        Label(master, text="{} Gb/s".format(round(vehicle[3], decimal_places)), bg=colour, height = 1, width = 10, anchor='w').grid(row = i+1, column = 11)

        Label(master, text = "Uplink pct:",                                     bg=colour, height = 1, width = 8,  anchor='w').grid(row = i+1, column = 12)
        Label(master, text="{}%".format(round(vehicle[4], decimal_places)),     bg=colour, height = 1, width = 8,  anchor='w').grid(row = i+1, column = 13)

        Label(master, text = "Tower Max Capacity:",                             bg=colour, height = 1, width = 15, anchor='w').grid(row = i+1, column = 14)
        Label(master, text="{} Gb/s".format(round(vehicle[5], decimal_places)), bg=colour, height = 1, width = 10, anchor='w').grid(row = i+1, column = 15)




button_ros_display = Button(master, text="Submit to ROS",        command = userinput,   height = 0,  width = button_size).grid(row = len(labels)+1, column = 1, padx=0, pady=10)
button_plot        = Button(master, text="Tower-Receiver Plot",  command = plot_func,   height = 0,  width = button_size).grid(row = len(labels)+2, column = 1, padx=0, pady=0)
button_quit        = Button(master, text="Quit",                 command = master.quit, height = 1,  width = 15         ).grid(row = len(labels)+3, column = 2, padx=0, pady=100)


mainloop()
