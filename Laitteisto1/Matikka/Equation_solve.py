import numpy as np
from sympy import symbols,solve
x, y, z = symbols('x, y, z')


A3 = solve([x+y+z-3,
           2*x+y+z-2,
           x-2*y-2*z+2],[x,y,z])
print(f"c) ={A3}\n")
