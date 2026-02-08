
import pandas as pd
import requests

URL = 'https://en.wikipedia.org/wiki/List_of_largest_banks'

response = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
tables = pd.read_html(response.text)

df = tables [0]  # Selecting the first table found on the page

#Conclusion: Pandas makes it easy to scrape tabular data from web pages
#But to extract data from non-tabular formats, BeautifulSoup or similar libraries are needed

print(df)