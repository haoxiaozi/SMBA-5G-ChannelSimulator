from math import log10
from parameters import *

# Free Space Path Loss (1m reference)
def fspl_1m(freq):
    return 32.4 + 20 * log10(freq) # def. 28 GHz


# Log Normal Shadowing Path Loss
#n: Path loss exponent (1 < n < 5)
#chi: standard variation fadin (0 < chi < 20)
def lognormal_pl(f, d, n, chi):
    return fspl_1m(f) + 10 * n * log10(d) + chi


# Weather attenuation factor
AT = 0

# Foilage Attenuation:
# (Weissberger's model)


#d: # foilage depth (max 400m)
def fl(f, d):
    if 14 < d <= 400:
        return 1.33 * (f ** 0.284) * (d ** 0.588)
    elif 0 < d <= 14:
        return 0.45 * (f ** 0.284) * d
    else:
        print("Input distance not in range 0 to 400.")


# Total Path loss:
def pl(f, d):
    return lognormal_pl(f, d, n = 1, chi = 0) + AT + fl(f, d)


labels =   ["Power in dB", "Distance in m", "Freq. Bandwidth in Hz", "Environment", "Vegetation [1 . . 0]", "Topology [1 . . 0]", "Weather attenuation factor [1 . . 0]"]

def snr_call(no_transmitters = defaults[0], no_receivers = defaults[1], power = defaults[2], distance = defaults[3], freq = defaults[4], environ1 = environment[1][0], environ2 = environment[2][0],  vegetation = defaults[6], topology = defaults[7], weather = defaults[8]):
    #TODO: complete



    return None


def l_cab():
    pass

def l_env(d):
    return 20 * log10(2.25 / d)


def p_r():
    return eirp(dB*m) + G_r - 32.44 - (20 * log10(d * f)) - l_cab() - l_env(d)