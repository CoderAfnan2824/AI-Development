
import numpy as np

#2d list is given as input to array for numpy
arr = [[1,2,3],[11,22,32],[55,66,77]]

a = np.array(arr)

print(a)

print(a.size)   #returns number of elements in entire 2d array which is 9
print(a.ndim)   #returns number of dimensions i.e., number of nested lists which is 2
print(a.shape)  #returns 2 values: first: number of rows, second: number of columns


print(a[1:3,1])