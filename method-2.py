"""
a AND b VARIABLES REPRESENT a + bi IN A COMPLEX NUMBER
"""

# SETTINGS - CHANGE FOR DIFFERENT RESULTS
MAX_N = 100             # LIMIT MAX PERIOD
K_BOUNDS = [2, 100]     # LIMIT PREPERIOD STEPS - LOWER BOUND MUST BE AT LEAST 2 
MNOTATIONLABEL = False  # DEFINES IF WE WANT LABELS OR NOT

# different headers depending on what type of program is being run
HEADERMLABEL = ["k", "n", "a", "b"]   # preperiod, period, a + bi
HEADER = ["a", "b"]

# differnet filenames depending on label
FILENAMELABEL   = "points-labeled"
FILENAMENOLABEL = "points-no-label"

import random                   # for point generation
import csv                      # for writing to file
from complex import Complex     # math with complex numbers

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
with open(f"{FILENAMELABEL if MNOTATIONLABEL else FILENAMENOLABEL}.csv", "w") as f:

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

        # checks if c is periodic or any values are NoneType
        skip = False
        for i in range(K_BOUNDS[0], maximum):

            # if it is equal, c is periodic and we skip
            try:
                if values[i] == c:
                    skip = True
            except:
                skip = True     # detects for NoneType

        # goes to the next generated number
        if skip:
            continue

        # we need labels so we need to check individual equalitie 
        if MNOTATIONLABEL:
            # checks for equality within bounds
            for i in range(K_BOUNDS[0], K_BOUNDS[1]):

                for j in range(i+1, maximum):

                    # continue if there is a NoneType object in next - meaning there is no equality
                    if values[i] == values[j] and values[i-1] != values[j-1]:   # make sure they are equal only in that instance

                        # get parameters
                        k = i               # determines preperiod
                        n = j - i           # how far it went

                        # write to file
                        writer.writerow([k, n, c.a, c.b])
 

        # we don't need the labels so it should be quicker
        else:

            # chops bounds off lower end 
            values = values[K_BOUNDS[0]::]

            # converts values to set
            valuesSet = set(values)

            # if the length of the set is less, that means there are equalities present - then we just add the thing to the file
            if len(values) > len(valuesSet):
                writer.writerow([c.a, c.b])
