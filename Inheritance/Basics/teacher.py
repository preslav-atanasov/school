class Person:
    def sleep(self):
        return f"kuchki..."


class Employee:
    def get_fired(self):
        return f"fuck..."


class Teacher(Person, Employee):
    def teach(self):
        return f"obrazovam."


teacher = Teacher()
teacher.sleep()
teacher.get_fired()
teacher.teach()
