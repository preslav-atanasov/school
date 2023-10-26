weekday = str(input("Den ot sedmicata : "))
ticket = 777

if weekday.lower() in ["monday", "tuesday", "friday"]:
    ticket = 12
elif weekday.lower() in ["wednesday", "thursday"]:
    ticket = 14
elif weekday.lower() in ["saturday", "sunday"]:
    ticket = 16
print(ticket)
