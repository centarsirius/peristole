#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 21:31:50 2022

@author: centarsirius
"""
import numpy as np
import matplotlib.pyplot as plt

G = 6.674*1e-11 # in SI units 
c = 3*1e8 # in m/s
M_sun=1.9884099*10E30

i=[np.radians(90.14), np.radians(90.28), np.radians(90.56)] #edge-on inclination angles
phi=np.linspace(np.radians(89),np.radians(91),1001) # varying from 89 to 91
e=0.0878 #eccentricity
o_peri=np.radians(73.8) #periastron
omega_p=1/22.7 #angular frequency in micro secs
a=8.784E7 #orbital semimajor axis
M_c=1.25*M_sun
a_bar = a*np.sin(i)*(1-e**2)/(1+e*np.sin(o_peri))
R_g = 2*G*M_c/c**2
R_E = (2*R_g*a)**0.5
eta=np.radians(45) #eta - angle bw orbit and spin axis projection
zeta=np.radians(50) #zeta - angle of separation bw line of sight and spin axis
big_phi=phi-o_peri #orbital true anomaly
big_phi0=np.radians(115)
alpha=np.radians(4) #angle between spin axis and magnetic axis
chi0=np.arctan((np.sin(alpha)*np.sin(big_phi0))/((np.cos(alpha)*np.sin(zeta))-(np.cos(big_phi0)*np.sin(alpha)*np.cos(zeta))))


for ang in range(0,3):
    a_bar=(a*np.sin(i[ang])*(1-e**2))/(1+e*np.sin(o_peri))
    r= a*(1-e**2)/(1+e*np.cos(big_phi))
    R= r*np.sqrt(1-(np.sin(i[ang]))**2*(np.sin(phi)**2))
    dri=0.5*(np.sqrt(R**2+(4*(R_E)**2))-R)
    #drn=0.5*(-np.sqrt(R**2+(4*(R_E)**2))-R)

    dtr_d=-(dri/(a_bar*omega_p))*((np.sin(eta)*np.cos(phi)-(np.cos(i[ang])*np.cos(eta)*np.sin(phi)))/(np.sin(zeta)*np.sqrt(1-np.sin(i[ang])**2*np.sin(phi)**2))) #eq 10

    if ang==0:
        plt.plot(np.degrees(phi), dtr_d, linestyle='--', label= '$90^{o}.14$', color='blue') #label=np.degrees(i[ang]))
    elif ang==1:
        plt.plot(np.degrees(phi), dtr_d, linestyle='--', dashes=[12,5], label= '$90^{o}.28$', color='firebrick') #label=np.degrees(i[ang]))
    else:
        plt.plot(np.degrees(phi), dtr_d, label= '$90^{o}.56$', color='black') #label=np.degrees(i[ang]))
    #plt.plot(phi, dtln)
    plt.xlim([89,91])
    plt.locator_params(nbins=4)
    plt.xlabel('$Longitude \quad (degree)$', fontsize=15)
    plt.ylabel(r'$(\Delta t)_{L} \quad (\mu s)$', fontsize=15)
    plt.tick_params(axis='both', direction='in', which='major', length=10)
    plt.legend(loc='center right', title='Inclination angle')
    plt.title('Time delay due to rotational lensing (dominant image)', fontsize=20, fontweight='bold')
plt.show()

chi0=np.arctan((np.sin(alpha)*np.sin(big_phi0))/((np.cos(alpha)*np.sin(zeta))-(np.cos(big_phi0)*np.sin(alpha)*np.cos(zeta))))

"""
for ang in range(0,3):
    a_bar=(a*np.sin(i[ang])*(1-e**2))/(1+e*np.sin(o_peri))
    r= a*(1-e**2)/(1+e*np.cos(  phi))
    R= r*np.sqrt(1-(np.sin(i[ang]))**2*(np.sin(phi)**2))
    dri=0.5*(np.sqrt(R**2+(4*(R_E)**2))-R)
    #drn=0.5*(-np.sqrt(R**2+(4*(R_E)**2))-R)

    dtl_d=(dri/(a_bar*omega_p))*((np.cos(eta)*np.cos(phi)+(np.cos(i[ang])*np.sin(eta)*np.sin(phi)))/(np.sin(zeta)*np.tan(chi0)*np.sqrt(1-np.sin(i[ang])**2*np.sin(phi)**2))) #eq 24
    #dtl=(dri/(a_bar*omega_p))*((np.cos(eta)*np.cos(phi)+(np.cos(i[ang])*np.sin(eta)*np.sin(phi)))/(np.sin(zeta)*0.08*np.sqrt(1-np.sin(i[ang])**2*np.sin(phi)**2))) 

    if ang==0:
        plt.plot(np.degrees(phi), dtl_d, linestyle='--', label= '$90^{o}.14$', color='blue') #label=np.degrees(i[ang]))
    elif ang==1:
        plt.plot(np.degrees(phi), dtl_d, linestyle='--', dashes=[12,5], label= '$90^{o}.28$', color='firebrick') #label=np.degrees(i[ang]))
    else:
        plt.plot(np.degrees(phi), dtl_d, label= '$90^{o}.56$', color='black') #label=np.degrees(i[ang]))
    #plt.plot(phi, dtln)
    plt.xlim([89,91])
    plt.locator_params(nbins=4)
    plt.xlabel('$Longitude \quad (degree)$', fontsize=15)
    plt.ylabel(r'$(\Delta t)_{L} \quad (\mu s)$', fontsize=15)
    plt.tick_params(axis='both', direction='in', which='major', length=10)
    plt.legend(loc='center right', title='Inclination angle')
    plt.title('Time delay due to latitudinal lensing (dominant image)', fontsize=20, fontweight='bold')
