import numpy as np

arr1 = np.array([[1],[2],[3],[4]])
arr2 = np.array([1,2,3,4])

print(arr1.shape)    #(4,1)
print(arr2.shape)    #(1,4)

print(arr1 * arr2)

'''
Here Broadcasting; it's the automatic expanding of array to perform operating

Possible only if:
1. Either of right most dimension is 1
2. or if rightmost dimensions are same

examples:
4,1 vs 4 allowed
1,4 vs 4,1 allowed

2,3 vs 1,3 allowed
2,3 vs 4,3 not allowed

5,1,3 vs 3 allowed
5,2,3 vs 4,5 not allowed (1,4,5)
'''
