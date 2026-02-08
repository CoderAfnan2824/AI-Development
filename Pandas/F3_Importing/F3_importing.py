import pandas as pd

from pathlib import Path 
file_path = Path(__file__).resolve().parent

#Reading a CSV file
data = pd.read_csv(file_path / 'file.csv')
#print(data) - > prints starting and ending 5 rows of the data
print(data.to_string()) #prints the entire data without truncation


#Reading an JSOn file
data_json = pd.read_json(file_path / 'cricket.json')
print("JSON Data: ")
print()
print(data_json.to_string()
