# Misiurewicz Points
A very experimental approach to generating Misiurewicz points. 

## Credits
- This [Wikipedia Article](https://en.wikipedia.org/wiki/Misiurewicz_point), which cleared up the process for me.
- [@easai](https://github.com/easai/Misiurewicz)'s program to check if a point is a Misiurewicz point (used for checking accuracy of the program manually).

## Method 1: Solving Directly
In this method, I tried to solve for the points directly, using the `sympy` module to solve equations that generate these points, but it seems to be pretty ineffecient.

### How It Works 
The program iterates through posible combinations of pre-periods and periods, and plugs those values into an equation solver. For example, a point M with the preperiod 2 and period 1, would require fc(0) iterated 2 times and fc(0) iterated 3 times to be equal. So, the expression is expanded solved, and the resulting complex point is outputted.

### Parameters
- `MAXITER`: Determines the maxmimum sum of preperiod and period which the program will iterate through. 
- `HEADER`: Preset header settings for the csv file

### Outputs
This program outputs a csv file named `points.csv` with the preperiod, period, and point for each point generated. The rows are in the form of `k, n, a, b`. The file will not be very long; I was only able to generate with a period and preperiod sum of 8 before running into roadblocks on time.

## Method 2: Random Generation
In this method, I decided to randomly generate points and then check to see if the point was a Misiurewicz point. 

### How It Works
For each point, the program generates a series of iterates of f(z) - the function for the Mandelbrot Set - and then determines if there are equalities of any of the points. Of course, equalities involving the original point indicated that the point was periodic rather than prepeiodic, so it was scrapped. 

### Parameters
- `MAX_N`: The maximum period the program will evaluate.
- `K_BOUNDS`: Sets the bounds for the preperiod analyses.
- `MNOTATIONLABEL`: Determines if you want the labeled file or not
- `HEADERMLABEL` and `HEADER`: Stores header presets for each file type
- `FILENAMELABEL` and `FILENAMENOLABEL`: Stores filename presets
- `EQUALITYSTRICTNESS`: Stores the maximum degree of difference there can be when comparing accuracy of complex numbers
- `HASHROUNDINGDIGITS`: Stores the number of digits to which the hashing function rounds before outputting the integer. A lower rounding is a less precise accuracy check.

### Outputs
There are two settings which the program runs in: one with labels in M(k, n) format, and the other without. You can change this by changing the boolean variable `MNOTATIONLABEL`.

If the notation is being used, you will be presented with a csv file named `points-labeled.csv` in the form of `k, n, a, b` where `k` is the preperiod, `n` is the period, and `a` & `b` are the components of the complex number `c` (`a + bi`). If this notation is used, then points will often appear many times.

If the notation is not being used (set to `False`), the program will generate a csv file named `points-no-label.csv` in the form of `a, b`, only showing the components of the complex number. If this is used, points will more than likely not appear several times.

## Other Programs

### complex.py
This simply stores the Complex class for complex number math.

### test-border.py
This program is meant to iterate through points in `points-no-label.csv` and determine if they lie on the border of the Mandelbrot Set. The program will output a csv named `border-points.csv`, with the same format as `points-no-label.csv`, with points on the border.