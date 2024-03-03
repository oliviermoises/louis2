from typing import Annotated, Union

from fastapi import FastAPI, Form

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
def create_person(person: Person):
    database.create(person)


# si utilisation du get
@app.get("/api/obtient_pret")
def obtient_pret(person: Person):
    if person.name[0] == "o":
        return True
    return False


# si utilisation du Form HTML
# https://fastapi.tiangolo.com/tutorial/request-forms/
@app.post("/api/obtient_pret")
def login(
    ch1: Annotated[str, Form()],
    ch2: Annotated[str, Form()],
    ch3: Annotated[str, Form()],
    ch4: Annotated[str, Form()],
    ch5: Annotated[str, Form()],
    ch6: Annotated[str, Form()],
):
    return True
