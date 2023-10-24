
import numpy as np
#Tehtävä1_1
a= 2.493
b=0.911

a_asteet = np.degrees(a)
b_asteet = np.degrees(b)

print(round(a_asteet, 1))
print(round(b_asteet, 1))

#Tehtävä1_2
import numpy as np
a= 137.7
b=62.3

a_radiaani = np.radians(a)
b_radiaani = np.radians(b)

print(round(a_radiaani, 3))
print(round(b_radiaani, 3))

#Tehtävä1_3
import numpy as np
A = np.array([30, 45, 60,90,120,135,150,180,270,360])

for i in A:
    radian =np.radians(i)
    print(round(radian,3))

#Tehtävä2_1
a=1.6
b=2.3
c = np.hypot(a,b)
print(round(c,1))



