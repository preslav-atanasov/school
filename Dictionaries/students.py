students = []

while True:
    command = input("Enter student details (name:id:course)")
    if ":" in command:
        elements = command.split(":")
        studentName = elements[0]
        studentId = elements[1]
        studentCourse = elements[2]

        # Create a dictionary for the student
        student = {'name': studentName, 'id': studentId, 'course': studentCourse}
        students.append(student)
    else:
        break

for student in students:
    if student['course'] == command:
        print(f"{student['name']} - {student['id']}")

