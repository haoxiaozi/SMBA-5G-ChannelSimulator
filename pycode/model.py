"""
from tkinter import *
import tkinter

top = tkinter.Tk()

def helloCallBack():
   tkinter.showinfo( "Hello Python", "Hello World")

B = tkinter.Button(top, text = "Hello", command = helloCallBack)

B.pack()
B.place(bordermode=OUTSIDE, height=100, width=100)
B.place(x = 35, y = 50)
top.mainloop()
"""

from tkinter import *
from tkinter import messagebox
import functions
import parameters

# power = 100.00, distance = 50, freq_band = 200, vegetation = 0, buildings = 0, weatherAF = 0
def myFunc ():
    messagebox.showinfo("Say Hello", "Hello World.")


colour = 'snow'

master = Tk()
master.title("5G Network Simulator for Autonomous Vehicles")
master.geometry("647x400") # size of the window in px
master.configure(background = colour) # background colour

Label(master, text = "Power in dB", bg = colour).grid(row = 0)
Label(master, text = "Distance in m", bg = colour).grid(row = 1)
Label(master, text = "Freq. Bandwidth in Hz", bg = colour).grid(row = 2)
Label(master, text = "Environment", bg = colour).grid(row = 3)
Label(master, text = "Vegetation [1 . . 0]", bg = colour).grid(row = 4)
Label(master, text = "Topology [1 . . 0]", bg = colour).grid(row = 5)
Label(master, text = "Weather attenuation factor [1 . . 0]", bg = colour).grid(row = 6)


power       = StringVar()
distance    = StringVar()
freq_band   = StringVar()
environment = StringVar()
vegetation  = StringVar()
topology    = StringVar()
weatherAF   = StringVar()


choices = {'Urban LOS','Urban NLOS','Rural LOS','Rural NLOS'}

e1 = Entry(master, textvariable = power)
e2 = Entry(master, textvariable = distance)
e3 = Entry(master, textvariable = freq_band)

e4 = OptionMenu(master, 'Choose from list', *choices)

e5 = Entry(master, textvariable = vegetation)
e6 = Entry(master, textvariable = topology)
e7 = Entry(master, textvariable = weatherAF)

e1.grid(row = 0, column = 1)
e1.insert(0, '100.00') # index, default values
e2.grid(row = 1, column = 1)
e2.insert(0, '50') # default values
e3.grid(row = 2, column = 1)
e3.insert(0, 200) # default values

e4.grid(row = 3, column = 1)
#e4.insert(0, 'Choose from list') # default values

e5.grid(row = 4, column = 1)
e5.insert(0, '0.12') # default values
e6.grid(row = 5, column = 1)
e6.insert(0, '0.3') # default values
e7.grid(row = 6, column = 1)
e7.insert(0, '0.3') # default values

button = Button(master, text="Simulate", command = myFunc).grid(row = 7, column = 1)

# myFunc(power, distance, freq_band, vegetation, topology, weatherAF))


mainloop()

"""
from tkinter import *
from tkinter import messagebox


def hello():
   messagebox.showinfo("Say Hello", "Hello World")


# defines the main window
main = Tk()
main.title("5G Network Simulator for Autonomous Vehicles")
main.geometry("970x600") # size of the window in px
main.configure(background='grey') # background colour

# make a frame for the distance
power_labelText = StringVar()

power_frame = Frame(main)

power_label = Label(power_frame, textvariable = 'Power')


# name where the distance frame is going to be located
B1 = Button(main, text = "Say Hello", command = hello, bd = 0)
B1.place(x = 35, y = 50)



power_frame.pack()

main.mainloop()
"""
"""
# TKinter stands for 'Tool Kit Interface', it was developed in C for Unix
from tkinter import *
from tkinter import ttk

# make a dictionary that lists the title of the field and the unit it will work in




root = Tk() # create an object, root will hold our window

root.title("5G Network Simulator for Autonomous Vehicles")

frame = Frame(root)

powe_labelText = StringVar()
dist_labelText = StringVar()

# layout of the items
power_label = Label(frame, textvariable = powe_labelText)
distance_label = Label(frame, textvariable = dist_labelText)
button = Button(frame, text="Simulate")

# content of the GUI items
dist_labelText.set("Distance")
powe_labelText.set("Power")

# fill in the data
power_label.pack()
distance_label.pack()
button.pack()
frame.pack()


#ttk.Button(root, text="Hello TkInter Button").grid()
#ttk.Label(root, text="Hello TkInter Label").grid()


# path loss vs T-R separation distance plot
#



root.mainloop()


# functor class
class Mimo:
    def __init__(self, num_antennas = None):
        self.num_antennas = num_antennas



distance_t_r = 10 # distance in metres

transmiting_power = 10 # dB

nof_antennas = 1 # number of antennas

noise = 0


environment = [] # py_dict

mimo = Mimo()


"""