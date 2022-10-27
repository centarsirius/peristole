import numpy as np
import matplotlib.pyplot as plt 

# defining the constants
 
G = 6.674*1e-11     # in SI units 
c = 3*1e8           # in SI units
M_0 = 1.989e30      # mass of the sun in SI units
psi_vals = np.linspace(np.radians(89), np.radians(91), 100)  # psi is the true anomaly measured from the ascending node of the pulsar

class pulsar:
    axis=8.784E8
    ecc=0.0878
    omega=73.8
    period =22.7E-3 #changed time to period
    angle=[90.14,90.28,90.56]
    mass=1.25
    eta=45
    zeta=50
    alpha=4
    big_phi0=115
    
    def __init__(self, mass):
        self.mass=mass
    
    def a(self, axis):
        self.axis = axis

    def e(self, ecc):
        self.ecc = ecc

    def o(self, omega):
        self.omega = omega

    def i(self, angle):
        if not isinstance(angle, (list, set, tuple)):
            angle = [angle]
        self.angle = angle

    def t(self, period):
        self.period = period #change time to period everywhere

    def et(self, eta):
        self.eta = eta

    def zet(self, zeta):
        self.zeta = zeta
    
    def alph(self, alpha):
        self.alpha = alpha

    def b_phi(self, big_phi0): #change big_phi0 to something else for user friendliness
        self.big_phi0 = big_phi0

def details(pulsar):
    print(pulsar.mass, pulsar.axis, pulsar.ecc, pulsar.omega, pulsar.angle, pulsar.eta, pulsar.zeta)


def amp_plot(pulsar, flag=0): 
    """
    Provides amplification factor for the dominant and subdominant images plotted as a function of 
    longitude.
    
    Args: 
       pulsar: An object of the pulsar class
       flag: An optional argument which if set to 1 gives the plot for the subdominant case
       
    Returns:
       The amplification factor plot
       
    Example call of the function:
       demo = pulsar_class()
       demo.default(demo)
       amp_plot(demo)
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
# pulsar1 = peri.pulsar()
# pulsar1.mass = 1.25
# pulsar1.axis=3E8
# pulsar1.ecc=0.5
# pulsar1.omega=50
# pulsar1.angle=[90.2, 90.4]

# details(pulsar1)
# amp_plot(pulsar1)
# amp_plot_demo()

# print(pulsar.mass)
# print(pulsar.ecc)
# pulsar.ecc=0.9
# print(pulsar.e)
# print(pulsar.ecc)
# print(pulsar.omega)
# details(pulsar)
# amp_plot(pulsar)
