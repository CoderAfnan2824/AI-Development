
data = {'Name': ['Afnan', 'Sam', 'Abhi', 'Srish'],
        'Age': [26, 23, 24, 25],
        'City': ['New York', 'New Angeles', 'Chicago', 'Houston']}

import pandas as pd

df = pd.DataFrame(data, index = ['Student1', 'Student2', 'Student3', 'Student4'])

print(df[df['Age'] > 24])

print(df[(df['Name'].str.startswith('A')) | (df['City'].str.contains('New'))]) #filters rows where Name starts with 'A' or City contains 'New'

