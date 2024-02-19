from sympy import symbols, solve
x, y, z = symbols('x, y, z')
A1 = solve([5*x +3* y - 9,
            2 * x + y -4], [x, y, z])

A2 = solve([2*x + y + z -6,
            x + 3*y + z -2,
            2*x + y +2 * z - 9], [x, y, z])
A3 = solve([x + y +3*z +1,
            3 * x + y + z -5,
            2*x + y +2* z -2], [x, y, z])

print(f"1a){A1}\n"
      f"1b){A2}\n"
      f"1c){A3}\n")