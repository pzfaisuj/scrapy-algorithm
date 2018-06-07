import requests

url = 'http://localhost:8095/products'

data = '''{
    "creationDate": "2018-06-02T13:09:13.534Z",
    "description": "string",
    "id": "string",
    "imageURL": "string",
    "links": [
      "string"
    ],
    "name": "string",
    "productCode": "string"
}'''
response = requests.post(url, data=data)
response = requests.get(url, data=data)
print(response.json())