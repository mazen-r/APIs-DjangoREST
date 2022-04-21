import requests

endpoint = "http://127.0.0.1:8000/api"

get_reponse = requests.get(endpoint, json={"query": "request sent"})