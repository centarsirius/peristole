class pulsar:
    # axis=8.784E8
    # ecc=0.0878
    # omega=73.8
    # period =22.7E-3 #changed time to period
    # angle=[90.14,90.28,90.56]
    # mass=1.25
    # eta=45
    # zeta=50
    # alpha=4
    # big_phi0=115
    
    def __init__(self, mass= None):
        self.mass=mass if mass is not None else 1.25
    
    def a(self, axis = None):
        self.axis = axis if axis is not None else 8.784E8

    def e(self, ecc = None):
        self.ecc = ecc if ecc is not None else 0.0878

    def o(self, omega = None):
        self.omega = omega if omega is not None else 73.8

    def i(self, angle = None):
        self.angle = angle if angle is not None else [90.14,90.28,90.56]

    def t(self, period = None): #change time to period everywhere
        self.period = period if period is not None else 22.7E-3

    def et(self, eta = None):
        self.eta = eta if eta is not None else 45

    def zet(self, zeta = None):
        self.zeta = zeta if zeta is not None else 50
    
    def alph(self, alpha = None):
        self.alpha = alpha if alpha is not None else 4

    def b_phi(self, big_phi0 = None): #change big_phi0 to something else for user friendliness
        self.big_phi0 = big_phi0 if big_phi0 is not None else 115

def details(pulsar):
    #print(pulsar.mass, pulsar.axis, pulsar.ecc, pulsar.omega, pulsar.angle, pulsar.period, pulsar.eta, pulsar.zeta, pulsar.alpha, pulsar.big_phi0)
    print("system parameters")
    print("mass of secondary pulsar: ", pulsar.mass, " solar mass")
    print("orbital semimajor axis: ", pulsar.axis, " meters")
    print("eccentricity of system: ", pulsar.ecc)
    print("spin period of primary pulsar: ", pulsar.period, " seconds")
    print("longitude of periastron: ", pulsar.omega)
    print("orbital inclination angle(s): ", pulsar.angle)
    print("angle between spin axis and magnetic axis: ", pulsar.alpha)
    print("to be filled: ", pulsar.eta)
    print("opening angle: ", pulsar.zeta)
    print("to be filled: ", pulsar.big_phi0)


