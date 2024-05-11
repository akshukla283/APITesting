import json
import requests

# if you want to updated 'name' part
payload = {
    "name": "API-Testing"
    }

resp = requests.patch("https://reqres.in/api/users/2", data=payload)
print(resp)
print("====="*3)
print(resp.json())
print(resp.headers.get("Content-Type"))
assert resp.json()['name'] =="API-Testing"

# Request
# / api / users / 2
#
# {
#     "name": "morpheus",
#     "job": "zion resident"
# }
#
# Response
# 200
#
# {
#     "name": "morpheus",
#     "job": "zion resident",
#     "updatedAt": "2024-05-11T19:52:36.619Z"
# }
