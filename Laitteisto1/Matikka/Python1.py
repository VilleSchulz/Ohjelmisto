import random

import numpy as np
#1 tehtävä
number = np.random.randint(0,9,5)
print(number)

#tehtävä 2a)
u = np.array([2,3])
v = np.array([4,-7])
uv = np.array([[2,3],
               [4,-7]])

#tehtävä 2b)
uu = np.array([1,1,1])
vv = np.array([3,-3,2])
uuvv = np.array([[1,1,1],
                [3,-3,2]])

#tehtävä 3)
u_normi = np.linalg.norm(u)
v_normi = np.linalg.norm(v)
uv_normi = np.linalg.norm(uv)
uu_normi = np.linalg.norm(uu)
vv_normi = np.linalg.norm(vv)
uuvv_normi = np.linalg.norm(uuvv)
print(f'U-normi = {u_normi}',f'V-normi = {v_normi}'
      f'UV-normi = {uv_normi}',f'UU-normi = {uu_normi}',
      f'vv-normi = {vv_normi}',f'UUVV-normi = {uuvv_normi}')

