#Task 2: Matrix Transformer
import numpy as np

matrix = np.random.randint(1,51, (5, 5))  # Create a 5x5 matrix with random integers from 1 to 50
print("Original Matrix:\n", matrix)
#1: Reshape it into a 1D array

reshape_arr= matrix.ravel()
print("Reshaped 1D array:", reshape_arr)

#2: Transpose the matrix
transpose= matrix.T
print("Transposed Matrix:\n", transpose)

#3: Replace all values > 50 with 0 using np.where()

replace_val= np.where(matrix > 50, 0, matrix) 
            
print("Matrix after replacing values > 50 with 0:\n", replace_val)

#4: Add a 5x5 identity matrix to it
identitiy_matrix = np.eye(5)
result_matrix = matrix + identitiy_matrix
print("Matrix after adding identity matrix:\n", result_matrix)
