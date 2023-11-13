import math

from matplotlib import pyplot as plt, patches
import numpy as np
from fractions import Fraction as fr

import matplotlib as mpl

fig = plt.figure()
ax = fig.subplots()

ymp = patches.Circle((0, 0), radius=1, fill=0)
ax.add_patch(ymp)

# Move left y-axis and bottom x-axis to centre, passing through (0,0)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')

# Eliminate upper and right axes
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# Show ticks in the left and lower axes only
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

ax.axis('equal')

plt.xticks([-1, 0, 1], minor=True)
plt.yticks([-1, 0, 1])
angles = [30, 45, 60, 90, 120, 150, 180, 270]
my_array = np.array([])
for angle in angles:
    angle_rad = math.radians(angle)
    my_array = np.append(my_array,[math.cos(angle_rad), math.sin(angle_rad)])
my_array = my_array.reshape(-1,2)

plt.scatter(my_array[:, 0], my_array[:, 1], marker='x', c='blue')
print(my_array)
plt.show()