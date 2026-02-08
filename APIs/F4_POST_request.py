'''
POST: It's used to send data to the server
'''

import requests

url_post = "http://httpbin.org/post"

payLoad = {"name":"Joseph","ID":"123"}

r_post = requests.post(url_post,data=payLoad)

#Below POST url doesn't have string queries 
#for GET url we had string queries
print(r_post.url)   


#GEt body doesn't had data
#Post Body has data
#It represents the data you sent to the server
print(r_post.request.body)  #return string queries

#It represents the data received by the server (server's version)
print(r_post.json()['form'])