import requests

resp = requests.get("https://reqres.in/api/users?page=2")
# print(resp)
# print(type(resp))
# print(dir(resp))
code=resp.status_code
# assert code==200, "Code doesn't match"
assert code==201, "Code doesn't match"