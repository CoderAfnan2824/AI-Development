import requests

url = "https://www.ibm.com"

r = requests.get(url)

#Obtain status for get request
print(r.status_code)

print(r.encoding)   #returns UTF-8
print(r.request.body)
print(r.request.headers)

header = r.headers
print(header)

print(r.text[0:100])
