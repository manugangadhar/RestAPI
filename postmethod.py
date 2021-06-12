import json
import requests
import jsonpath

fd = open("C:\\DVF\\Scripting\\RestAPI\\file1.json", 'r')
file_content = fd.read()
fd.close()

json_format = json.loads(file_content)
response = requests.post("https://reqres.in/api/register", json_format)
print(response.status_code)
print(response.content)

response_json_format = json.loads(response.text)
print(response_json_format)
print(jsonpath.jsonpath(response_json_format, "id"))