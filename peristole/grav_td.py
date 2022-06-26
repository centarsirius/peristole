import numpy as np
import matplotlib.pyplot as plt 

# defining the constants
 
G = 6.674*1e-11 # in SI units 
c = 3e8 # in SI units
M_0 = 1.989e30 # mass of the sun 
psi_vals = np.linspace(np.radians(89), np.radians(91), 1001)  
# the true anomaly measured from the ascending node of the pulsar

def delay_geom(a=8.784*1e8, e=0.0878, omega=np.radians(73.8), i=[90.14,90.28,90.56], M_c=1.25*M_0, flag=0, dummy='default'):
    """
    Shows the geometric time delay 
    plotted as as a function of changing longitude. The user has 
    to provide information/parameters about the double pulsar 
    system in the following order - semi major axis, eccentricity, 
    the longitude of periastron in radians, a list of any length
    consisting of the different values of inclination angle
    of the orbital plane in degrees (i), 
    the mass of the companion pulsar, and a variable 'flag' 
    which shows the plot for the dominant image if left at 
    its default value 0 and shows the subdominant case if 
    set to 1. The variable named dummy is not relevant for 
    the user.
    """


    phi = psi_vals - np.radians(omega)*np.ones(len(psi_vals))
    r = a*(1-e**2)/(np.ones(len(phi))+e*np.cos(phi))
    R_g = 2*G*M_c/c**2
    geom_delay = np.zeros((len(i), len(psi_vals)))
    for j in range(len(i)):
        R_s = r*(1-(np.sin(np.radians(i[j])))**2*(np.sin(psi_vals))**2)**0.5
        a_pll = a*np.sin(np.radians(i[j]))*(1-e**2)/(1+e*np.sin(np.radians(omega)))    
        R_E = (2*R_g*a_pll)**0.5
        if flag==1:
            R_pm = 0.5*(R_s-(R_s**2+4*(R_E**2)*np.ones(len(R_s)))**0.5)
            delta_R_pm = abs(R_pm - R_s)
            geom_delay[j,:] = ((R_g/c)*(delta_R_pm/R_E)**2) 
        else:
            R_pm = 0.5*(R_s+(R_s**2+4*(R_E**2)*np.ones(len(R_s)))**0.5)
            delta_R_pm = abs(R_pm - R_s)
            geom_delay[j,:] = ((R_g/c)*(delta_R_pm/R_E)**2)
        if dummy == 'default':
            plt.plot(np.degrees(psi_vals), geom_delay[j,:])
    
    if dummy=='only value':
        return geom_delay
    
    plt.xlim(89,91)
    plt.xlabel('$Longitude \quad (degree)$', fontsize=15)
    plt.ylabel(r'$(\Delta t)_{geom} \quad (\mu s)$', fontsize=15)
    plt.tick_params(axis='both', direction='in', which='major', length=10)
    if flag==1:
        plt.title('Time delay due to geometric lensing (subdominant image)', fontsize=20, fontweight='bold')
    else:
        plt.title('Time delay due to geometric lensing (dominant image)', fontsize=20, fontweight='bold')
    plt.legend(i)
    plt.show()
    
# example call of this function -     
# delay_geom(8.784e8, 0.0878, np.radians(73.8), [90.14, 90.28, 90.56], 1.25*M_0)


