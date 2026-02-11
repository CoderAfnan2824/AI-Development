'''

Dataframe: It's a 2D data structure witj rows and columns.
It's similar to a excel spreasheet.

'''

import pandas as pd

data = {'Name': ['Afnan', 'Sam', 'Abhi', 'Krish'],
        'Age': [26, 23, 24, 25],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']}

df = pd.DataFrame(data, index = ['Student1', 'Student2', 'Student3', 'Student4'])
print(df)

#Selecting a row by index
print(df.iloc[1])  #selects the second row (index starts from 0)

#Selecting a row by name
print(df.loc['Student3'])  #selects the row with index 'Student3'

#Selecting a column
print(df['Name'])  #selects the 'Name' column

#Adding a new column
print( " ")
df['Grade'] = ['A','B','C','D']
print(df)

#Adding a new row. 
#Note: Each Dictionary in the list represents a row, and the keys of the dictionary correspond to the column names in the DataFrame.
new_df = pd.DataFrame([{'Name': 'Rahul', 'Age': 22, 'City': 'Miami', 'Grade': 'B'}, 
                       {'Name': 'Priya', 'Age': 24, 'City': 'Boston', 'Grade': 'A'}], 
                      index = ['Student5','Student6'])
df = pd.concat([df,new_df])
print(df)


#Filtering rows based on a condition
df_filtered = df[df['Age'] > 24]
print(df_filtered)

#Extracting a specific column and rows
print(df.loc['Student2':'Student4', ['Name', 'City']])

#Removing a column
#axis=1 means we want to drop a column, axis=0 would mean we want to drop a row
df = df.drop('Grade', axis=1)
print(df)

#Removing a row
df = df.drop('Student5', axis=0)
print(df)