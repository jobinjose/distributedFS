import requests as r
import json as j

url = "http://localhost:8188/"
file_name = input("Enter the path: ")
url = url + str(file_name)
response = r.post(url)
print("Response : ", response.text)
