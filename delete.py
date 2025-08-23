import requests
import config


url=config.users()+"192650"

r=requests.delete(url)
print(r)
