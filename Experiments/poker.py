import random


def check_straight(values):
    ranks = [card_ranks[x] for x in values]
    ranks.sort()

    for i in range(len(ranks) - 4):
        if (ranks[i] + 1 == ranks[i+1] and ranks[i+1] + 1 == ranks[i+2] and
                ranks[i+2] + 1 == ranks[i+3] and ranks[i+3] + 1 == ranks[i+4]):
            return True
    return False


final_hand = 0

cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
card_ranks = {'2': 0, '3': 1, '4': 2, '5': 3, '6': 4, '7': 5, '8': 6, '9': 7, '10': 8,
              'J': 9, 'Q': 10, 'K': 11, 'A': 12}
dyes = ["♠", "♣", "♥", "♦"]

hand_unformatted_value = [random.choice(cards), random.choice(cards)]
hand_unformatted_dye = [random.choice(dyes), random.choice(dyes)]

hand = (f"{hand_unformatted_value[0]}{hand_unformatted_dye[0]} "
        f"{hand_unformatted_value[1]}{hand_unformatted_dye[1]}")


table_unformatted_value = [random.choice(cards), random.choice(cards), random.choice(cards)]
table_unformatted_dye = [random.choice(dyes), random.choice(dyes), random.choice(dyes)]

table = (f"{table_unformatted_value[0]}{table_unformatted_dye[0]} "
         f"{table_unformatted_value[1]}{table_unformatted_dye[1]} "
         f"{table_unformatted_value[2]}{table_unformatted_dye[2]}")

print(table)
print(hand)
gaming = True

# Poker game loop
while len(table_unformatted_value) < 5:
    print("Your move? (Hit/Fold)")
    userinput = input()

    if userinput == "fold":
        print("You have folded your hand.")
        exit()

    if userinput == "hit":
        table_unformatted_value.append(random.choice(cards))
        table_unformatted_dye.append(random.choice(dyes))
        table += f" {table_unformatted_value[-1]}{table_unformatted_dye[-1]}"
        print(table)
        print(hand)

# Create a list of all card values and dyes to check for hands after game end
hand_and_table_dye = table_unformatted_dye + hand_unformatted_dye
hand_and_table_dye.sort()

all_cards = table_unformatted_value + hand_unformatted_value
all_cards.sort(key=lambda x: card_ranks[x])


# Create a no duplicates list of all card values to check for a straight.
all_cards_no_dupes = list(set(all_cards))
all_cards_no_dupes.sort(key=lambda x: card_ranks[x])

# Create a definition for a "pair" and a "triplet" to check for... pairs and three of a kind.
pairs = [item for item in set(all_cards) if all_cards.count(item) == 2]
triplets = [item for item in set(all_cards) if all_cards.count(item) == 3]

hand_and_table_dye = hand_unformatted_dye + table_unformatted_dye
hand_and_table_dye.sort()

first_five_elements = hand_and_table_dye[0:5]

if check_straight(all_cards_no_dupes):
    for i in range(len(all_cards_no_dupes) - 4):
        if len(set(hand_and_table_dye[i:i+5])) == 1:
            if all(card in all_cards_no_dupes for card in ["10", "J", "Q", "K", "A"]):
                final_hand = max(final_hand, 9)  # royal flush
            else:
                final_hand = max(final_hand, 8)    # straight flush
            break
    else:
        final_hand = max(final_hand, 4)  # straight

for item in set(all_cards):
    if all_cards.count(item) == 4:
        final_hand = max(final_hand, 7)    # four of a kind

if len(triplets) == 1:
    if len(pairs) == 1:
        final_hand = max(final_hand, 6)    # full house
    else:
        final_hand = max(final_hand, 3)    # three of a kind

if len(pairs) == 1:
    final_hand = max(final_hand, 1)    # pair
if len(pairs) >= 2:
    final_hand = max(final_hand, 2)    # two pair

hand_types = {
    0: "High card.",
    1: "Pair.",
    2: "Two pair!",
    3: "Three of a kind!",
    4: "Straight!",
    5: "Flush!",
    6: "Full house! (BOAT)",
    7: "Four of a kind!",
    8: "Straight flush!",
    9: "Royal flush!"
}


if final_hand in hand_types:
    print(hand_types[final_hand])
else:
    print("how did you break my little poker game :(")
