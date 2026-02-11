import numpy as np

rng = np.random.default_rng()
print(rng)

print(rng.integers(low=1, high=2)) #return any number from 1 to 9
print(rng.integers(low=1, high=15, size = 3)) #return list of 3 elements from 1 to 14
print(rng.integers(low=1, high=15, size = (3,2))) #return list of elemments with 3 rows and 2 columns
      

rng1 = np.random.default_rng(seed=1)
#every time you run the program, the random generator has same start point
print(rng1.integers(low=1, high=15, size = (3,2))) #return list of elemments with 3 rows and 2 columns

#The program generates same random sequence for every run if seed specified

#Generate float point number between range
np.random.seed(seed=1) #produces same uniform floating values)
print(np.random.uniform(low=-1, high=-1,size=3))

#shuffle array
arr = np.array([1,3,5,7,8])
rng.shuffle(arr)
print(arr)

#Choose from array
my_num = rng.choice(arr)
my_num = rng.choice(arr, size=(2,3))
print(my_num)