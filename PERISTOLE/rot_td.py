import numpy as np
import matplotlib.pyplot as plt

# defining the constants
 
G = 6.674*1e-11 # in SI units 
c = 3e8 # in SI units
M_0 = 1.989e30 # mass of the sun 
psi_vals = np.linspace(np.radians(89), np.radians(91), 1001)  
#the true anomaly measured from the ascending node of the pulsar

def delay_lat(a, e, omega, time, i, M_c, eta, zeta, alpha, big_phi0, flag=0, dummy='default'):
    """
    The user has to provide information/parameters about 
    the double pulsar system in the following order - semi 
    major axis, eccentricity, the longitude of 
    periastron in radians, a list of any length
    consisting of the different values of inclination angle
    of the orbital plane in degrees (i), 
    the mass of the companion pulsar in solar mass, and a variable 'flag' 
    which shows the plot for the dominant image if left at 
    its default value 0 and shows the subdominant case if 
    set to 1. The variable named dummy is not relevant for 
    the user.
    eta - angle bw orbit and spin axis projection
    zeta - angle of separation bw line of sight and spin axis
    alpha=np.radians(4) #angle between spin axis and magnetic axis
    """
    phi = psi_vals - np.radians(omega)*np.ones(len(psi_vals))
    r = a*(1-e**2)/(np.ones(len(phi))+e*np.cos(phi))
    R_g = 2*G*M_c*M_0/c**2
    lat_delay = np.zeros((len(i), len(psi_vals)))
    for j in range(len(i)):
        R_s = r*(1-(np.sin(np.radians(i[j])))**2*(np.sin(psi_vals))**2)**0.5
        a_pll = a*np.sin(np.radians(i[j]))*(1-e**2)/(1+e*np.sin(np.radians(omega)))    
        R_E = (2*R_g*a_pll)**0.5
        chi0=np.arctan((np.sin(np.radians(alpha))*np.sin(np.radians(big_phi0)))/((np.cos(np.radians(alpha))*np.sin(np.radians(zeta)))-(np.cos(np.radians(big_phi0))*np.sin(np.radians(alpha))*np.cos(np.radians(zeta)))))
        if flag==1:
            R_pm = 0.5*(R_s-(R_s**2+4*(R_E**2)*np.ones(len(R_s)))**0.5)
            delta_R_pm = abs(R_pm - R_s)
            lat_delay[j,:] = (delta_R_pm*time/a_pll)*((np.cos(np.radians(eta))*np.cos(np.radians(phi))+(np.cos(np.radians(i[j]))*np.sin(np.radians(eta))*np.sin(np.radians(phi))))/(np.sin(np.radians(zeta))*np.tan(np.radians(chi0))*np.sqrt(1-np.sin(np.radians(i[j]))**2*np.sin(np.radians(phi))**2))) #eq 24
        else:
            R_pm = 0.5*(R_s+(R_s**2+4*(R_E**2)*np.ones(len(R_s)))**0.5)
            delta_R_pm = abs(R_pm - R_s)
            lat_delay[j,:] = (delta_R_pm*time/a_pll)*((np.cos(np.radians(eta))*np.cos(np.radians(phi))+(np.cos(np.radians(i[j]))*np.sin(np.radians(eta))*np.sin(np.radians(phi))))/(np.sin(np.radians(zeta))*np.tan(np.radians(chi0))*np.sqrt(1-np.sin(np.radians(i[j]))**2*np.sin(np.radians(phi))**2))) #eq 24
        if dummy == 'default':
            plt.plot(np.degrees(psi_vals), lat_delay[j,:])
    
    if dummy=='only value':
        return lat_delay

    plt.xlim(89,91)
    plt.xlabel('$Longitude \quad (degree)$', fontsize=15)
    plt.ylabel(r'$(\Delta t)_{L}^{(lat)} \quad (\mu s)$', fontsize=15)
    plt.tick_params(axis='both', direction='in', which='major', length=10)
    if flag==1:
        plt.title('Time delay due to latitudinal lensing (subdominant image)', fontsize=20, fontweight='bold')
    else:
        plt.title('Time delay due to latitudinal lensing (dominant image)', fontsize=20, fontweight='bold')
    plt.legend(i)
    plt.show()
    
