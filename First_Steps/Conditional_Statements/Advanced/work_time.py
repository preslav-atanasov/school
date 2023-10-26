hour = int(input("chas ot denonoshtieto : "))
weekday = str(input("den ot sedmicata : "))

if weekday.lower() in ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]:
    if 10 <= hour <= 18:
        print("open")
else:
    print("closed")
