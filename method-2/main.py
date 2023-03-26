"""
a AND b VARIABLES REPRESENT a + bi IN A COMPLEX NUMBER
"""

# SETTINGS - CHANGE FOR DIFFERENT RESULTS
MAX_N = 100             # LIMIT MAX PERIOD
K_BOUNDS = [2, 100]     # LIMIT PREPERIOD STEPS - LOWER BOUND MUST BE AT LEAST 2 
MNOTATIONLABEL = True  # DEFINES IF WE WANT LABELS OR NOT


# different headers depending on what type of program is being run
HEADERMLABEL = ["k", "n", "a", "b"]   # preperiod, period, a + bi
HEADER = ["a", "b"]

# differnet filenames depending on label
FILENAMELABEL   = "points-labeled"
FILENAMENOLABEL = "points-no-label"

# represent complex numbers
class Complex:

    # defines how strcit to check for equalities
    EQUALITYSTRICTNESS = 0.0000000001

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

    # check for equality
    def __eq__(self, other):
        return (abs(self.a - other.a) < Complex.EQUALITYSTRICTNESS 
            and abs(self.b - other.b) < Complex.EQUALITYSTRICTNESS) 



import random   # for point generation
import csv      # for writing to file

# random number in bounds
def randomBounded(min, max):
    return random.random() * (max-min) + min

# performs check - returns new complex number
def check(iter, c):
    # this is the one that will be squared
    z = Complex(0, 0)   # REPRESENTS ITERATION 1

    # does the iterations - if overflow, return None - test failed
    try:
        for _ in range(iter):
            z.square()      # squares 
            z.add(c)        # adds constant
    except:
        return None
    
    # return new complex
    return z

# open the point file
with open(f"method-2/{FILENAMELABEL if MNOTATIONLABEL else FILENAMENOLABEL}.csv", "w") as f:

    # initialize writer and write header if just beginning
    writer = csv.writer(f)
    writer.writerow(HEADERMLABEL if MNOTATIONLABEL else HEADER)

    # generates new constants as long as possible
    while True:
        # generates random file
        c = Complex(randomBounded(-2, 0.5), randomBounded(-1.2, 1.2))       # represents c in the z**2 + c function

        # defines max value for array
        maximum = K_BOUNDS[1] + MAX_N

        # creates array of values
        values = [check(iter, c) for iter in range(maximum)]

        # checks if c is periodic
        skip = False
        for i in range(K_BOUNDS[0], maximum):

            # skip if None
            if not values[i]:
                continue

            # if it is equal, c is periodic and we skip
            if values[i] == c:
                skip = True

        # goes to the next generated number
        if skip:
            continue


        # we need labels so we need to check individual equalitie 
        if MNOTATIONLABEL:
            # checks for equality within bounds
            for i in range(K_BOUNDS[0], K_BOUNDS[1]):
                # checks if its none
                if not values[i]:
                    continue

                for j in range(i+1, maximum):

                    # checks if no value
                    if not values[j]:
                        continue

                    # continue if there is a NoneType object in next - meaning there is no equality
                    try:       
                        if values[i] == values[j] and values[i-1] != values[j-1]:   # make sure they are equal only in that instance

                            # get parameters
                            k = i               # determines preperiod
                            n = j - i           # how far it went

                            # write to file
                            writer.writerow([k, n, c.a, c.b])

                    except: 
                        continue

        # we don't need the labels so it should be quicker
        else:
            # TODO: code this
            pass