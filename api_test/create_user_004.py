import requests

# changing data, this should create new id
payload = {
    "name": "Ankit",
    "job": "Automation"
    }
print(f"Data type : {type(payload)}")
resp = requests.post("https://reqres.in/api/users", data=payload)
print(resp)
# if you want to print data
print(resp.json())
print("======"*3)
# we can use assert statement

assert resp.json()['job']=="Automation"