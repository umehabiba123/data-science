# ************************************Indexing in Numpy arrays*********************************************
#                                         Indexing in 1-D Array
import numpy as np
import random
array1 = np.arange(7)
print("Original array ",array1)
print(array1[2])
print(array1[0])
print(array1[-2])       #negtive indexing start from Right side or in last

#                                         Indexing in 2-D Array
array2= np.random.randint(1,8,[3,3])
print(array2)


print(array2[2][0])
print(array2[-1][1])
print(array2[1][-1])

array3= np.random.randint(1,10,[3,4,4])
print(array3)


print(array3[1][0][1])
print(array3[-1][1][0])
print(array3[0][2][1])


# ************************************Slicing in Numpy arrays*********************************************
#                                         Slicing in 1-D Array

print(array1[2:4])
print(array1[-1:])
print(array1[:])
print(array1[:4])
print(array1[2:])

#                                         Slicing in 2-D Array
print("Slicing in Matrix",array2[:,:])
print(array2[1:2,:])
print(array2[-1:,0:1])
print(array2[1:2,0:2])
print(array2[-1:,0:2])

#                                         Slicing in 3-D Array
print("Slicing in 3-D array",array3[:,:])
print("All Levels ",array3[0:,1:2,:])
print("Level 1 to 2 ",array3[1:2,-1:,0:1])
print("Level 0 to 2 ",array3[0:2,1:,0:2])
print("Level 1 to all ",array3[1:,-1:,0:3])


# ************************************Boolean/Fancy arrays Indexing*********************************************
#                                         1-D Array          
print(array1[array1%2==0])
print(array1[array1>2])

#                                         2-D Array   
print("Matrix",array2)       
print(array2[array2%2==0])
print(array2[array2>2])
