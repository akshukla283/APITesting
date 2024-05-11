import requests

# paste your data from https://reqres.in/api/users?page=2
# to https://jsonviewer.stack.hu/ to view it
# passing parameters to test the urls
# check arguments of 'get' press 'ctrl' and hover mouse over 'get' or click

p = {"page":2}

resp = requests.get("https://reqres.in/api/users", params=p)
print(resp.url)

json_response = resp.json()
print(json_response["data"][0]["email"])
print("======="*3)
assert (json_response["data"][0]["email"]).endswith("reqres.in"), "Email format is not matching"
# print("======="*3)
# assert (json_response["data"][0]["email"]).endswith("gmail.com"), "Email format is not matching"
print(json_response["data"][2]["last_name"])
print("======="*3)
print("Getting urls")
print(json_response["support"]["url"])
