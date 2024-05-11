import json
import requests

# Now we can use 'patch',
# Note in 'post' there is header CreatedAt but
# for 'put' and 'patch' this will we 'UpdatedAt'

payload = {
    "name": "Ankit",
    "job": "API Testing"
    }

resp = requests.patch("https://reqres.in/api/users/2", data=payload)
print(resp)
print("====="*3)
print(resp.json())
print(resp.headers.get("Content-Type"))
assert resp.json()['job'] =="API Testing"

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
