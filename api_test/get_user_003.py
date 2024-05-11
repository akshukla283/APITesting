import requests

resp = requests.get("https://reqres.in/api/users?page=2")

code=resp.status_code
assert code==200, "Code doesn't match"
# suppose we want data
print(resp.json())
print("======="*3)
print(type(resp.headers))
print("======="*3)
print(resp.headers)
print("======="*3)
print(resp.cookies)
print("======="*3)
print(resp.encoding)
print("======="*3)
print(resp.url)