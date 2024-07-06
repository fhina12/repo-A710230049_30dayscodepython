import requests

response = requests.get("https://api.agify.io?name=michael")
data = response.json()
print(data)
