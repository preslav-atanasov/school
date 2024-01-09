import calendar

year = int(input("bday year: "))
month = int(input("bday month (in numbers): "))
day = int(input("bday day: "))
weekday = "none"
print(calendar.calendar(year))

if calendar.weekday(year, month, day) == 0:
    weekday = "Monday"
elif calendar.weekday(year, month, day) == 1:
    weekday = "Tuesday"
elif calendar.weekday(year, month, day) == 2:
    weekday = "Wednesday"
elif calendar.weekday(year, month, day) == 3:
    weekday = "Thursday"
elif calendar.weekday(year, month, day) == 4:
    weekday = "Friday"
elif calendar.weekday(year, month, day) == 5:
    weekday = "Saturday"
elif calendar.weekday(year, month, day) == 6:
    weekday = "Sunday"

print(f"your birthday is on a {weekday}")
