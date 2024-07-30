import numpy as np
import sys
import time
array1 = [1,2,3,4,5]
size = sys.getsizeof(array1)
print(size)

array2 = np.array([1,2,3,4,5])
size2 = array2.itemsize
print(size2)


size= 100
array1 = np.arange(size)
array2 = np.arange(size)
initialTime = time.time()
array3 = array1*array2
print(array3)
finalTime = time.time()
print(f"Numpy list exction time is {finalTime-initialTime} seconds")

list1 =list(range(size))
list2 =list(range(size))
initialTime = time.time()
for i in range(len(list1)):
    list3 = list1[i]*list2[i]
    print(list3)
finalTime = time.time()
totaltime = finalTime-initialTime
print(f"Python list exction time is {finalTime-initialTime} seconds")



