import csv
from sympy import symbols, Eq, solve, I, re, im, N

# set constants for the code
MAXITER = 8                                     # the maximum depth you want to find points at
HEADER = ["k", "n", "real_part", "imaginary_part"]    # information in the header of the csv file

# generates expressions to be solved based on how long it is
def genExpression(i):
    return "".join(["(" for _ in range(i)]) + "c" + "".join([") ** 2 + c" for _ in range(i)])

def genPoint(k, n):

    # defines symbol
    c = symbols('c')

    # generates solution
    solutions = solve([
                    Eq(
                        eval(genExpression(k-1)),         # first expression
                        eval(genExpression(k+n-1))     # second expression
                    )
                ])
    
    # creates output
    output = []
    
    # fill output with soltuions
    for solution in solutions:
        output.append([k, n, N(re(solution[c])), N(im(solution[c]))])

    return output


with open("points.csv", "w") as f:

    # creates writer
    writer = csv.writer(f)

    # adds the header
    writer.writerow(HEADER)

    # generates a row and adds to file
    for i in range(MAXITER):
        for j in range(0, MAXITER - i):
            points = genPoint(i, j)
            if not points:
                continue
            for point in points:
                writer.writerow(point)
