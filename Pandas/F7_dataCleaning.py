'''
Data Cleaning: It's the process of identifying and removing data which
is incorrect, incomplete, irrelevant, duplicated, or improperly formatted from a dataset.

more than 75% of usage of Pandas is for data cleaning and manipulation.

'''
import pandas as pd

data = [
    {"Pokemon": "Pikachu", "Type": "Electric", "HP": 35, "Attack": 55, "Legendary": False, "Region": "Kanto", "Capture_Date": "2024-01-12", "Trainer_Notes": "Strong starter"},
    {"Pokemon": "Pikachu", "Type": "Electric", "HP": 35, "Attack": 55, "Legendary": False, "Region": "Kanto", "Capture_Date": "2024-01-12", "Trainer_Notes": "Strong starter"},
    
    {"Pokemon": "Charizard", "Type": "Fire/Flying", "HP": 78, "Attack": 84, "Legendary": False, "Region": "Kanto", "Capture_Date": "2024-02-10", "Trainer_Notes": None},
    
    {"Pokemon": "Bulbasaur", "Type": "Grass/Poison", "HP": 45, "Attack": 49, "Legendary": False, "Region": "Kanto", "Capture_Date": "2024-02-15", "Trainer_Notes": "Good for beginners"},
    
    {"Pokemon": "Mewtwo", "Type": "Psychic", "HP": 106, "Attack": 110, "Legendary": True, "Region": "Kanto", "Capture_Date": "2024-03-01", "Trainer_Notes": "Legendary capture"},
    
    # Missing Attack
    {"Pokemon": "Squirtle", "Type": "Water", "HP": 44, "Attack": None, "Legendary": False, "Region": "Kanto", "Capture_Date": "2024-02-20", "Trainer_Notes": "Missing attack value"},
    
    # Incorrect Attack (string instead of number)
    {"Pokemon": "Eevee", "Type": "Normal", "HP": 55, "Attack": "abc", "Legendary": False, "Region": "Kanto", "Capture_Date": "2024-02-25", "Trainer_Notes": "Attack incorrect"},
    
    # Incorrect negative HP
    {"Pokemon": "Gengar", "Type": "Ghost/Poison", "HP": -60, "Attack": None, "Legendary": False, "Region": "Unknown", "Capture_Date": "2024-02-28", "Trainer_Notes": "Negative HP error"},
    
    # Inconsistent boolean + date format
    {"Pokemon": "Dragonite", "Type": "Dragon/Flying", "HP": 91, "Attack": 134, "Legendary": "TRUE", "Region": "Kanto", "Capture_Date": "03-05-2024", "Trainer_Notes": "Date format inconsistent"},
    
    # Duplicate entry
    {"Pokemon": "Pikachu", "Type": "Electric", "HP": 35, "Attack": None, "Legendary": False, "Region": "Kanto", "Capture_Date": "2024-01-12", "Trainer_Notes": "Duplicate entry"},
    
    # Missing date + inconsistent boolean
    {"Pokemon": "Snorlax", "Type": "Normal", "HP": 160, "Attack": 110, "Legendary": "No", "Region": "Kanto", "Capture_Date": None, "Trainer_Notes": "Missing capture date"},
    
    # Corrupted / irrelevant row
    {"Pokemon": "MissingNo", "Type": "Glitch", "HP": None, "Attack": 999, "Legendary": "Maybe", "Region": "Kanto", "Capture_Date": "2024-13-40", "Trainer_Notes": "Corrupted entry"},
    
    # Lowercase boolean + different date format
    {"Pokemon": "Charmander", "Type": "Fire", "HP": 39, "Attack": 52, "Legendary": "false", "Region": "Kanto", "Capture_Date": "2024/02/05", "Trainer_Notes": "Lowercase boolean"}
]

import pandas as pd

df = pd.DataFrame(data)

#Key details of the dataset:
print()
print("Dataset Overview:")

exit()
print(df.head()) #prints the first 5 rows of the dataset
print(df.info()) #prints summary of the dataset including data types and non-null counts
print(df.describe()) #prints statistical summary of numeric columns
print(df.isnull().sum()) #prints the count of null values in each column

#1. Drop not needed columns
df = df.drop(columns = ['Trainer_Notes'])
# other way: df.drop(['Trainer_Notes'], axis=1, inplace=True) 
# #inplace=True modifies the original dataframe without needing to assign it back to df
#axis=1 means we want to drop a column, axis=0 would mean we want to drop a row
print(df.to_string())

#2. Drop Not applicable rows
df = df.dropna(subset=['HP','Capture_Date']) #drops rows where 'HP' or 'Capture_Date' is NaN
print(df.to_string())

#3. It fills None values in 'Attack' column with 0
df['Region'] = df.fillna({'Region':'Unknown'}) #fills NaN values in 'Region' column with 'Unknown'
df['Attack'] = df.fillna({'Attack':df['Attack'].mean()}) #fills NaN values in 'Attack' column with mean of the column
print(df.to_string())

#4. Fix inconsistent values
df['Type'] = df['Type'].replace({'Electric':'ELECTRIC'}) #replaces 'Electric' with 'ELECTRIC' in 'Type' column
print(df.to_string())

#5. Standardize text data
df['Pokemon'] = df['Pokemon'].str.lower() #converts 'Pokemon' column to lowercase
print(df.to_string())

#6. Remove duplicates
df = df.drop_duplicates() #drops duplicate rows
#df = df.drop_duplicates(subset=['Pokemon']) 
# #drops duplicate rows based on 'Pokemon' column
print(df.to_string())

#7. Standardize column names by stripping whitespace and converting to lowercase
df.columns = df.columns.str.strip().str.lower()
print(df.to_string())

#8. Fix Data types
df['Attack'] = pd.to_numeric(df['Attack'], errors='coerce')
# #converts 'Attack' column to numeric, setting invalid parsing to NaN
#errors='coerce' will replace non-numeric values with NaN, which can then be handled with fillna() or dropna() as needed
df['Attack'] = df['Attack']