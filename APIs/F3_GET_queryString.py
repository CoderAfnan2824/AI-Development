'''
Query String is a part of URL that sends extra details after '?' to filter,search, pass info

format: 
base_url/get?key=value&key2=value2
'''

import requests

url_get = "http://httpbin.org/get"

pay_load = {'name':'Joseph','ID':'123'}

r = requests.get(url_get,params=pay_load)

print(r.status_code)
print(r.url)
print(r.request.body)

#print(r.text)
print(r.headers['Content-Type'])

print(r.json())

print(r.json()['args']) #returns key values used in query string