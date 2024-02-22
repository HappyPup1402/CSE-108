import numpy as np
from numpy import linalg

A = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
B = np.array([[3, 1, 4],[2, 6, 1],[2, 9, 7]])

print("Part A:")
print("A+B")
#.add prints the addition of matricies A and B
print(np.add(A,B))
print('\n')

print("Part B:")
print("A*B")
#.dot prints the multiplication of matrix A * matrix B
print(np.dot(A,B))
print('\n')

print("Part C:")
print("Determinate of A")
#.det prints the determinate of matrix A
print(np.round(linalg.det(A)))
print('\n')

print("Part D:")
print("Inverse of B")
#.inv prints the inverse of matrix B
print(linalg.inv(B))
print('\n')

print("Part E:")
print("Eigen Values of A")
#.eigvals prints the eigen values of matrix A
print(linalg.eigvals(A))