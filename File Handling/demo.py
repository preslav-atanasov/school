with open("info.txt", "w+") as file:
    file.write("Preslav A.\n")
    file.write("17\n")
    file.seek(0)
    print(file.read())


