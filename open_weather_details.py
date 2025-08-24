import requests

url="https://api.openweathermap.org/data/2.5/weather"

api_key=""

queries={
    "q":input("Enter the city name: "),
    "appid":api_key
}

r=requests.get(url, params=queries)
print(r.json())
