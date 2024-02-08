import numpy as np
from sympy import symbols, solve

array = []
x, y, z = symbols('x, y, z')

equation_amount = int(input("Give me number of equations to solve \n"))
input("Enter equation in this style :x+y+z-1\n"
      "Press enter to continue.")
for i in range(equation_amount):
    equation = input(f"Give equation {i + 1}!")
    array.append(equation)


result = solve(array, [x, y, z])


'''A3 = solve([x + y + z - 3,
            2 * x + y + z - 2,
            x - 2 * y - 2 * z + 2], [x, y, z])'''

print(result)