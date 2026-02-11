'''
Numpy: It's a replacement for python list. It's written in C programming

Numpy arrays are 10x faster than python list

eg: 
[1,2,3] * 2 = [1,2,3,1,2,3]
np.array([1,2,3])*2 = [2,4,6]

'''
import numpy as np

ls = [1,2,3]

print(ls*2) #[1,2,3,1,2,3]

num_array = np.array([1,2,3])
print(num_array*2) #[2,4,6]