# example call of this function -     
# delay_lat(8.784e8, 0.0878, 73.8, 22.7, [90.14, 90.28, 90.56], 1.25, 45, 50, 4, 115)


phi=np.linspace(np.radians(89),np.radians(91),1001) # varying from 89 to 91
e=0.0878 #eccentricity
o_peri=np.radians(73.8) #periastron
a=8.784E7 #orbital semimajor axis
M_c=1.25*const.M_sun.value
#R_E=np.sqrt(4*const.G*M_c*a/(const.c**2))
R_E=255000 #Einstein radius
omega_p=1/22.7 #angular frequency in micro secs
eta=np.radians(45) #eta - angle bw orbit and spin axis projection
zeta=np.radians(50) #zeta - angle of separation bw line of sight and spin axis
big_phi=phi-o_peri #orbital true anomaly
big_phi0=np.radians(115)
alpha=np.radians(4) #angle between spin axis and magnetic axis
chi0=np.arctan((np.sin(alpha)*np.sin(big_phi0))/((np.cos(alpha)*np.sin(zeta))-(np.cos(big_phi0)*np.sin(alpha)*np.cos(zeta))))

i=np.radians(90.14) #edge-on inclination angles

a_bar=(a*np.sin(i)*(1-e**2))/(1+e*np.sin(o_peri))
r= a*(1-e**2)/(1+e*np.cos(big_phi))
R= r*np.sqrt(1-(np.sin(i))**2*(np.sin(phi)**2))
dri=0.5*(np.sqrt(R**2+(4*(R_E)**2))-R)
drn=0.5*(-np.sqrt(R**2+(4*(R_E)**2))-R)

dtr_d=-(dri/(a_bar*omega_p))*((np.sin(eta)*np.cos(phi)-(np.cos(i)*np.cos(eta)*np.sin(phi)))/(np.sin(zeta)*np.sqrt(1-np.sin(i)**2*np.sin(phi)**2))) #eq 10

plt.plot(np.degrees(phi), dtr_d*100, linestyle='--', label= np.degrees(i), color='blue') #label=np.degrees(i[ang]))

plt.xlim([math.floor(np.degrees(i))-1,math.floor(np.degrees(i))+1])
plt.locator_params(nbins=4)
plt.xlabel('$Longitude \quad (degree)$', fontsize=15)
plt.ylabel(r'$(\Delta t)_{L} \quad (\mu s)$', fontsize=15)
plt.tick_params(axis='both', direction='in', which='major', length=10)
plt.legend(loc='center right', title='Inclination angle')
plt.title('Time delay due to rotational lensing (dominant image)', fontsize=20, fontweight='bold')
plt.show()

dtr_s=-(drn/(a_bar*omega_p))*((np.sin(eta)*np.cos(phi)-(np.cos(i)*np.cos(eta)*np.sin(phi)))/(np.sin(zeta)*np.sqrt(1-np.sin(i)**2*np.sin(phi)**2))) #eq 10

plt.plot(np.degrees(phi), dtr_s*100, linestyle='--', label= np.degrees(i), color='blue') #label=np.degrees(i[ang]))

plt.xlim([math.floor(np.degrees(i))-1,math.floor(np.degrees(i))+1])
plt.locator_params(nbins=4)
plt.xlabel('$Longitude \quad (degree)$', fontsize=15)
plt.ylabel(r'$(\Delta t)_{L} \quad (\mu s)$', fontsize=15)
plt.tick_params(axis='both', direction='in', which='major', length=10)
plt.legend(loc='center right', title='Inclination angle')
plt.title('Time delay due to rotational lensing (subdominant image)', fontsize=20, fontweight='bold')
plt.show()