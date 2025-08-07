import numpy as np


arr1= np. array([2,5,10,21]) # create a 2D array
arr2= np.array([[3,6,9], [12, 15, 18]]) # create another 2D array


# print(np.concatenate(([arr1,arr2]),axis=0))  # concatenate two arrays

# print(np.array_split(arr1,3))# split arr1 into 2 sub-arrays along the first axis
# print(np.split(arr1,2)) #it can cause error if the array cannot be split evenly 

# print (np.hstack((arr1, arr2))) # horizontally stack two arrays
# print (np.vstack((arr1, arr2))) # vertically stack two arrays


#print (np.transpose(arr2)) # transpose the array arr2 using np.transpose
print (arr2.T) # transpose the array arr2 using the T attribute

print (arr2.argmax()) # it tells  the index of the maximum value in arr2
print (arr2.argmin()) # it tells the index of the minimum value in arr2