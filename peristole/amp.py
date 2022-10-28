import numpy as np
import matplotlib.pyplot as plt 

# defining the constants
 
G = 6.674*1e-11 # in SI units 
c = 3*1e8 # in SI units
M_0 = 1.989e30 # mass of the sun 
psi_vals = np.linspace(np.radians(89), np.radians(91), 1001) # psi is the true anomaly measured from the ascending node of the pulsar

def amp_plot(pulsar, flag=0): 
    """Amplification factor plot
    
    Provides amplification factor for the dominant and subdominant images plotted as a function of 
    longitude. Needs mass, axis, ecc, angle, omega to be already declared.
    

    Args: 
       pulsar: An object of the pulsar class
       flag: An optional argument which if set to 1 gives the plot for the subdominant case
       

    Returns:
       The amplification factor plot
      
       
    Example call of the function:
       example = pulsar()
       ...
       amp_plot(example, 1)
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
    plt.tick_params(axis='both', direction='in', which='major', length=10)
    if flag == 1:
        plt.yscale('log')
        plt.title('Amplification factor for the sub-dominant image', fontsize=20, fontweight='bold')
        plt.ylabel("$A_{-}$", fontsize=15)
    else:
        plt.title('Amplification factor for the dominant image', fontsize=20, fontweight='bold')
        plt.ylabel("$A_{+}$", fontsize=15)
    plt.legend(pulsar.angle)
    plt.show()
    
