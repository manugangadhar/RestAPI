import json
import requests
import jsonpath

fd = open('C:\\DVF\\Scripting\\RestAPI\\file2.json','r')
json_format = json.loads(fd.read())
fd.close()


response = requests.put('https://reqres.in/api/users?page=2', json_format)
print(response.status_code)
print(response.content)