def delay_grav(a=8.784*1e8, e=0.0878, omega=73.8, i=[90.14,90.28,90.56], M_c=1.25*M_0, flag=0, dummy='default'):
    """
    Shows the gravitational time delay 
    plotted as a function of changing longitude. The user has 
    to provide information/parameters about the double pulsar 
    system in the following order - semi major axis, eccentricity, 
    the longitude of periastron in radians, a list of any length
    consisting of the different values of inclination angle
    of the orbital plane in degrees (i), 
    the mass of the companion pulsar, and a variable 'flag' 
    which shows the plot for the dominant image if left at 
    its default value 0 and shows the subdominant case if 
    set to 1. The variable named dummy is not relevant for 
    the user.
    """
    
    phi = psi_vals - np.radians(omega)*np.ones(len(psi_vals))
    r = a*(1-e**2)/(np.ones(len(phi))+e*np.cos(phi))
    R_g = 2*G*M_c/c**2
    grav_delay = np.zeros((len(i), len(psi_vals)))
    for j in range(len(i)):
        a_pll = a*np.sin(np.radians(i[j]))*(1-e**2)/(1+e*np.sin(np.radians(omega)))
        R_s = r*(1-(np.sin(np.radians(i[j])))**2*(np.sin(psi_vals))**2)**0.5
        R_E = (2*R_g*a_pll)**0.5
        r_pll = r*np.sin(np.radians(i[j]))*np.sin(psi_vals)
        if flag==1:
            R_pm = 0.5*(R_s-(R_s**2+4*R_E**2)**0.5) #subdom
            grav_delay[j,:] = (-R_g/c)*np.log(((r_pll**2+R_pm**2)**0.5-r_pll)/(a*(1-e**2)))
        else:
            R_pm = 0.5*(R_s+(R_s**2+4*R_E**2)**0.5) #dom
            grav_delay[j,:] = (-R_g/c)*np.log(((r_pll**2+R_pm**2)**0.5-r_pll)/(a*(1-e**2)))
        if dummy == 'default':
            plt.plot(np.degrees(psi_vals), grav_delay[j,:])
    
    if dummy == 'only value':
        return grav_delay

    plt.xlim(89,91)
    plt.xlabel('$Longitude \quad (degree)$', fontsize=15)
    plt.ylabel(r'$(\Delta t)_{grav} \quad (\mu s)$', fontsize=15)
    plt.tick_params(axis='both', direction='in', which='major', length=10)
    if flag==1:
        plt.title('Time delay due to gravitational lensing (subdominant image)', fontsize=20, fontweight='bold')
    else:
        plt.title('Time delay due to gravitational lensing (dominant image)', fontsize=20, fontweight='bold')
    plt.legend(i)
    plt.show()
    
# example call of this function - 
# delay_grav(8.784e8, 0.0878, np.radians(73.8), [90.14, 90.28, 90.56], 1.25*M_0)

def delay_combined(a=8.784*1e8, e=0.0878, omega=73.8, i=[90.14,90.28,90.56], M_c=1.25*M_0, flag=0, dummy='default'):
    """
    Shows the combined gravitational and geometric time delay 
    plotted as a function of changing longitude. 
    The user has to provide information/parameters about 
    the double pulsar system in the following order - semi 
    major axis, eccentricity, the longitude of 
    periastron in radians, a list of any length
    consisting of the different values of inclination angle
    of the orbital plane in degrees (i), 
    the mass of the companion pulsar, and a variable 'flag' 
    which shows the plot for the dominant image if left at 
    its default value 0 and shows the subdominant case if 
    set to 1.
    """
    combined = delay_grav(a, e, np.radians(omega), i, M_c, flag, dummy='only value')+delay_geom(a, e, np.radians(omega), i, M_c, flag, dummy='only value')
    
    for j in range(len(i)):
        plt.plot(np.degrees(psi_vals), combined[j,:])    
    
    plt.xlim(89,91)
    plt.xlabel('$Longitude \quad (degree)$', fontsize=15)
    plt.ylabel(r'$(\Delta t)_{geom+grav} \quad (\mu s)$', fontsize=15)
    plt.tick_params(axis='both', direction='in', which='major', length=10)
    if flag==1:
        plt.title('Combined time delay due to geometric and gravitational lensing (subdominant image)', fontsize=20, fontweight='bold')
    else:
        plt.title('Combined time delay due to geometric and gravitational lensing (dominant image)', fontsize=20, fontweight='bold')
    plt.legend(i)
    plt.show()

# example call of this function - 
# delay_combined(8.784e8, 0.0878, np.radians(73.8), [90.14, 90.28, 90.56], 1.25*M_0)

# for demos, run - 
# delay_geom()
# delay grav()
# delay_combined()
