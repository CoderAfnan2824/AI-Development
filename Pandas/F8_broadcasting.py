'''
Broadcasting: Broadcasting in pandas allows arithmetic operations between objects of different shapes by automatically expanding the smaller object while aligning indexes and columns.

'''

import pandas as pd
data = {'Name': ['Afnan', 'Sam', 'Abhi', 'Srish'],
        'Age': [26, 23, 24, 24],
        'Marks': [85, 92, 78, 95]}

data2 = {'Bonus': [5, 15, 20]}

df1 = pd.DataFrame(data, index = ['Student1', 'Student2', 'Student3', 'Student4'])
df2 = pd.DataFrame(data2, index = ['Student1', 'Student3', 'Student4'])

#Broadcasting addition of 'Bonus' column to 'Marks' column
df1['Total_Marks'] = df1['Marks'] + df2['Bonus']
print(df1)

#For row 2, we have null value in Bonus column
