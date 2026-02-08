data = {'Name': ['Afnan', 'Sam', 'Abhi', 'Srish'],
        'Age': [26, 23, 24, 24],
        'Marks': [85, 92, 78, 95]}

import pandas as pd
df = pd.DataFrame(data, index = ['Student1', 'Student2', 'Student3', 'Student4'])

print(df.mean(numeric_only=True)) #calculates the mean of numeric columns (Age and Marks

print(df.sum(numeric_only=True)) #calculates the sum of numeric columns (Age and Marks)

print(df.min(numeric_only=True)) #calculates the minimum value of numeric columns (Age and Marks
print(df.max(numeric_only=True)) #calculates the maximum value of numeric columns (Age and Marks

print(df.count()) #counts the number of rows in each column (non-null values)

#For single columns
print(df['Age'].mean()) #calculates the mean of the 'Age' column 
#Same above functions can be applied to single columns as well.  


#Group Data by a specific column and calculate the mean of another column for each group
group = df.groupby('Age')
print(group['Marks'].mean()) #calculates the mean of 'Marks' for each unique value in 'Age' column
print(group['Marks'].sum())
 
