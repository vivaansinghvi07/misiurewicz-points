# represent complex numbers
class Complex:

    # defines how strcit to check for equalities
    EQUALITYSTRICTNESS = 0.0000000001
    HASHROUNDINGDIGITS = 10

    # creates a new complex number a + bi
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    # square itself
    def square(self):
        self.a, self.b = self.a ** 2 - self.b ** 2, 2 * self.a * self.b

    # add two numbers together
    def add(self, other):
        self.a += other.a
        self.b += other.b

    # find magnitude
    def mag(self):
        return (self.a**2 + self.b**2)**0.5

    # check for equality
    def __eq__(self, other):
        return (abs(self.a - other.a) < Complex.EQUALITYSTRICTNESS 
            and abs(self.b - other.b) < Complex.EQUALITYSTRICTNESS) 
    
    # hashes the complex number
    def __hash__(self):
        return int(str(hash(round(self.a, Complex.HASHROUNDINGDIGITS))) + "0000" + str(abs(hash(round(self.b, Complex.HASHROUNDINGDIGITS)))))