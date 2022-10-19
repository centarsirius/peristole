from cgi import print_directory
from contextlib import suppress

class pulsar:
    
    def __init__(self):
        pass

    def default(self, name= 'PSR J0737-3039', mass= 1.25, axis=8.784E8, ecc=0.0878, omega=73.8, period =22.7E-3, angle=[90.14,90.28,90.56], eta=45, zeta=50, alpha=4, big_phi0=115):
        self.name=name
        self.mass = mass
        self.axis = axis 
        self.ecc = ecc 
        self.omega = omega
        self.angle = angle 
        self.period = period 
        self.eta = eta 
        self.zeta = zeta 
        self.alpha = alpha 
        self.big_phi0 = big_phi0 
    
    def a(self, axis):
        self.axis = axis 

    def m(self, mass):
        self.mass = mass

    def e(self, ecc):
        self.ecc = ecc 

    def o(self, omega):
        self.omega = omega

    def i(self, angle):
        self.angle = angle 

    def t(self, period): #change time to period everywhere
        self.period = period 

    def et(self, eta):
        self.eta = eta 

    def zet(self, zeta):
        self.zeta = zeta 
    
    def alph(self, alpha):
        self.alpha = alpha 

    def b_phi(self, big_phi0): #change big_phi0 to something else for user friendliness
        self.big_phi0 = big_phi0 

    def details(self):
        #print(pulsar.mass, pulsar.axis, pulsar.ecc, pulsar.omega, pulsar.angle, pulsar.period, pulsar.eta, pulsar.zeta, pulsar.alpha, pulsar.big_phi0)
        with suppress(AttributeError):
            print("system parameters ")
            print("mass of secondary pulsar: ", self.mass, " solar mass")
            print("orbital semimajor axis: ", self.axis, " meters")
            print("eccentricity of system: ", self.ecc)
            print("longitude of periastron: ", self.omega)
            print("orbital inclination angle(s): ", self.angle)
            print("spin period of primary self: ", self.period, " seconds")
            print("angle between spin axis and magnetic axis: ", self.alpha)
            print("to be filled: ", self.eta)
            print("opening angle: ", self.zeta)
            print("to be filled: ", self.big_phi0)

demo=pulsar()
demo.default(demo)
#peri.demo.details()
