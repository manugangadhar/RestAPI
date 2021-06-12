import json

dict1 = '{ "firstName": "John", "lastName" : "doe", "age": 26, "address": 9}'

json_result = json.loads(dict1)
print(json_result["firstName"])

