import numpy as np

def ice_load(diam, ice, ice_density=900):
    diam = diam / 1000          # Convert diameter from mm to m
    ice = ice * 25.4 / 1000     # Convert ice thickness from inches to m
    return ice_density * np.pi * (diam*ice + ice**2)

def wind_conversion(wind, gravity=9.810665):
    return np.sqrt(gravity * wind / 0.599072)

def wind_load(diam, wind, ice, gravity, w):
    diam = diam / 1000          # Convert diameter from mm to m
    ice = ice * 25.4 / 1000     # Convert ice thickness from inches to m
    wind = wind_conversion(wind, gravity)  # Convert wind pressure (kg/m^2) to velocity (m/s)
    return 0.599072/gravity*(diam + 2*ice)*wind**2

def total_load(diam, ice, ice_density, wind, gravity, w):
    ice_load_value = ice_load(diam, ice, ice_density)
    wind_load_value = wind_load(diam, wind, ice, gravity, w)
    return np.sqrt((ice_load_value + w)**2 + wind_load_value**2)    

##################

def Vor(wh, H, B_mon, phi, T, alpha, wv, diam, wind, ice, gravity, w):

    wh = wind_load(diam, wind, ice, gravity, w)
    wv = w + ice_load(diam, ice, ice_density=900)

    return (wh*H - B_mon*np.tan(phi)/2 + 2*T*np.sin(alpha))/wv/np.tan(phi)

def main():
    
    S = 290            # m
    h = 0              # m
    Th = 2875          # kg
    w = 1.303          # kg/m
    diam = 25.15       # mm
    ice = .25          # inches
    ice_density = 900  # kg/m^3
    wind = 44          # kg/m2
    gravity = 9.810665 # m/s^2

    print(ice_load(diam, ice, ice_density))
    print(wind_load(diam, wind, ice, gravity, w))
    print(total_load(diam, ice, ice_density, wind, gravity, w))

    #plt.plot([1, 2, 3], [1, 4, 11])
    #plt.savefig("plot.png")

if __name__ == "__main__":
    main()