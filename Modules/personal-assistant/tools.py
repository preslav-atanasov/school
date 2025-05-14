import datetime
import pyjokes
import pytz


def greet_user():
    now = datetime.datetime.now()
    hour = now.hour

    if hour < 12:
        greeting = "Good morning"
    elif hour < 18:
        greeting = "Good afternoon"
    else:
        greeting = "Good night"

    print(f"{greeting}")


def tell_joke():
    print(pyjokes.get_joke())


def show_time():
    current_time = datetime.datetime.now(pytz.timezone('Europe/Sofia'))
    print(f"The current time is {current_time}")


def convert_temperature(celsius):
    return celsius * 9 / 5 + 32


