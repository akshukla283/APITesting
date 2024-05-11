import requests

# user and password for this authentication is "admin"
# but let's try with dummy user so that it should response different outcome
resp = requests.get("https://the-internet.herokuapp.com/basic_auth", auth=('asda', 'asd'))
print(resp.status_code)