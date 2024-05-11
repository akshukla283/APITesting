import requests

resp = requests.get("https://reqres.in/api/users?page=2")

code=resp.status_code
assert code==200, "Code doesn't match"
# suppose we want data

print(resp.text)
print("======"*2)
print(resp.content)
print("======"*2)
print(resp.json())