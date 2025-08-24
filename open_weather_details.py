import requests

url="https://api.openweathermap.org/data/2.5/weather"

api_key="a2a60e5a5258fd801a9cc17d23d3cf18"

queries={
    "q":input("Enter the city name: "),
    "appid":api_key
}

r=requests.get(url, params=queries)
print(r.json())
