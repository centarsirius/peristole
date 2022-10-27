from contextlib import suppress

class pulsar:
    """
    Initiates a pulsar object with the given name allowing you to specify the physical parameters of the double pulsar system. 
       

    Args: 
        mass: Mass of the pulsar playing the role of the lensing companion (labelled B), with A being the pulsar whose delays are to be plotted (in units of solar mass)
        axis: Semi-major axis of the orbit of the system (in metres)
        ecc: Eccentricity of the system 
        omega: Longitude of periastron (in degrees)
        period: Spin period of pulsar A (in seconds)
        angle: Orbital inclination angle (in degrees, can be a list)
        eta: Angle between the ascending node of the orbit and the projection of the unit vector along the pulsar spin axis on the sky plane (in degrees)
        zeta: Angle between the pulsar spin axis and the line of sight vector (in degrees)
        alpha: Angle between the pulsar spin axis and magnetic axis (in degrees)
        l: 


    Example call:
        example = pulsar()
        example.mass = 5
        example.ecc = 0.7
        ...
        example.eta = 30
    """
    def __init__(self):
        pass

    def default(self, name= 'PSR J0737-3039', mass= 1.25, axis=8.784E8, ecc=0.0878, omega=73.8, period =22.7E-3, angle=[90.14,90.28,90.56], eta=45, zeta=50, alpha=4, l=115):
        """
        Specifies the physical parameters of the double pulsar system. 
        
        Args: 
           name: Name of the system
           mass: Mass of the pulsar playing the role of the lensing companion (labelled B), with A being the pulsar whose delays are to be plotted (in units of solar mass)
           axis: Semi-major axis of the orbit of the system (in metres)
           ecc: Eccentricity of the system 
           omega: Longitude of periastron (in degrees)
           period: Spin period of pulsar A (in seconds)
           angle: Orbital inclination angle (in degrees, can be a list)
           eta: Angle between the ascending node of the orbit and the projection of the unit vector along the pulsar spin axis on the sky plane
           zeta: Angle between the pulsar spin axis and the line of sight vector 
           alpha: Angle between the pulsar spin axis and magnetic axis 
           big_phi0: 
        """
        
        
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
        self.l = l
    
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

    def t(self, period):
        self.period = period 

    def et(self, eta):
        self.eta = eta 

    def zet(self, zeta):
        self.zeta = zeta 
    
    def alph(self, alpha):
        self.alpha = alpha 

    def b_phi(self, l): 
        self.l = l

    def details(self):
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
            print("to be filled: ", self.l)

demo=pulsar()
demo.default(demo)
#peri.demo.details()
