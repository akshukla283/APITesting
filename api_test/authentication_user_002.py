import requests

# user and password for this authentication is "admin"
# now use proper user and password
resp = requests.get("https://the-internet.herokuapp.com/basic_auth", auth=('admin', 'admin'))
print(resp.status_code)
