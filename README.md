
# demarrage:  _uvicorn src.main:app --reload --host 0.0.0.0 --port 8000_
# curl : 
curl http://localhost:8000/api/persons
curl -X DELETE http://localhost:8000/api/persons/1
