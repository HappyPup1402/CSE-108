import numpy as np
print("Part A:")
#creates a 4 by 2 matrix with number ranging from 2 to 10
arrA = np.random.randint(low = 2, high = 11, size = (4,2))
print(arrA)
print('\n')

 
print("Part B:")
#creates a 8 by 8 matrix with all zeroes
arrB = np.zeros((8,8), dtype = int)
#creates the checkered pattern in the matrix 
arrB[::2,1::2] = 1
arrB[1::2,::2] = 1
print(arrB)
print('\n')

print("Part C")
arrC = [10, 20, 10, 30, 20, 40, 20, 20, 10, 30, 0, 50, 10]
#.unique prints the unique values of matric arrC
print(np.unique(arrC))
print('\n')

print("Part D")
arrD = np.array([6, 75, 9, 82, 36, 42, 59, 3, 52, 1, 32, 68, 93, 4, 27, 85, 0, -3, 57])
#prints all the values greater than 37 in matrix arrD
print(arrD[arrD > 37])
print('\n')

print("Part E")
arrE = np.array([0, 12, 45.21 ,34, 99.91])
#convert all elements to fahrenheit
arrE = arrE*(9/5) + 32
print(np.round(arrE,2))