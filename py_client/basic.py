import requests

endpoint = "http://127.0.0.1:8000/api/"
get_response = requests.post(endpoint, json={"title": "2nd product", "content": "Hello world", "price": "200"})
# get_response = requests.get(endpoint, json={"product_id": 1})
print (get_response.json())