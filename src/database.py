from src.person import Person


class Database:
    def __init__(self) -> None:
        self.__d = dict()
        self.__internal_index = 0

    def create(self, record: Person) -> int:
        record.id = self.__internal_index
        self.__d[record.id] = record
        self.__internal_index += 1
        return record.id

    def update(self, index, record: Person):
        self.__d[index] = record

    def read(self, index: int) -> Person:
        return self.__d[index]

    def delete(self, index):
        del self.__d[index]

    def list_records(self) -> list[Person]:
        return list(self.__d.values())
