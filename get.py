import requests
import config

# r=requests.get(config.users())
# print(r.json())

url=config.users()
print(url)
r=requests.get(url)
print(r.status_code)
print(r.text)
