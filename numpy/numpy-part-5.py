# ************************************BroadCasting in Numpy arrays*********************************************
#                                         Indexing in 1-D Array
import numpy as np
import random
array1 = np.array([1,2,3,4,5,6])
print(id(array1))
print("Addition of Scalar",array1+2)
print("Subtraction of Scalar",array1-2)
print("Multiplication of Scalar",array1*2)
print("Divison of Scalar",array1/2)
print("Modulas of Scalar",array1%2)



#           Scalar math in 2-Dimensional array
array2 = np.random.randint(1,10,[2,2])
print("Addition of Scalar Matrix ",array2+2)
print("Subtraction of Scalar Matrix ",array2-2)
print("Multiplication of Scalar Matrix ",array2*2)
print("Divison of Scalar Matrix ",array2/2)
print("Modulas of Scalar Matrix ",array2%2)

#            Multiplication of  1-D array and 2-D array

print("Multiplication of  2-D array with 1-D array",array2*np.array([4,5]))


#            Multiplication of  2-D arrays

array3 = [[3],[4]]
print("Multiplication of  2-D arrays ",array2*array3)

# ***********************************Reshaping in Numpy arrays*********************************************
#                                         Reshaping in 1-D Array

array1 = np.arange(24)


array1.shape=(6,4)
print("Shaping 1-D array to 2-D array ",array1)
#                                         shaping in 1-D Array into 2-D array
array1.shape=(2,3,4)
print("Shaping 1-D array to 3-D array ",array1)


print("Reshaping 1-D array to 3-D array ",np.reshape(array1,(-1)))
print("Reshaping 1-D array to 2-D array ",np.reshape(array1,(6,4)))
print("Reshaping 1-D array to 3-D array ",np.reshape(array1,(2,3,4)))


#                                         Resizing 
print("Resizing the arrays according to number of rows and column \n",np.resize(array1,(4,4)))
print("Resizing the arrays according to number of rows and column \n",np.resize(array1,(2,4,4)))


# ***********************************Transpose in Numpy arrays*********************************************
#                                         Transpose in 1-D Array is not possible

#                                         Transpose in 1-D Array is not possible
array_tra = np.random.randint(1,10,(4,2))
print("Tranpose of Matrix ",np.transpose(array_tra))
print("Tranpose of Matrix ",np.transpose(array_tra))

# ***********************************Swapaxis in Numpy arrays*********************************************
#                                         Transpose in 1-D Array is not possible

print(np.swapaxes)

# ***********************************Flatten in Numpy arrays*********************************************
#                    2-D array
flatten_array = array1.flatten("C") 
print("Flaten arrray ",flatten_array)
print("Flaten arrray ",array1.flatten("F"))
print("Flaten arrray ",array1.flatten("A"))
print("Flaten arrray ",array1.flatten("K"))


# ***********************************Sorting in Numpy arrays*********************************************
# 
arry = np.random.randint(1,10,(4,4))

print("Sorted array without axis \n",np.sort(arry))
print("Sorted array with axis 0 \n",np.sort(arry,0))
print("Sorted array with axis 1 \n",np.sort(arry,1))

# ***********************************Iteratting in Numpy arrays*********************************************
#                                          1-D Array

array1  = np.random.randint(1,10,6)
for i in array1:
    print(i,end=" ")

for i in arry:
    print("\n Iteration ")  # it will print row wise
    print(i)
array3 = arry = np.random.randint(1,10,(2,4,4))
for i in arry:
    print("\n Level ")  # it will print Level wise
    print(i)

    