import json
import requests

# suppose we want some header or content type
mydata = open("data_01.json", 'r').read()

# we are reading data here from json file so we have to load it

print(f"Data type : {type(mydata)}")
resp = requests.post("https://reqres.in/api/users", data=json.loads(mydata))
print(resp)
# if you want to print data
print(resp.json())
print("======"*3)
# we can use assert statement
assert resp.json()['job']=="Automation"

print(resp.headers.get("Content-Type"))

# out--> application/json