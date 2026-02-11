import numpy as np
import pandas as pd

array = np.array([[['A','B','C'],['D','E','F'],['G','H','I']],
                 [['J','K','L'],['M','N','O'],['P','Q','R']],
                 [['S','T','U'],['V','W','X'],['Y','Z',' ']]])

#Return number of dimensions
print(array.ndim) #3

#Return (3,3,3) 3 layers, 3 rows, 3 columns
print(array.shape)

#Chain indexing
print(array[0][1][2]) #F

#multiDimen indexing
print(array[0,1,2]) #F

df = pd.DataFrame(array[1])
print(df)

