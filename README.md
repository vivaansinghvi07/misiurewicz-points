# Misiurewicz Points
A very experimental approach to generating Misiurewicz points. Uses the `sympy` module to solve equations that generate these points, but, obviously, it seems to be pretty ineffecient.

## How It Works 
The program iterates through posible combinations of pre-periods and periods, and plugs those values into an equation solver. For example, a point M with the preperiod 2 and period 1, would require fc(0) iterated 2 times and fc(0) iterated 3 times to be equal. So, the expression is expanded solved, and the resulting complex point is outputted.