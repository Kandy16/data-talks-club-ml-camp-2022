import requests


# ## question 4

# url = 'http://127.0.0.1:8080/'
# url = 'http://0.0.0.0:8080/'
# url = 'http://localhost:2345/'


# #response = requests.get(url)

# url = "http://127.0.0.1:2345/predict"
# client = {"reports": 0, "share": 0.245, "expenditure": 3.438, "owner": "yes"}
# response = requests.post(url, json=client)

# print(response.json())


## question 6

url = "http://127.0.0.1:8080/predict"
client = {"reports": 0, "share": 0.245, "expenditure": 3.438, "owner": "yes"}
response = requests.post(url, json=client)

print(response.json())