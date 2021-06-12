import json
import requests
import jsonpath
from requests.auth import HTTPBasicAuth

response = requests.get("https://api.github.com/users",auth=HTTPBasicAuth("manug30@gmail.com", "Yourmind#1"))
print(response.text)

