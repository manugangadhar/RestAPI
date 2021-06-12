import json
import requests
import jsonpath

response = requests.get(url='https://reqres.in/api/users?page=2')

print(response.content)
json_content = json.loads(response.content)
print(json_content)
pages = jsonpath.jsonpath(json_content, "page")
print(pages)
print(json_content['page'])