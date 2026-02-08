
import requests
import json
import pandas as pd

data = requests.get("https://web.archive.org/web/20240929211114/https://fruityvice.com/api/fruit/all")

#extracting json data from the response
results = json.loads(data.text)

#pd.DataFrame(results)

#json normalization - to convert nested json data to flat table of pandas DataFrame
df1 = pd.json_normalize(results)
print(df1)

#retrieving specific data from the DataFrame
cherry = df1.loc[df1["name"] == "Cherry"]
print(cherry.iloc[0]['family']," ",cherry.iloc[0]["nutritions.carbohydrates"])