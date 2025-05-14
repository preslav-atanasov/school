import tools

while True:
    print("\n - -- Личен асистент - --")
    print("1. Поздрави  ме")
    print("2. Кажи ми смешка")
    print("3. Покажи дата и час")
    print("4. Преобразувай температура")
    print("5. Изход")

    choice = input(" Избери опция:")

    if choice == "1":
        tools.greet_user()
    elif choice == "2":
        tools.tell_joke()
    elif choice == "3":
        tools.show_time()
    elif choice == "4":
        c = float(input("Въведи температура в °C: "))
        print(f"{c}°C = {tools.convert_temperature(c)}°F")
    elif choice == "5":
        print("Довиждане!")
        break
    else:
        print("Невалиден избор.")
