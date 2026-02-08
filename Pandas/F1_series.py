'''
Series: is a one-dimensional labeled array capable of holding any data type (integers, strings, floating point numbers, Python objects, etc.).
The axis labels are collectively referred to as the index. A Series is like a column in a spreadsheet or a SQL table. It can also be seen as a dictionary-like container for data.
'''

import pandas as pd

# print the version of pandas
print(pd.__version__)

data = [1, 2, 3, 4, 5]

series = pd.Series(data)
print(series)

#Series with custom index
series1 = pd.Series(data, index = ['a','b','c','d','e'])
print(series1)

# using loc and iloc
print(series1.loc['c'])
print(series1.iloc[3])

print(series1[series1 > 3])