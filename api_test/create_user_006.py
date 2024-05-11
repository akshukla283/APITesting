import json
import requests

# changing some data in 'data_02.json' file so
# we can make assertion fail
mydata = open("data_02.json", 'r').read()

# we are reading data here from json file so we have to load it

print(f"Data type : {type(mydata)}")
resp = requests.post("https://reqres.in/api/users", data=json.loads(mydata))
print(resp)
# if you want to print data
print(resp.json())
print("======"*3)
# we can use assert statement

assert resp.json()['job']=="Automation"