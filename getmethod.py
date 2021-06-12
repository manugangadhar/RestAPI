import requests

url = 'https://reqres.in/api/users?page=2'
response = requests.get(url)
print(response)
print(response.content)
print("#####")
print(response.headers)
print(response.cookies)
print(response.elapsed)
try:
    assert response.status_code == 200, 'Status code is not valid'
except AssertionError as e:
    print(e)