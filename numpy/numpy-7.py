import numpy as np

# ************************************Concatenating in Numpy arrays*********************************************
#                                         Concatenating in 1-D Array
array1 = np.arange(5)
array2 = np.arange(5,10)
concatenate_array=np.concatenate((array1,array2))
print(concatenate_array)
#                                         Concatenating in 2-D Array
array3= np.random.randint(1,8,[3,3])
array4= np.random.randint(1,10,[3,3])
concatenate_array=np.concatenate((array3,array4))
print(concatenate_array)
concatenate_array_axis0=np.concatenate((array3,array4),axis=0)
print("Concatenate arrays at 0 axis \n",concatenate_array_axis0)
concatenate_array_axis1=np.concatenate((array3,array4),axis=1)
print("Concatenate arrays at 1 axis \n",concatenate_array_axis1)

# ************************************STacking in Numpy arrays*********************************************
#                                         STacking in 1-D Array
print("Staking in arrays \n",np.stack((array1,array2)))
print("Staking in arrays by 0 index \n",np.stack((array1,array2),axis=0))
print("Staking in arrays 1 index \n",np.stack((array1,array2),axis=1))
print("Staking in arrays vertically \n",np.vstack((array1,array2)))
print("Staking in arrays horizantly \n",np.hstack((array1,array2)))
print("Staking in arrays horizantly \n",np.column_stack((array1,array2)))
print("Staking in arrays horizantly \n",np.row_stack((array1,array2)))
#                                         STacking in 2-D Array

print("Staking in 2-D array \n",np.stack((array3,array4)))
print("Staking in  2-D arrays vertically \n",np.vstack((array3,array4)))
print("Staking in  2-D arrays horizantly \n",np.hstack((array3,array4)))
print("Staking in  2-D arrays horizantly \n",np.column_stack((array3,array4)))
print("Staking in  2-D arrays horizantly \n",np.row_stack((array3,array4)))

# ************************************Spliting in Numpy arrays*********************************************
#                                         Spliting in 1-D Array

print(np.split(array1,3))