import requests

# find requests library version
print("\n\n==========")
print("The Version of requests is: ", requests.__version__)
print("=========\n")

# GET the Google homepage
print("\n\n==========")
print("GET the Google homepage")
print("=========\n")
resp = requests.get("http://google.com")
print(resp.text)

# Download itself
print("\n\n==========")
print("GET the source code of Python script")
print("=========\n")
itself = requests.get("https://raw.githubusercontent.com/menghan-cmh/CMPUT404/master/lab1.py")
print(itself.text)