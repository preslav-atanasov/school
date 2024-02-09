energy = 100
coins = 100

events = input()
events_list = events.split('|')             # Split events from rest-2|order-10 to rest-2, order-10

for event in events_list:
    singleEvent = event.split('-')          # Split events further

    if singleEvent[0] == "rest":
        if energy < 100:                    # Cap energy at 100
            energy += int(singleEvent[1])
            print(f"You gained {int(singleEvent[1])} energy!")
        else:
            print("You gained 0 energy!")
        print(f"Current energy: {energy}")

    elif singleEvent[0] == "order":
        if energy >= 30:                    # Check if there's enough energy
            coins += int(singleEvent[1])
            print(f"You earned {int(singleEvent[1])} coins!")
            energy -= 30                    # Deduct energy after placing an order
        else:
            print("You had to rest!")

    else:
        if coins > int(singleEvent[1]):     # Check if there's enough money for order
            coins -= int(singleEvent[1])    # Deduct amount of money for purchase
            print(f"You bought {singleEvent[0]}")
        else:                               # Close store if there isn't enough money
            print(f"Closed! Cannot afford {singleEvent[0]}")
            exit()

print("Day completed!")
print(f"Coins = {coins}")
print(f"Energy = {energy}")
