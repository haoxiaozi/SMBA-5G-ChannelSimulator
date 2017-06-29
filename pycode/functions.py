from math import log10


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
    if 0 < d <= 14:
        return 0.45 * (f ** 0.284) * d
    else:
        print("Input distance not in range 0 to 400.")


# Total Path loss:
def pl(f, d):
    return lognormal_pl(f, d, n = 1, chi = 0) + AT + fl(f, d)


labels =   ["Power in dB", "Distance in m", "Freq. Bandwidth in Hz", "Environment", "Vegetation [1 . . 0]", "Topology [1 . . 0]", "Weather attenuation factor [1 . . 0]"]

def snr_full(power, distance, freq, environ, vegetation, topology, weather):
    #TODO
    return
