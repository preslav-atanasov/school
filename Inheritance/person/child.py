from person import Person


class Child(Person):
    def __init__(self, name: str, age: int):
        super().__init__(name, age)


person = Person("Peter", 25)
child = Child("Peter Jr", 5)
print(person.name)
print(person.age)
print(child.__class__.__bases__[0].__name__)