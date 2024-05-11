import numpy as np


#                *********************Scalar Math************************

#           Scalar math in 1-Dimensional array
array1 = np.array([1,2,3,4,5,6])
print(id(array1))
print("Addition of Scalar",array1+2)
print("Subtraction of Scalar",array1-2)
print("Multiplication of Scalar",array1*2)
print("Divison of Scalar",array1/2)
print("Modulas of Scalar",array1%2)

#           Scalar math in 2-Dimensional array
array1 = np.random.randint(1,10,[2,2])
print("Addition of Scalar Matrix ",array1+2)
print("Subtraction of Scalar Matrix ",array1-2)
print("Multiplication of Scalar Matrix ",array1*2)
print("Divison of Scalar Matrix ",array1/2)
print("Modulas of Scalar Matrix ",array1%2)

#                *********************Arthimatic Operations************************

#           Arithmetic Operation in 1-Dimensional array 
array1 = np.array([1,2,3,4,5,6])
array2 = np.array([1,2,3,4,5,6])
print("Addition of Arthmetic values ",array1+array2)
print("Subtraction of Arthmetic values ",array1-array2)
print("Multiplication of Arthmetic values ",array1*array2)
print("Divison of Scalar Arthmetic values ",array1/array2)
print("Modulas of Scalar",array1%array2)

#           Arithmetic Operation in 2-Dimensional array 
array1 = np.random.randint(1,10,[2,2])
array2 = np.random.randint(1,10,[2,2])
print("Addition of Arthmetic values ",array1+array2)
print("Subtraction of Arthmetic values ",array1-array2)
print("Multiplication of Arthmetic values ",array1*array2)
print("Divison of Scalar Arthmetic values ",array1/array2)
print("Modulas of Scalar",array1%array2)



#                *********************More Mathematical Operations***********************
#                                        1-Dimensional array 
array1 = np.array([1,2,3,4,5,6])
print(np.abs(array1))
print(np.sqrt(array1))
print(np.square(array1))
print(np.cbrt(array1))
print(np.log(array1))
print(np.log10(array1))
print(np.ceil(array1))
print(np.floor(array1))
print(np.cumsum(array1))   # each number add all privious values

#                                        2-Dimensional array 
array1 = np.random.randint(1,10,[2,2])
print(np.abs(array1))
print(np.sqrt(array1))
print(np.square(array1))
print(np.cbrt(array1))
print(np.log(array1))
print(np.log10(array1))
print(np.ceil(array1))
print(np.floor(array1))
print(np.cumsum(array1))



#                *********************Aggregate Functions***********************
#                                        1-Dimensional array 
array1 = np.array([1,2,3,7,4,5])
print(np.sum(array1))
print(np.mean(array1))
print(np.median(array1))
print(np.average(array1))
print(np.percentile(array1,100))  
print(np.var(array1))


#                                        2-Dimensional array 
array1 = np.random.randint(1,10,[2,2])

print(array1)
print(np.sum(array1,axis=0))   # axis=0 mean add rows 
print(np.mean(array1,axis=0))
print(np.median(array1,axis=0))
print(np.average(array1,axis=0))
print(np.percentile(array1,100))  
print(np.var(array1,axis=0))


#                *********************Comparing numpy arrays***********************
#                                        1-Dimensional array 
array1 = np.array([1,2,3,4,5,6])
array2 = np.array([1,2,3,4,5,6])
print(f"{array1} and {array2} are equal?? ",array1==array2)
print(f"{array1} and {array2} are not equal?? ",array1!=array2)
print(f"{array1} and {array2} are grater or equal?? ",array1>=array2)
print(f"{array1} and {array2} are less or equal?? ",array1<=array2)
print(f"{array1} and {array2} are grater ?? ",array1>array2)
print(f"{array1} and {array2} are less ?? ",array1<array2)

#                                        2-Dimensional array 
array1 = np.random.randint(1,10,[2,2])
array2 = np.random.randint(1,10,[2,2])
print(f"{array1} and {array2} are equal?? ",array1==array2)
print(f"{array1} and {array2} are not equal?? ",array1!=array2)
print(f"{array1} and {array2} are grater or equal?? ",array1>=array2)
print(f"{array1} and {array2} are less or equal?? ",array1<=array2)
print(f"{array1} and {array2} are grater ?? ",array1>array2)
print(f"{array1} and {array2} are less ?? ",array1<array2)


#                *********************Searching numpy arrays***********************
#                                        1-Dimensional array 
array1 = np.array([1,2,3,4,5,6])
print(np.shape(array1))
print(np.where(array1==5))
print(np.where(array1%2==0,True,False))
print(np.where(array1<4))

