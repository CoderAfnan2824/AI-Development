
from bs4 import BeautifulSoup
import requests

html="<!DOCTYPE html><html><head><title>Page Title</title></head><body><h3><b id='boldest'>Lebron James</b></h3><p> Salary: $ 92,000,000 </p><h3> Stephen Curry</h3><p> Salary: $85,000, 000 </p><h3> Kevin Durant </h3><p> Salary: $73,200, 000</p></body></html>"

table="<table><tr><td id='flight'>Flight No</td><td>Launch site</td> <td>Payload mass</td></tr><tr> <td>1</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a></td><td>300 kg</td></tr><tr><td>2</td><td><a href='https://en.wikipedia.org/wiki/Texas'>Texas</a></td><td>94 kg</td></tr><tr><td>3</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a> </td><td>80 kg</td></tr></table>"

soup = BeautifulSoup(html, 'html.parser')

table_soup = BeautifulSoup(table, 'html.parser')

#print(soup.prettify())  # Print the formatted HTML content

tag_object = soup.h3

tag_child = tag_object.b

tag_parent = tag_child.parent
sibling_1 = tag_object.next_sibling

print(tag_child)
print(tag_parent)
print(sibling_1)

#Navigable string is used to extract the text content of a tag
print(f"string data: {tag_object.string}")  # Extract the text content of the <h3> tag

print(tag_child.attrs)  # Print the attributes of the <b> tag
print(tag_child['id'])  # Access the 'id' attribute of the <b>

table_rows = table_soup.find_all('tr')
print(table_rows[0])
print(table_rows[1].td)  # Access the first <td> element of the second row

#iterating through all the rows of the table
for i, row in enumerate(table_rows):
    print(f"Row {i}: {row}")
    cells = row.find_all('td')  #print html content of each row in the table
    for j, cell in enumerate(cells):
        print(f' cell {j}: {cell.text}')  # Print the text content of each cell


#prints attributes 
print(table_soup.find_all(id = 'flight'))