hour = int(input("Chas? "))

if 0 <= hour < 24:  # mrazq if statements
    minute = int(input("Minuti? "))
    add15 = minute + 15

    if 0 <= minute < 60:
        if hour > 23 and minute > 45:
            hour = 0
        if minute > 45:
            add15 = minute - 45
            hour += 1

        formatted_minute = '{:02}'.format(add15)
        if hour == 24:
            hour = 0
        print(f"{hour}:{formatted_minute}")
    else:
        print("molq vuvedete minuti ot 0 do 59")
else:
    print("molq vuvedete chas ot 0 do 23")
