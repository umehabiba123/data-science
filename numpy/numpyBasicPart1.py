import numpy as np
import random
print(np.array([]))
print(np.array([1,2,3,4,5]))
print(np.array([[1,2,3,4,5],[1,2,3,4,5]]))
print("/n")
print(np.array([[[1,2,3,4,5],[1,2,3,4,5]],[[1,2,3,4,5],[1,2,3,4,5]]]))

 # we can  use both braces () and []
print(np.empty([]))
print(np.empty((2,3)))  #it return junk values

#using np.zeros( ) method
print(np.zeros(3,dtype=int))
print(np.zeros((3,5),dtype=int))
print(np.zeros((3,5,2),dtype=int))    #three dimensional array

#using np.ones( ) method
print(np.ones(3,dtype=int))
print(np.ones((3,5),dtype=int))
print(np.ones((3,5,2),dtype=int))    

#using np.ones( ) method                                                
print(np.full(6,4))
print(np.full((6,4),8))

#using np.eye( ) method
print(np.eye(2,2),0)
print(np.eye(3,3,-1,dtype=int))   

#using np.fromstring( ) method
print(np.fromstring('1 2 3 4',dtype=int,sep=" "))
print(np.fromstring('1,2', dtype=int, sep=','))


#using np.arange( ) method
print(np.arange(6))
print(np.arange(1,10))
print(np.arange(-1,10,2))

#using np.random( ) method
print(random.random())
print(np.random.rand(5))
print(np.random.rand(2,3))
print(np.random.rand())
print(np.random.rand(2,3,4))
print(random.randint(1,10))


#using np.linspace( ) method
print(np.linspace(1,9,dtype=int))    # by default 50 values will print
print(np.linspace(1,9,5,dtype=int)) 


arr1 = np.array([1,2,3,4,5])
print(arr1)
arr2 =np.array([[1,2,3,4,5],[1,2,3,4,5]])

print(np.zeros_like(arr1))
print(np.zeros_like(arr2))