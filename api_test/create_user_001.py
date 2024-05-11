import requests

# we can say data or payload
payload = {
    "name": "morpheus",
    "job": "leader"
    }
print(f"Data type : {type(payload)}")
resp = requests.post("https://reqres.in/api/users", data=payload)
print(resp)
