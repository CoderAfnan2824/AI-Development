import numpy as np

ages = np.array([6,3,19,22,12,15,16,89,33,64,56,45,90,100])

#filtering
teenagers = ages[ages < 19]
print(teenagers)

adults = ages[ (ages >18) & (ages <65)]
print(adults)

even = ages[ ages % 2 == 0]
print(even)

#fill values based on filter
new_ages = np.where(ages > 18, ages, 0)
print(new_ages)