examHour = int(input("Chas na izpita: "))
examMinute = int(input("Minuta na izpita: "))
arrivalHour = int(input("Chas na pristigane: "))
arrivalMinute = int(input("Minuta na pristigane: "))

# proverki za pravilno vreme
if (0 <= examHour or arrivalHour < 24) or (0 <= examMinute or arrivalMinute < 60):

    # chasove kum minuti
    examTime = (examHour * 60) + examMinute
    arrivalTime = (arrivalHour * 60) + arrivalMinute

    if arrivalTime <= examTime:
        if examTime - arrivalTime > 30:
            print("Early")
            formattedTime = "{:d}:{:02d}".format(examHour - arrivalHour, examMinute - arrivalMinute)
            print(f"{formattedTime} hours before the start.")
            exit()
        print("On time")
        if examTime - arrivalTime > 0:
            print(f"{examTime - arrivalTime} minutes before the start")
        else:
            exit()
    else:
        print("Late")
        if arrivalTime - examTime <= 59:
            print(f"{arrivalTime - examTime} minutes after the start")
        else:
            formattedTime = "{:d}:{:02d}".format(arrivalHour - examHour, arrivalMinute - examMinute)
            print(f"{formattedTime} hours after the start.")
else:
    print("Molq vuvedete pravilno chas i minuta.")
