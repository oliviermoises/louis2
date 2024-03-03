from pydantic import BaseModel


class Person(BaseModel):
    id: int | None = None
    name: str
