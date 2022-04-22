import requests


endpoint = "http://127.0.0.1:8000/api/products/"

data = {
    "title": "this is new field",
    "content": "let's create some content "
}
get_response = requests.post(endpoint, json=data)
print (get_response.json())