import numpy as np
import matplotlib.pyplot as plt 

# defining the constants
 
G = 6.674*1e-11 # in SI units 
c = 3*1e8 # in SI units
M_0 = 1.989e30 # mass of the sun 
psi_vals = np.linspace(np.radians(89), np.radians(91), 100)
# the true anomaly measured from the ascending node of the pulsar

def amp_plot(a=8.784*1e8, e=0.0878, omega=np.radians(73.8), i=[90.14,90.28,90.56], M_c=1.25*M_0, flag=0): 
    """
    Provides amplification factor for the images plotted as a function of 
    longitude.
    The user has to provide information/parameters about 
    the double pulsar system in the following order - semi 
    major axis, eccentricity, the longitude of 
    periastron in radians, the inclination angle of the orbital plane
    in degrees, the mass of the companion pulsar, and a variable 'flag' 
    which shows the plot for the dominant image if left at 
    its default value 0 and shows the subdominant case if 
    set to 1  
    """

    phi = psi_vals - omega*np.ones(len(psi_vals))
    r = a*(1-e**2)/(np.ones(len(phi))+e*np.cos(phi))
    R_g = 2*G*M_c/c**2
    amplification = np.zeros((len(i), len(psi_vals)))
    for j in range(len(i)):
        R = r*(1-(np.sin(np.radians(i[j])))**2*(np.sin(psi_vals))**2)**0.5
        a_pll = a*np.sin(np.radians(i[j]))*(1-e**2)/(1+e*np.sin(omega))
        R_E = (2*R_g*a_pll)**0.5
        u = R/R_E
        if flag == 1:
            amplification[j,:] = (u**2+2)/(2*u*(u**2+4)**0.5)-0.5  # dominant
        else:
            amplification[j,:] = (u**2+2)/(2*u*(u**2+4)**0.5)+0.5  # subdominant
        plt.plot(np.degrees(psi_vals), amplification[j,:])
    
    plt.xlim(89,91)
    plt.xlabel('$Longitude \quad (degree)$', fontsize=15)
    if flag == 1:
        plt.yscale('log')
        plt.title('Sub-dominant image')
        plt.ylabel("$A_{-}$")
    else:
        plt.title('Dominant image')
        plt.ylabel("$A_{+}$")
    plt.legend(i)
    plt.show()
    

# example call for this function
# amp_plot(8.784*1e8, 0.0878, np.radians(73.8), [90.14,90.28,90.56], 1.25*M_0,1)

# for demo, run
# amp_plot()



