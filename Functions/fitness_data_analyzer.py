def calculate_bmi(thisweight, thisheight):
    thisbmi = thisweight / (thisheight ** 2)    # calculate using bmi formula
    return thisbmi


def calculate_calories_burned(thisduration):
    caloriesburned = thisduration * 7   # calculate average calories burned per minute
    return caloriesburned


def filter_overweight_people(thispeopledata):
    for _ in thispeopledata:
        thisbmi = calculate_bmi(person['weight'], person['height'])     # calculate bmi for every person
        if thisbmi >= 25:
            overweight_people.append(person)    # add overweight people to dictionary
    return overweight_people


people_data = []
overweight_people = []

# Main program

print("Enter fitness data for each person (Enter a blank name to finish)")

while True:     # start program loop
    name = input("Enter person's name: ").strip()
    if not name:
        break
    weight = float(input("Enter person's weight in kilograms: "))
    height = float(input("Enter person's height in meters: "))
    duration = float(input("Enter exercise duration in minutes: "))

    # create dictionary with needed information for every person (name, weight, height, exercise duration)
    person = {'name': name, 'weight': weight, 'height': height, 'duration': duration}
    people_data.append(person)

print("\nFitness Analysis:")
for person in people_data:
    bmi = calculate_bmi(person['weight'], person['height'])     # run the calculate bmi function
    calories_burned = calculate_calories_burned(person['duration'])     # calculate calories burned
    print(f"{person['name']}: BMI = {bmi:.2f}, Calories burned = {calories_burned}")    # format

print("\nOverweight People:")
overweight_people = filter_overweight_people(people_data)   # use function to filter overweight ppl
for person in overweight_people:
    bmi = calculate_bmi(person['weight'], person['height'])
    print(f"{person['name']}: BMI = {bmi:.2f}")     # format
