from typing import Union

from fastapi import FastAPI

from src.database import Database
from src.person import Person

app = FastAPI()


database = Database()
database.create(Person("olivier"))
database.create(Person("louis"))
database.create(Person("Alexandre"))


@app.get("/api/persons")
def list_persons():
    return database.list_records()


@app.get("/api/persons/{person_id}")
def read_person(person_id: int):
    return database.read(person_id)
