numberOfInputs = int(input("Pairs of rows: ")) * 2
studentsDic = {}
name = ""

for i in range(1, numberOfInputs + 1):
    if i % 2 != 0:
        name = input()
        if name not in studentsDic:
            studentsDic[name] = []
    else:
        grade = float(input())
        studentsDic[name].append(grade)

for name, grades in studentsDic.items():
    average = sum(grades) / len(grades)
    if average >= 4.50:
        print(f"{name} -> {average:.2f}")
