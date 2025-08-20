import requests
from requests.exceptions import Timeout


BASE_URL = "https://catfact.ninja/fact"

max_retries=3

for i in range(max_retries):
    try:
        resp=requests.get(BASE_URL, timeout=0.3)
        print(resp.text)
        print(resp.status_code)
        break
    except Timeout as t:
        print("Timeout Error")
else:
    print("All retries failed")
