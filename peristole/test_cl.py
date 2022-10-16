import numpy as np
import matplotlib.pyplot as plt 

# defining the constants
 
G = 6.674*1e-11 # in SI units 
c = 3*1e8 # in SI units
M_0 = 1.989e30 # mass of the sun 
psi_vals = np.linspace(np.radians(89), np.radians(91), 100)
# the true anomaly measured from the ascending node of the pulsar

class pulsar:

	# The init method or constructor
	def __init__(self, mass):
		self.mass=mass
	
	# Adds an instance variable
	def axis(self, axis):
		self.axis = axis

	def e(self, ecc):
		self.ecc = ecc

	def omega(self, omega):
		self.omega = omega

	def angle(self, angle):
		self.angle = angle

def details(pulsar):
	print(pulsar.mass, pulsar.axis, pulsar.ecc, pulsar.omega, pulsar.angle)
	
def amp_plot_demo(a=8.784*1e8, e=0.0878, omega=73.8, i=[90.14,90.28,90.56], M_c=1.25, flag=0): 
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

    phi = psi_vals - np.radians(omega)*np.ones(len(psi_vals))
    r = a*(1-e**2)/(np.ones(len(phi))+e*np.cos(phi))
    R_g = 2*G*M_c*M_0/c**2
    amplification = np.zeros((len(i), len(psi_vals)))
    for j in range(len(i)):
        R = r*(1-(np.sin(np.radians(i[j])))**2*(np.sin(psi_vals))**2)**0.5
        a_pll = a*np.sin(np.radians(i[j]))*(1-e**2)/(1+e*np.sin(np.radians(omega)))
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


def amp_plot(pulsar, flag=0): 
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
	
    phi = psi_vals - np.radians(pulsar.omega)*np.ones(len(psi_vals))
    r = pulsar.axis*(1-pulsar.ecc**2)/(np.ones(len(phi))+pulsar.ecc*np.cos(phi))
    R_g = 2*G*pulsar.mass*M_0/c**2
    amplification = np.zeros((len(pulsar.angle), len(psi_vals)))
    for j in range(len(pulsar.angle)):
        R = r*(1-(np.sin(np.radians(pulsar.angle[j])))**2*(np.sin(psi_vals))**2)**0.5
        a_pll = pulsar.axis*np.sin(np.radians(pulsar.angle[j]))*(1-pulsar.ecc**2)/(1+pulsar.ecc*np.sin(np.radians(pulsar.omega)))
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
    plt.legend(pulsar.angle)
    plt.show()


# Driver Code
# pulsar1 = pulsar(20)
# pulsar1.axis=8.784*1e8
# pulsar1.ecc=0.0878
# pulsar1.omega=73.8
# pulsar1.angle=[0, 45, 90,90.2, 90.4,91, 135, 180]

# details(pulsar1)
# amp_plot(pulsar1)
# amp_plot_demo()
