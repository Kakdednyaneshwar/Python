# joining of array

import numpy as np

arr = np.array([[11,12,13],[14,15,16]])
rra = np.array([[17,18,19],[20,21,22]])

print(type(arr))
print(type(rra))  
print("\n***********************************************")
r = np.concatenate((arr,rra)) # concatenate without axix
print("\nconcatenate without axis\n",r)

x = np.concatenate((arr,rra),axis=1) 
print("\nconcatenate with axis=1\n",x)