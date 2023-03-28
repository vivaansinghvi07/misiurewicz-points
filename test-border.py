import csv                      # for reading from file
from complex import Complex     # for complex math

# defines name of file being looked at
FILENAME = "points-no-label"    # THIS IS THE ONLY THING SUPPORTED FOR NOW
CHECKDEPTH = 1000
BORDERSTRICTNESS = 1.9

# performs check - returns new complex number
def check(depth, c):
    # this is the one that will be squared
    z = Complex(0, 0)   # REPRESENTS ITERATION 1

    # does the iterations - if overflow, return None - test failed
    for _ in range(depth):
        z.square()      # squares 
        z.add(c)        # adds constant

    # return magnitude
    return z.mag()

# opens two files for data conversions
with open(f"{FILENAME}.csv", "r") as inp:
    with open("border-points.csv", "w") as out:
        
        # reader for first file
        reader = csv.DictReader(inp)

        # writer for the second file and writes header
        writer = csv.writer(out)
        writer.writerow(reader.fieldnames)

        # iterates through every point
        for point in reader:

            # gets complex point
            c = Complex(float(point["a"]), float(point["b"]))

            # runs border check
            if check(depth=CHECKDEPTH, c=c) > BORDERSTRICTNESS:
                writer.writerow([point["a"], point["b"]])
            
