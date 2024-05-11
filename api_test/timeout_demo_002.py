import requests

# there is website about making response delay
# https://httpbin.org/#/Dynamic_data/put_delay__delay_
# in this there is limit of delaying of 10 sec

# Now going to make it reverse so that we make it faile
# I mean assertion check
r = requests.get("https://httpbin.org/delay/5", timeout=3)
print(r.status_code)

# we will get response within 3 seconds
