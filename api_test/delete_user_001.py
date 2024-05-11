import requests

# in delete method response code should be 204

resp = requests.delete("https://reqres.in/api/users/2")
# as it doesn't return any data because there was no data to delete
# print(resp.json())
print("===="*3)
print(resp.status_code)

assert resp.status_code == 204, "User deletion Failed"








# Request
# / api / users / 2
#
# Response
# 204