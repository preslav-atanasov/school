class Person:
    kind = "mammal"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello!"


class Student(Person):
    def __init__(self, name, age, num):
        super().__init__(name, age)
        self.num = num

    def greet(self):
        super().greet()

    def study_for_exam(self):
        return f"Studying!"