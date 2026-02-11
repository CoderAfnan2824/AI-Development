import numpy as np

array = np.array([[1,2,3,4],
                 [5,6,7,8],
                 [9,10,11,12],
                 [13,14,15,16]])

print(array[0,0]) #1

print(array[0:2,1]) #[2,6]

print(array[::2,:3]) #[[1,2,3],[9,10,11]]