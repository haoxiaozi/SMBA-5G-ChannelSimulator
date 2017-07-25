from model import *

def vehicles_bandwidth(vehicles, distance_to_tx):

    for vehicle in vehicles:

        available_gbs = None # call the regular functions to return a Gbs

        if vehicle.vehicle_data_size > available_gbs:
            print("Vehicle {} is exceeding available Bandwith. Capped to {}".format())
            return 100, vehicle.vehicle_data_size, available_gbs

        else:
            percentage = (vehicle.vehicle_data_size / available_gbs) * 100
            return percentage, vehicle.vehicle_data_size, available_gbs



def total_bandwidth(tower_bgs_limit, num_vehicles):
    return 0


# 'how much data the car wants to send' is out of scope for this semester, so we will have to use randomly generated
# sizes within a min and max range.


def bandwidth_gui(vehicles):
    pass


