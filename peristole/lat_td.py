import numpy as np
import matplotlib.pyplot as plt

# defining the constants

G = 6.674*1e-11     # in SI units 
c = 3e8             # in SI units
M_0 = 1.989e30      # mass of the sun 
psi_vals = np.linspace(np.radians(89), np.radians(91), 1001) # psi is the true anomaly measured from the ascending node of the pulsar

def delay_lat(pulsar, flag=0, dummy='default'):
    """Latitudinal lensing delay
    
    Provides latitudinal lensing delay for the dominant and subdominant images plotted as a function of 
    longitude. Needs mass, axis, ecc, angle, omega, period, eta, zeta, alpha, phi_0 to be already declared.
    

    Args: 
       pulsar: An object of the pulsar class
       flag: An optional argument which if set to 1 gives the plot for the subdominant case


    Returns:
       The latitudinal lensing delay plot
    
       
    Example call of the function:
       example = pulsar()
       ...
       delay_lat(example,1)
    """
    phi = psi_vals - np.radians(pulsar.omega)*np.ones(len(psi_vals))
    r = pulsar.axis*(1-pulsar.ecc**2)/(np.ones(len(phi))+pulsar.ecc*np.cos(phi))
    R_g = 2*G*pulsar.mass*M_0/c**2
    lat_delay = np.zeros((len(pulsar.angle), len(psi_vals)))
    chi0=(np.sin(np.radians(pulsar.alpha))*np.sin(np.radians(pulsar.phi_0)))/((np.cos(np.radians(pulsar.alpha))*np.sin(np.radians(pulsar.zeta)))-(np.cos(np.radians(pulsar.phi_0))*np.sin(np.radians(pulsar.alpha))*np.cos(np.radians(pulsar.zeta))))
    
    for j in range(len(pulsar.angle)):
        R_s = r*(np.ones(len(psi_vals))-(np.sin(np.radians(pulsar.angle[j])))**2*(np.sin(psi_vals))**2)**0.5
        a_pll = pulsar.axis*np.sin(np.radians(pulsar.angle[j]))*(1-pulsar.ecc**2)/(1+pulsar.ecc*np.sin(np.radians(pulsar.omega))) 
        R_E = (2*R_g*a_pll)**0.5
        omega_p=2*np.pi/pulsar.period
        if flag==1:
           delta_R_pm = 0.5*(-(R_s**2+4*(R_E**2)*np.ones(len(R_s)))**0.5-R_s)
           lat_delay[j,:] = (delta_R_pm/R_s)*(r/a_pll)*(np.cos(np.radians(pulsar.eta))*np.cos(psi_vals)+np.cos(np.radians(pulsar.angle[j]))*np.sin(np.radians(pulsar.eta))*np.sin(psi_vals))/(omega_p*np.sin(np.radians(pulsar.zeta))*chi0)
        else:
           delta_R_pm = 0.5*((R_s**2+4*(R_E**2)*np.ones(len(R_s)))**0.5-R_s) 
           lat_delay[j,:] = (delta_R_pm/R_s)*(r/a_pll)*(np.cos(np.radians(pulsar.eta))*np.cos(psi_vals)+np.cos(np.radians(pulsar.angle[j]))*np.sin(np.radians(pulsar.eta))*np.sin(psi_vals))/(omega_p*np.sin(np.radians(pulsar.zeta))*chi0)
        if dummy == 'default':
            plt.plot(np.degrees(psi_vals), lat_delay[j,:]*1e6)
    
    if dummy=='only value':
        return lat_delay

    plt.xlim(89,91)
    plt.locator_params(nbins=4)
    plt.xlabel('$Longitude \quad (degree)$', fontsize=15)
    plt.ylabel(r'$(\Delta t)_{L}^{(lat)} \quad (\mu s)$', fontsize=15)
    plt.tick_params(axis='both', direction='in', which='major', length=10)
    if flag==1:
        plt.title('Time delay due to latitudinal lensing (subdominant image)', fontsize=20, fontweight='bold')
    else:
        plt.title('Time delay due to latitudinal lensing (dominant image)', fontsize=20, fontweight='bold')
    plt.legend(pulsar.angle)
    plt.show()
    
