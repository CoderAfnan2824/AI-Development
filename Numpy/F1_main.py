
# Numpy Array is similar to Java Array
# It is fixed in size and contains same type elements

import numpy as np

a = np.array([0,2,4,6])

print(type(a))  # return numpy.ndarray
print(a.dtype)  # return int64 which is type of the data stored

print(a.size)   # return size of array
print(a.ndim)   #return no of dimentions
print(a.shape)  # return tuple of intgers indicating the size in each dimention

a[1] = 100
print(a)    # a[1] modified to 100

# slicing is applied here
e = a[1:2]
print(e)

#Broadcasting values: setting value from index 1 to index 2
a[1:3] = 300,500    
print(a)

#Broadcasting: applying any math operation to vector reflects in all elements
e = a+ 1
print(f"broadcasting: {e}")

#Numpy vector addition
u = np.array([1,0])
v = np.array([0,1])
z = u + v
print(z)

#Vector multiplication

x = 2*v
print(x)

a = np.array([1,2])
b = np.array([3,4])
c = a*b
print(c)

#Dot product for a and b:
# 1*3 + 2*4 = 11
d = np.dot(a,b)
print(d)

#Functions in Numpy
mean_a = a.mean()
print(mean_a)

print(np.pi)
print(np.max)

t = np.array([0,np.pi/2,np.pi])
s = np.sin(t)
print(s)

#Plotting in numpy
p1 = np.linspace(-2,2,num=5) # plot from -2 to 2 (-2,-1,0,1,2)
p2 = np.linspace(-2,2,num=9) # plot from -2 to 2 (-2,-1.5,-1,-0.5,,0,0.5,1,1.5,2)

print(p2)