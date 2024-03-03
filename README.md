
# demarrage:  _uvicorn src.main:app --reload --host 0.0.0.0 --port 8000_
# curl : 
curl http://localhost:8000/api/persons
curl -X DELETE http://localhost:8000/api/persons/1
curl -X POST 'http://localhost:8000/api/persons' -H 'Content-Type: application/json' -d '{"id":0, "name" : "olivier"}'


curl -v -X GET http://localhost:8000/api/obtient_pret -H 'Content-Type: application/json' -d '{ "name" : "zolivier"}'
