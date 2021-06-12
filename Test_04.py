# Add student data

import json
import requests
import jsonpath


def test_poststudentdetails():
    fd = open("C:\\DVF\\Scripting\\RestAPI\\studentdetails.json", 'r')
    response = requests.post()
    fd.close()
    url = "https://thetestingworldapi.com/api/studentsDetails"
    response = requests.get(url)
    print(response.text)

