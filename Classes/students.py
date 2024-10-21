class Class:
    student_count = 16

    def __init__(self, name):
        self.name = name
        self.students = []
        self.grades = []

    def add_student(self, name: str, grade: float):
        if len(self.students) < Class.student_count:
            self.students.append(name)
            self.grades.append(grade)

    def grade_avg(self):
        avg = sum(self.grades) / len(self.students)
        return float(f"{avg:.2f}")

    def __repr__(self):
        students = " || ".join(self.students)
        print(f"The students in {self.name}: {students}. Average grade: {self.grade_avg()}")


v_class = Class("11В")
while True:
    enter_student = input("Въведете име на ученика (или 'е' за край): ")
    if len(v_class.students) < Class.student_count:
        v_class.students.append(enter_student)
    else:
        break
    if enter_student.lower() == "e":
        break
    enter_grade = float(input("Въведете средния успех на ученика: "))
    if 2.00 <= enter_grade <= 6.00:
        v_class.grades.append(enter_grade)
    else:
        print("Моля въведете оценка м-у 2.00 и 6.00")

v_class.__repr__()



