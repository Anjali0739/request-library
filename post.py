import requests
import config

url = config.users()

name=input("Enter your name: ")
email=input("Enter your email: ")
gender=input("Enter your gender: ")
status=input("Enter the status: ")

data=dict()
data['name']=name
data['email']=email
data['gender']=gender
data['status']=status

# print(data)

r=requests.post(url,data=data)
print(r)
