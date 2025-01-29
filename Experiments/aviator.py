import random
import sys
import time
import keyboard

# Initialize winnings and player bet
winnings = 0
money = float(input("bet?: "))

# Start multiplier and game variables
start = 1.0  # Starting multiplier
x = 1  # Visual plane progression
fly_away = random.uniform(1, 10000)  # Random crash point

# Define growth phases (estimated behavior)
growth_phases = [
    {"end_multiplier": 2.0, "rate_per_second": 0.2},  # Linear growth phase
    {"end_multiplier": 5.0, "rate_per_second": 0.5},  # Moderate growth
    {"end_multiplier": 10.0, "rate_per_second": 1.0},  # Accelerated growth
    {"end_multiplier": 50.0, "rate_per_second": 2.0},  # Slower high multiplier growth
    {"end_multiplier": 100.0, "rate_per_second": 1.0}  # Extreme range growth slowing down
]


# Function to get the multiplier increment for a given range
def get_multiplier_increment(multiplier, growth_phases):
    for phase in growth_phases:
        if multiplier < phase["end_multiplier"]:
            return phase["rate_per_second"] * 0.1  # Increment every 0.1 seconds
    return 0  # Stop incrementing if past the max range


# Main game loop
while True:
    # Get the increment for the current multiplier
    increment = get_multiplier_increment(start, growth_phases)

    # Update the multiplier
    start += increment
    b = f"{start:.2f}"  # Format multiplier to 2 decimal places

    # Print the multiplier and plane
    sys.stdout.write('\r' + b)
    print("\n" + ("-" * x) + ">✈️")
    x += 1
    print("\r" * 5)  # Clear lines for neat display
    time.sleep(0.5)  # Wait for 0.1 seconds (visual effect)

    # Check if the plane crashes
    fly_away = random.uniform(1, 10000)  # Adjust crash randomness
    if fly_away < 2000:  # Simulated crash probability
        print("flew away!")
        break

    # Check for player cash out
    if keyboard.is_pressed("x"):
        winnings = money * start - money
        print(f"CASH OUT!! You won {winnings:.2f}")
        exit()

# If the loop ends, the plane has crashed
print("You lost!")
