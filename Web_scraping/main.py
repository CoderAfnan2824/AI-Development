'''
It's a way to obtain data from the internet for data analysis, price comparison, content aggregation

Steps involved:
1. HTTP request: send a request to web server to obtain web page
2. HTML retrieval: receives the web page in HTML
3. HTML Parsing: the web page data is broken down into components like tag, attribute, 
4. Data extraction: here the data is extracted by identifying the type (text, link, images,etc)
5. Data transformation: All unnecessary tags, keywords are removed and data prepared
6. Storage: the data will be stored in database, csv, json, spreadsheet, etc

'''
#BeautifulSoap is used to parse the HTML data
import requests
from bs4 import BeautifulSoup


url = "https://en.wikipedia.org/wiki/IBM"

response = requests.get(url)
html_content = response.text

soup = BeautifulSoup(html_content, 'html.parser')

#print(html_content[:500])  # Print first 500 characters of the HTML content

links = soup.find_all('a')  # Find all anchor tags


#print all the links on the page
for link in links:
    print(link.text)