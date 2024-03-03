import requests

r = requests.get("http://localhost:8000/api/persons/1")

print (r.json())
