import numpy as np
import statistics as stats
arr= np.array([1, 2, 3,10,58])

print (np.mean(arr))
print (np.cumsum(arr))

arr2 = np.array([1, 2, 3, 4, 5])
arr3 = np.array([6, 7, 8, 9, 10])



a= [7,10, 20, 30, 40, 50,58,70,70]
arr= np.array(a)
print(stats.mode(arr)) 
print(np.std(arr))  


price= np.array(arr2)
quantity= np.array(arr3)

print(np.dot(price, quantity))

c =(np.cumprod([price, quantity], axis=0)) 
print(c)
print("Sum of second row:", c[1].sum())  # This will print the sum of the second row of the cumulative product

