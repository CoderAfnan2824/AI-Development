
import pandas as pd
from pathlib import Path    
import json
import xml.etree.ElementTree as ET

base = Path(__file__).resolve().parent

csv_path = base / "myFile.csv"
json_path = base / "file.json"
xml_path = base / "file.xml"

#Reading csv file
#By default, pandas considers the first row of the csv file as header. To avoid this, we can set header=None
csv_data = pd.read_csv(csv_path, header=None)

df = pd.DataFrame(csv_data)
#print(df)

df.columns = ["Name","ID","Branch"]
print(df)


#Reading json file
with open(json_path, "r") as f:
    json_data = json.load(f)
    df1 = pd.DataFrame(json_data)
    print(df1)

#reading XML file
tree = ET.parse(xml_path)   #Parse will read the XML file and create a tree structure in memory
root = tree.getroot()   #getroot will return the root element of the XML tree

columns = []
