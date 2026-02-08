

import pandas as pd
from pathlib import Path 

base = Path(__file__).resolve().parent

my_path = base / "myFile.csv"
my_excel = base / "my_excel.xlsx"

my_data = {"Name":["Afnan",'Krish','Adnan'],
           "Age": [26,25,26],
           "Job":['mainframe',"support",'civil']}

#below method reads whole csv data
data = pd.read_csv(my_path)

#head contains quick 5 initial rows of the file
print(data.head())

#below method reads whole excel data
#df = pd.read_excel(my_excel)


#below method read my own dataframe
df = pd.DataFrame(my_data)
print(df)

#Create new data table from existing dataFrame
#It create table with two columns: Name, Job
yt = df[["Name","Job"]]
print(yt)

#Accessing specific value from table
print(df.iloc[0,0])
print(df.loc[1,"Job"])

#Below 3 lines modified row index from 1,2,3 to a,b,c
df_new = df
df_new.index = ["a",'b','c']
print(df.loc['a',"Job"])


#Slice dataFrames: It displays code from row a to b with column JOB
df_slice = df.loc['a':'b',"Job"]
print(df_slice)

#Obtain unique: List down only unique rows in age column
print(df["Age"].unique())

#Filter on the dataframe
df1 = df[df["Age"]>25]
print(df1)