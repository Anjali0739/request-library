import requests
import config

url=config.users() + "193687"
# print(url)

data=dict()
data['name']= "Depender"

r=requests.put(url, data=data)
print(r)
