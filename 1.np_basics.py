import numpy as np

arr = np.array([[1, 2, 3] ,[4, 5, 6], [7, 8, 9]]) 

print (np.shape(arr)) #number of rows and columns
print (np.ndim(arr)) #number of dimensions  
print (np.size(arr)) #total number of elements
print(np.ndim(arr))# number of dimensions
print (np.size (arr)) # total number of elements
print (arr.dtype) # data type of the array
print (arr.nbytes) # total bytes consumed by the elements of the array
print (arr.itemsize) # size in bytes of each element of the array

print(len(arr)) # number of rows
print(len(arr[0])) # number of columns


print (arr.astype(str)) # convert the array to string type

print ("-----------------------------------------------------")


arr1 = np.array([[1, 2, 3] , [10, 20, 30]]) # create a 2D array
arr2 =  np.array([[4, 5, 6], [40, 50, 60]]) # create another 2D array
print (arr1+ arr2)# element-wise addition
print (np.add(arr1, arr2)) # element-wise addition using np.add


print (arr1 - arr2) # element-wise subtraction  
print (arr1 * arr2) # element-wise multiplication
print (arr1 / arr2) # element-wise division

print ("-----------------------------------------------------")


arr1= np.array([[1, 2, 3, 4, 5]]) # create a 1D array
arr1[0,1]=45 
print(arr1) # modified array after changing an element
print (np.zeros((2, 3))) # create a 2D array of zeros with shape (2, 3)

print (np.ones((2, 3))) # create a 2D array of ones with shape (2, 3)

print (np.full((2, 3), 7)) # create a 2D array filled with the value 7

print (np.eye(3)) # create a 2D identity matrix of size 3x3
print ()
print (np.arange(15))

print (np.arange(1, 10, 2)) # create a 1D array with values from 1 to 10 with a step of 2

print(np.linspace(1, 9, 5)) # create a 1D array with 5 evenly spaced values between 1 and 10

print(np.empty((2, 3))) # create an empty 2D array with shape (2, 3)

a1= (np.arange( 60)) 
print(a1) # create a 1D array with values from 0 to 59
print(np.reshape(a1, (3, 20))) # reshape the array to have 3 rows and 20 columns
print (np.ravel(a1)) # convert 2D  the array to a 1D array