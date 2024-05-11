import requests

# always check that you are using valid url
# we can update data like email and all
payload = {
    "email": "eve.holt@reqres.in",
    "password": "pistol"
}

resp = requests.post("https://reqres.in/api/register", data=payload)
print(resp)
# if you want to print data
print(resp.json())
print("======"*3)
# we can use assert statement

print(resp.json()['token'])