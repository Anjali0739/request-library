import requests
import config

r=requests.get(config.users())
print(r.json())