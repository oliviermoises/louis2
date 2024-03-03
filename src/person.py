class Person:
    gender = None
    name = None
    weight = 0
    size = 0

    def __init__(self, name) -> None:
        self.name = name 



p1 = Person("olivier")

print (p1.gender)
print (p1.name)