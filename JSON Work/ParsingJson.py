# Parsing the dictionary to a Json and vice versa

import requests
import json
import jsonpath

sample_dictionary = '{"Name" : "Ram", "Age" : "22"}'

# Loads method is used to parse a string dictionary to a JSON
print(json.loads(sample_dictionary))

url = "https://reqres.in/api/users?page=2"
response = requests.get(url)
# Below method will display a string
print(response.text)

# Parsing the response string into a Json format
json_response = json.loads(response.text)
print(json_response)

# Applying JSON Path
print(jsonpath.jsonpath(json_response,"data[0].email"))

# Data key has an array from which ID value is got
for i in json_response['data']:
    print(i['id'])