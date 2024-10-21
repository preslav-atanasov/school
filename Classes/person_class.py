from datetime import date, datetime

person_list = []


class Person:
    def __init__(self):
        self.name = input("Име?: ")
        self.country = input("Държава?: ")
        self.birthdate = (input("Дата на раждане?(DD/MM/YYYY): ")).split("/")

    def calculate_age(self):
        birthdate = date(int(self.birthdate[2]), int(self.birthdate[1]), int(self.birthdate[0]))
        today = datetime.now().date()
        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
        return age


person = Person()
age = person.calculate_age()
