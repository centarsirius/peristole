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
    print(pulsar.mass, pulsar.axis, pulsar.ecc, pulsar.omega, pulsar.angle, pulsar.period, pulsar.eta, pulsar.zeta, pulsar.alpha, pulsar.big_phi0)
