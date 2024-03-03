from typing import Union

from fastapi import FastAPI

from src.database import Database
from src.person import Person

app = FastAPI()


database = Database()

# renvoie toutes les personnes
@app.get("/api/persons")
def list_persons():
    return database.list_records()

# renvoie une personne dont l'id est passé
@app.get("/api/persons/{person_id}")
def read_person(person_id: int):
    return database.read(person_id)


# suppr une personne dont l'id est passé
@app.delete("/api/persons/{person_id}")
def delete_person(person_id: int):
    database.delete(person_id)

@app.post("/api/persons")
def create_person(person:Person):
    database.create(person)