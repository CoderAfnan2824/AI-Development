import numpy as np

array = np.array([2,4,7])

#Scalar arithmetic
print(array + 1) #[3,5,8]
print(array - 1) #[1,3,6]
print(array * 2) #[4,8,14]
print(array / 2) #[1,4,3.5]
print(array ** 2) #[4,16,49]

#Vector calculations

array = np.array([1.01,2.9,4])

print("-------------------")
print(np.sqrt(array))
print(np.round(array))
print(np.ceil(array))
print(np.floor(array))
print(np.pi)

#Radius of the list
radii = np.array([2,4,6])

print(np.pi * radii ** 2)

arr1 = np.array([5,7,9])
arr2 = np.array([2,4,6])

#Vector arithmetic operations
print(arr1 + arr2)
print(arr1 ** arr2)
print(arr1 - arr2)
print(arr1 * arr2)
print(arr1 / arr2)

#
scores = np.array([50,60,90,100,40])
print(scores > 70) #return array of boolean values for elements greater than 70 
#[False False True True Fales]
print(scores[scores > 70]) #Return array of values that are greater than 70 [90 100]

scores[scores > 70] = 0 #setting other values to zero
#[0 0 90 100 0]