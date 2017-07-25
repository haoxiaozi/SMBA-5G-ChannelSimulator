import rospy

from std_msgs.msg import Int32

from project_constants import *

std_topic = "chatter"

vehicles = [[0, 5.977, 4, 8, (4 / 8) * 100, 5],
            [1, 2.34, 5, 8, (5 / 8) * 100, 10],
            [2, 15.6, 3, 8, (3 / 8) * 100, 10]]

set_number = 1

# Sets the table default values, formats the size of the columns and the number of rows that will appear.
def set_ros_table():

    global set_number

    set_number = len(vehicles)

    for i, vehicle in enumerate(vehicles):

        if i % 2 == 0:
            colour = "light sky blue"
        else:
            colour = "white"

        Label(master, text="ID",                                                bg=colour, height=1, width=2,  anchor='w').grid(row=i+1, column=4)
        Label(master, text="{}".format(0),                                      bg=colour, height=1, width=3,  anchor='w').grid(row=i+1, column=5)

        Label(master, text="Distance to Tx:",                                   bg=colour, height=1, width=12, anchor='w').grid(row=i+1, column=6)
        Label(master, text="{} m".format(round(vehicle[1], decimal_places)),    bg=colour, height=1, width=9,  anchor='w').grid(row=i+1, column=7)

        Label(master, text="Vehicle Data:",                                     bg=colour, height=1, width=10, anchor='w').grid(row=i+1, column=8)
        Label(master, text="{} Gb/s".format(round(vehicle[2], decimal_places)), bg=colour, height=1, width=10, anchor='w').grid(row=i+1, column=9)

        Label(master, text="Uplink to Tx:",                                     bg=colour, height=1, width=10, anchor='w').grid(row=i+1, column=10)
        Label(master, text="{} Gb/s".format(round(vehicle[3], decimal_places)), bg=colour, height=1, width=10, anchor='w').grid(row=i+1, column=11)

        Label(master, text="Uplink pct:",                                       bg=colour, height=1, width=8,  anchor='w').grid(row=i+1, column=12)
        Label(master, text="{}%".format(round(vehicle[4], decimal_places)),     bg=colour, height=1, width=8,  anchor='w').grid(row=i+1, column=13)

        Label(master, text="Tower Max Capacity:",                               bg=colour, height=1, width=15, anchor='w').grid(row=i+1, column=14)
        Label(master, text="{} Gb/s".format(round(vehicle[5], decimal_places)), bg=colour, height=1, width=10, anchor='w').grid(row=i+1, column=15)




def callback(data):

    # if the number of vehicles has changed then run the set_ros_table() function again
    if len(vehicles) != set_number:
        set_ros_table()

    print(len(vehicles))

    print(set_number)

    for i, vehicle in enumerate(vehicles):

        if i % 2 == 0:
            colour = "light sky blue"
        else:
            colour = "white"

        Label(master, text="{}".format(data.data),                                 bg=colour, height=1, width=3,  anchor='w').grid(row=i+1, column=5)

        Label(master, text="{} m".format(round(vehicle[1], decimal_places)),       bg=colour, height=1, width=9,  anchor='w').grid(row=i+1, column=7)

        Label(master, text="{} Gb/s".format(round(vehicle[2], decimal_places)),    bg=colour, height=1, width=10, anchor='w').grid(row=i+1, column=9)

        Label(master, text="{} Gb/s".format(round(vehicle[3], decimal_places)),    bg=colour, height=1, width=10, anchor='w').grid(row=i+1, column=11)

        Label(master, text="{}%".format(round(vehicle[4], decimal_places)),        bg=colour, height=1, width=8,  anchor='w').grid(row=i+1, column=13)

        Label(master, text="{} Gb/s".format(round(vehicle[5], decimal_places)),    bg=colour, height=1, width=10, anchor='w').grid(row=i+1, column=15)






def listener():

    rospy.init_node('CarConsole', anonymous = True)

    rospy.Subscriber(std_topic, Int32, callback)




if __name__ == '__main__':

    set_ros_table()

    listener()

#    print("Hello ", car_ido)




mainloop()