plt.show()


for ang in range(0,3):
    a_bar=(a*np.sin(i[ang])*(1-e**2))/(1+e*np.sin(o_peri))
    r= a*(1-e**2)/(1+e*np.cos(big_phi))
    R= r*np.sqrt(1-(np.sin(i[ang]))**2*(np.sin(phi)**2))
    #dri=0.5*(np.sqrt(R**2+(4*(R_E)**2))-R)
    drn=0.5*(-np.sqrt(R**2+(4*(R_E)**2))-R)

    dtr_s=-(drn/(a_bar*omega_p))*((np.sin(eta)*np.cos(phi)-(np.cos(i[ang])*np.cos(eta)*np.sin(phi)))/(np.sin(zeta)*np.sqrt(1-np.sin(i[ang])**2*np.sin(phi)**2))) #eq 10
    #dtln=-(drn/(a_bar*omega_p))*((np.sin(eta)*np.cos(phi)-(np.cos(i)*np.cos(eta)*np.sin(phi)))/(np.sin(zeta)*np.sqrt(1-np.sin(i)**2*np.sin(phi)**2)))   

    if ang==0:
        plt.plot(np.degrees(phi), dtr_s, linestyle='--', label= '$90^{o}.14$', color='blue') #label=np.degrees(i[ang]))
    elif ang==1:
        plt.plot(np.degrees(phi), dtr_s, linestyle='--', dashes=[12,5], label= '$90^{o}.28$', color='firebrick') #label=np.degrees(i[ang]))
    else:
        plt.plot(np.degrees(phi), dtr_s, label= '$90^{o}.56$', color='black') #label=np.degrees(i[ang]))
    #plt.plot(phi, dtln)
    plt.xlim([89,91])
    plt.locator_params(nbins=4)
    plt.xlabel('$Longitude \quad (degree)$', fontsize=15)
    plt.ylabel(r'$(\Delta t)_{L} \quad (\mu s)$', fontsize=15)
    plt.tick_params(axis='both', direction='in', which='major', length=10)
    plt.legend(loc='center right', title='Inclination angle')
    plt.title('Time delay due to rotational lensing (subdominant image)', fontsize=20, fontweight='bold')
plt.show()

chi0=np.arctan((np.sin(alpha)*np.sin(big_phi0))/((np.cos(alpha)*np.sin(zeta))-(np.cos(big_phi0)*np.sin(alpha)*np.cos(zeta))))

for ang in range(0,3):
    a_bar=(a*np.sin(i[ang])*(1-e**2))/(1+e*np.sin(o_peri))
    r= a*(1-e**2)/(1+e*np.cos(  phi))
    R= r*np.sqrt(1-(np.sin(i[ang]))**2*(np.sin(phi)**2))
    #dri=0.5*(np.sqrt(R**2+(4*(R_E)**2))-R)
    drn=0.5*(-np.sqrt(R**2+(4*(R_E)**2))-R)

    dtl_s=(drn/(a_bar*omega_p))*((np.cos(eta)*np.cos(phi)+(np.cos(i[ang])*np.sin(eta)*np.sin(phi)))/(np.sin(zeta)*np.tan(chi0)*np.sqrt(1-np.sin(i[ang])**2*np.sin(phi)**2)))
    #dtl=(dri/(a_bar*omega_p))*((np.cos(eta)*np.cos(phi)+(np.cos(i[ang])*np.sin(eta)*np.sin(phi)))/(np.sin(zeta)*0.08*np.sqrt(1-np.sin(i[ang])**2*np.sin(phi)**2))) 

    if ang==0:
        plt.plot(np.degrees(phi), dtl_s, linestyle='--', label= '$90^{o}.14$', color='blue') #label=np.degrees(i[ang]))
    elif ang==1:
        plt.plot(np.degrees(phi), dtl_s, linestyle='--', dashes=[12,5], label= '$90^{o}.28$', color='firebrick') #label=np.degrees(i[ang]))
    else:
        plt.plot(np.degrees(phi), dtl_s, label= '$90^{o}.56$', color='black') #label=np.degrees(i[ang]))
    #plt.plot(phi, dtln)
    plt.xlim([89,91])
    plt.locator_params(nbins=4)
    plt.xlabel('$Longitude \quad (degree)$', fontsize=15)
    plt.ylabel(r'$(\Delta t)_{L}^{(lat)} \quad (\mu s)$', fontsize=15)
    plt.tick_params(axis='both', direction='in', which='major', length=10)
    plt.legend(loc='center right', title='Inclination angle')
    plt.title('Time delay due to latitudinal lensing (subdominant image)', fontsize=20, fontweight='bold')
plt.show()"""