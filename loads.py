import numpy as np
import matplotlib.pyplot as plt

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

def Vor(H, B_mon, phi, T, alpha, diam, wind, ice, ice_density, gravity, w):

    wh = wind_load(diam, wind, ice, gravity, w)
    wv = w + ice_load(diam, ice, ice_density=900)

    return (wh*H*np.cos(alpha/2) - B_mon*np.tan(phi)/2 + 2*T*np.sin(alpha/2))/wv/np.tan(phi)

def main():
    
    S = 290                 # m
    h = 0                   # m
    Th = 2875               # kg
    
    w = 1.303 -0.074               # kg/m   after subtracting K constant
    diam = 25.15            # mm
    ice = 0                 # inches
    ice_density = 900       # kg/m^3
    wind = 20              # kg/m2
    gravity = 9.810665      # m/s^2

    phi = np.radians(35)    # the input in degrees 
    T = 2775              # ruling span tension
    B_mon = 100              # kg     
    #alpha = np.radians(0)   # the input in degrees
    
    H = np.linspace(100,450,351)

    alpha_degrees = [0, 1, 2, 3, 4, 5, 6]

    plt.figure(figsize=(8, 8))

    for alpha_deg in alpha_degrees:
        alpha = np.radians(alpha_deg)

        H_max = 450 - 50*alpha_deg

        H_cut = H[H <= H_max]

        V = Vor(H_cut, B_mon, phi, T, alpha, diam, wind, ice, ice_density, gravity, w)

        plt.plot(H_cut, V, label=f"alpha = {alpha_deg}°")

        
        print(f"slope for {alpha_deg}°: {wind_load(diam, wind, ice, gravity, w)*np.cos(alpha/2)/(
            ice_load(diam, ice, ice_density)+w)/np.tan(phi):.4f}")

    plt.xlabel("Οριζόντιο")
    plt.ylabel("Κατακόρυφο")
    plt.title("")
    #plt.legend()
    plt.grid(True)
    plt.tight_layout()
    
    plt.xlim(100, 500)
    plt.ylim(100, 650)
    plt.gca().set_aspect('equal', adjustable='box')
    
    plt.show()
    plt.savefig("plot.png")

    
    #V = Vor(H,B_mon, phi, T, alpha, diam, wind, ice, ice_density, gravity, w)
    
    #plt.plot(H,V)
    
    #print(Vor(145,B_mon, phi, T, alpha, diam, wind, ice, ice_density, gravity, w))
    #rint(Vor(450,B_mon, phi, T, alpha, diam, wind, ice, ice_density, gravity, w))
    
    
    #print(ice_load(diam, ice, ice_density))

    # print(f"slope: {wind_load(diam, wind, ice, gravity, w)*np.cos(alpha/2)/(
    #     ice_load(diam, ice, ice_density)+w)/np.tan(phi)}")
    
    #print(total_load(diam, ice, ice_density, wind, gravity, w))

    #plt.plot([1, 2, 3], [1, 4, 11])
    #plt.savefig("plot.png")

if __name__ == "__main__":
    main()