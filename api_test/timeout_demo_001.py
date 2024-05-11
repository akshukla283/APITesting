import requests

# there is website about making response delay
# https://httpbin.org/#/Dynamic_data/put_delay__delay_
# in this there is limit of delaying of 10 sec

# first giving 10 second so that code should work and
# later will make it 5 second to check
# in url we gave 3 seconds means we get response in 3 sec
r = requests.get("https://httpbin.org/delay/3", timeout=10)
print(r.status_code)

# we will get response within 3 seconds
