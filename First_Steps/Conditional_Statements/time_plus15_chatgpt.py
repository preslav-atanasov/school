hour = int(input("Chas? "))

if 0 <= hour < 24:
    minute = int(input("Minuti? "))
    add15 = minute + 15

    if 0 <= minute < 60:
        if minute > 45:
            add15 = minute - 45
            hour = (hour + 1) % 24  # Ensure hour is within 0-23 range

        formatted_minute = str(add15).zfill(2)
        print(f"{hour}:{formatted_minute}")

    else:
        print("Molq vuvedete minuti ot 0 do 59")

else:
    print("Molq vuvedete chas ot 0 do 23")