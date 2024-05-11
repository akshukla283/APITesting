import requests

resp = requests.get("https://reqres.in/api/users?page=2")

json_response = resp.json()
print(json_response["total"])
print("======="*3)
assert json_response["total"] == 12
print("======="*3)
print(json_response["total_pages"])
assert json_response["total_pages"] == 3, "tatol pages count is not matching"