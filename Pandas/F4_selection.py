
data = [
    {"Team": "Mumbai Indians", "City": "Mumbai", "Titles_Won": 5, "Captain": "Hardik Pandya"},
    {"Team": "Chennai Super Kings", "City": "Chennai", "Titles_Won": 5, "Captain": "MS Dhoni"},
    {"Team": "Kolkata Knight Riders", "City": "Kolkata", "Titles_Won": 2, "Captain": "Shreyas Iyer"},
    {"Team": "Royal Challengers Bangalore", "City": "Bengaluru", "Titles_Won": 0, "Captain": "Faf du Plessis"}
]

import pandas as pd

df = pd.DataFrame(data)

#Selecting a specific column
print(df['Team'])

#Selecting multiple columns
print(df[['Team','Captain']])


#Selecting a single row by index
print(df.iloc[1])

#Selecting multiple rows by index
print(df.iloc[1:3]) #selects rows from index 1 to 2 (3 is exclusive)

#Selecting rows and columns together
print(df.loc[1:3,['Team','Captain']])

print(df.iloc[0:4:2,0:3])

print(df.loc[:,'Team'])

try:
    print(df.iloc[9])
except IndexError as e:
    print("Error: ", e)
