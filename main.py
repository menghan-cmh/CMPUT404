import requests

# find requests library version
print(requests.__version__)

# GET the Google homepage
resp = requests.get("http://google.com")
print(resp.text)