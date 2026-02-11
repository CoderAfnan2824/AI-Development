import numpy as np

arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])

#sum all elements
print(np.sum(arr))
print(np.mean(arr))
print(np.std(arr))
print(np.var(arr))
print(np.min(arr))
print(np.max(arr))
print(np.argmax(arr))
print(np.argmin(arr))

#sum all columns
print(np.sum(arr, axis=0))