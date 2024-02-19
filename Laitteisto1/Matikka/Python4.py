import numpy as np

# KERTOLASKUJA

# a
arr1 = np.array([[-1, 2],
                 [3, 1]])
arr2 = np.array([[0, 1, 3],
                 [2, -3, 5]])

# b
arr3 = np.array([[1, 3, 5],
                 [0, -2, 1],
                 [2, -1, 4]])
arr4 = np.array([[1],
                 [-3],
                 [-1]])
# c
arr5 = np.array([[2, 0, 1],
                 [1, -3, 4],
                 [0, 1, 5]])
arr6 = np.array([[3],
                 [-5],
                 [7]])

# d
arr7 = np.array([[1, -4, 2],
                 [3, 0, -2],
                 [2, 1, 0]])
arr8 = np.array([[5, 1, -1],
                 [-2, 1, 3],
                 [0, 3, 4]])
arr_result1 = np.matmul(arr1, arr2)
arr_result2 = np.matmul(arr3, arr4)
arr_result3 = np.matmul(arr5, arr6)
arr_result4 = np.matmul(arr7, arr8)

arr_results = [arr_result1, arr_result2, arr_result3, arr_result4]
for i in range(4):
    print(f"{arr_results[i]}\n")

# DETERMINANTIT JA TRANSPOOSIT

# Original matrix
matrix_A = np.matrix([[4, 9, 0],
                      [-3, 7, 11]])

# Transposed matrix
transposed_matrix_A = matrix_A.transpose()

print("Original Matrix:")
print(matrix_A)
print("\nTransposed Matrix:")
print(transposed_matrix_A)
# Original matrix
matrix_B = np.matrix([[8, 9],
                      [-3, 12],
                      [0, -1],
                      [7, 1]])

# Transposed matrix
transposed_matrix_B = matrix_B.transpose()

print("Original Matrix:")
print(matrix_B)
print("\nTransposed Matrix:")
print(f"{transposed_matrix_B}\n")


#2.1 tehtävä

a = np.array([[5, -6],
              [8, 10]])
det_a=np.linalg.det(a)
print(f"1a) {det_a}")

from sympy import *
x, y, z = symbols('x, y, z')

b= Matrix([[1-x, -x],
              [x, 1-x]])
det_b=b.det()
print(f"1b) {det_b}")

#Tehtävä2.2
A_2= Matrix([[2,3,4],
             [-2,-1,1],
             [5,3,2]])
det_A_2 = A_2.det()
print(f"2a) {det_A_2}")


B_2= Matrix([[3,15,7],
             [0,-4,0],
             [3,2,3]])
det_B_2 = B_2.det()
print(f"2a) {det_B_2}")


_3= Matrix([[-2,0,8,5],
             [3,-1,2,1],
             [4,7,6,2],
             [1,0,2,3]])
det_3 = _3.det()
print(f"3) {det_3}")


