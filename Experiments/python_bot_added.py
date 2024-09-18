import random
import time
from collections import deque, Counter


def check_straight(values):
    ranks = [card_ranks[x] for x in values]
    ranks.sort()
    for i in range(len(ranks) - 4):
        if (ranks[i] + 1 == ranks[i+1] and ranks[i+1] + 1 == ranks[i+2] and
                ranks[i+2] + 1 == ranks[i+3] and ranks[i+3] + 1 == ranks[i+4]):
            return True
    return False


def handle_user_input(prompt, valid_inputs=None):
    while True:
        user_input = input(prompt).lower()
        if valid_inputs is None:
            if user_input in ["yes", "no", "hit", "fold", "raise"]:
                return user_input
            else:
                print("Please enter a valid command.")
        else:
            if user_input in valid_inputs:
                return user_input
            else:
                print("Please enter a valid command.")


def exit_if_no():
    if user_command == "no":
        print("Exiting program...")
        time.sleep(0.5)
        exit()


def print_result(winner, bot_hand_unformatted_value, bot_hand_unformatted_dye, money, raised_sum):
    if winner == "bot":
        print(f"You have: {hand_types[final_hand]}")
        print("Bot wins!")
        print(f"Bot's hand: {bot_hand_unformatted_value[0]}{bot_hand_unformatted_dye[0]}"
              f" {bot_hand_unformatted_value[1]}{bot_hand_unformatted_dye[1]}. It has {hand_types[bot_final_hand]}")
        money -= raised_sum
    elif winner == "user":
        print("You win!")
        print(f"You have: {hand_types[final_hand]}")
        print(f"Bot's hand: {bot_hand_unformatted_value[0]}{bot_hand_unformatted_dye[0]}"
              f" {bot_hand_unformatted_value[1]}{bot_hand_unformatted_dye[1]}. It has {hand_types[bot_final_hand]}")
        money += raised_sum * 2
    else:
        print("It's a tie!")
        print(f"You have: {hand_types[final_hand]}")
        print(f"Bot's hand: {bot_hand_unformatted_value[0]}{bot_hand_unformatted_dye[0]}"
              f" {bot_hand_unformatted_value[1]}{bot_hand_unformatted_dye[1]}. It has {hand_types[bot_final_hand]}")
        money += raised_sum


money = 100
raised_sum = 0
card_ranks = {'2': 0, '3': 1, '4': 2, '5': 3, '6': 4, '7': 5, '8': 6, '9': 7, '10': 8,
              'J': 9, 'Q': 10, 'K': 11, 'A': 12}
dyes = ["♠", "♣", "♥", "♦"]
deck = deque([(value, dye) for value in card_ranks for dye in dyes])
random.shuffle(deck)

user_command = handle_user_input("Would you like to play a game? (Yes/No) : ", ["yes", "no"])
exit_if_no()

while True:
    hand = [deck.pop(), deck.pop()]
    hand_unformatted_value = [card[0] for card in hand]
    hand_unformatted_dye = [card[1] for card in hand]
    hand = (f"{hand_unformatted_value[0]}{hand_unformatted_dye[0]}"
            f" {hand_unformatted_value[1]}{hand_unformatted_dye[1]}")

    bot_hand = [deck.pop(), deck.pop()]
    bot_hand_unformatted_value = [card[0] for card in bot_hand]
    bot_hand_unformatted_dye = [card[1] for card in bot_hand]
    bot_hand = (f"{bot_hand_unformatted_value[0]}{bot_hand_unformatted_dye[0]}"
                f" {bot_hand_unformatted_value[1]}{bot_hand_unformatted_dye[1]}")

    table = [deck.pop(), deck.pop(), deck.pop()]
    table_unformatted_value = [card[0] for card in table]
    table_unformatted_dye = [card[1] for card in table]
    table = (f"{table_unformatted_value[0]}{table_unformatted_dye[0]} "
             f"{table_unformatted_value[1]}{table_unformatted_dye[1]} "
             f"{table_unformatted_value[2]}{table_unformatted_dye[2]}")

    print(table)
    print(hand)
    gaming = True
    hand_folded = False

    while len(table_unformatted_value) < 5:
        user_input = handle_user_input("Your move? (Hit/Fold/Raise) : ", ["hit", "fold", "raise"])

        if user_input == "fold":
            print("You have folded your hand.")
            time.sleep(0.5)
            hand_folded = True
            break

        elif user_input == "hit":
            new_card = deck.pop()
            table_unformatted_value.append(new_card[0])
            table_unformatted_dye.append(new_card[1])
            table += f" {table_unformatted_value[-1]}{table_unformatted_dye[-1]}"
            print(table)
            print(hand)

        elif user_input == "raise":
            if int(money > 0):
                amount = int(input("What amount would you like to raise? : "))
                if amount <= money:
                    print(f"Raising by {amount}.")
                    money -= amount
                    raised_sum += amount
                    new_card = deck.pop()
                    table_unformatted_value.append(new_card[0])
                    table_unformatted_dye.append(new_card[1])
                    table += f" {table_unformatted_value[-1]}{table_unformatted_dye[-1]}"
                    print(table)
                    print(hand)
                else:
                    print("You don't have enough money for such a raise.")
            else:
                print("Too broke to raise.")

    all_cards = table_unformatted_value + hand_unformatted_value
    all_cards_no_dupes = list(set(all_cards))
    all_cards_no_dupes.sort(key=lambda x: card_ranks[x])

    hand_and_table_dye = hand_unformatted_dye + table_unformatted_dye
    hand_and_table_dye.sort()

    card_counts = Counter(all_cards)
    pairs = [card for card, count in card_counts.items() if count == 2]
    triplets = [card for card, count in card_counts.items() if count == 3]
    four_of_a_kind = [card for card, count in card_counts.items() if count == 4]

    final_hand = 0

    if check_straight(all_cards_no_dupes):
        for i in range(len(all_cards_no_dupes) - 4):
            if len(set(hand_and_table_dye[i:i+5])) == 1:
                if all(card in all_cards_no_dupes for card in ["10", "J", "Q", "K", "A"]):
                    final_hand = max(final_hand, 9)  # royal flush
                else:
                    final_hand = max(final_hand, 8)  # straight flush
                break
        else:
            final_hand = max(final_hand, 4)  # straight

    for i in range(len(all_cards_no_dupes) - 4):
        if len(set(hand_and_table_dye[i:i+5])) == 1:
            final_hand = max(final_hand, 5)  # flush

    if four_of_a_kind:
        final_hand = max(final_hand, 7)  # four of a kind

    if triplets:
        if pairs:
            final_hand = max(final_hand, 6)  # full house
        else:
            final_hand = max(final_hand, 3)  # three of a kind

    if pairs:
        if len(pairs) > 1:
            final_hand = max(final_hand, 2)  # two pair
        else:
            final_hand = max(final_hand, 1)  # pair



    hand_types = {
        0: "High card.",
        1: "Pair.",
        2: "Two pair!",
        3: "Three of a kind!",
        4: "Straight!",
        5: "Flush!",
        6: "Full house! ( BOAT)",
        7: "Four of a kind!",
        8: "Straight flush!",
        9: "Royal flush!"
    }

    bot_final_hand = 0

    bot_all_cards = bot_hand_unformatted_value + table_unformatted_value
    bot_all_cards_no_dupes = list(set(bot_all_cards))
    bot_all_cards_no_dupes.sort(key=lambda x: card_ranks[x])

    bot_hand_and_table_dye = bot_hand_unformatted_dye + table_unformatted_dye
    bot_hand_and_table_dye.sort()

    bot_card_counts = Counter(bot_all_cards)
    bot_pairs = [card for card, count in bot_card_counts.items() if count == 2]
    bot_triplets = [card for card, count in bot_card_counts.items() if count == 3]
    bot_four_of_a_kind = [card for card, count in bot_card_counts.items() if count == 4]

    if check_straight(bot_all_cards_no_dupes):
        for i in range(len(bot_all_cards_no_dupes) - 4):
            if len(set(bot_hand_and_table_dye[i:i+5])) == 1:
                if all(card in bot_all_cards_no_dupes for card in ["10", "J", "Q", "K", "A"]):
                    bot_final_hand = max(bot_final_hand, 9)  # royal flush
                else:
                    bot_final_hand = max(bot_final_hand, 8)  # straight flush
                break
        else:
            bot_final_hand = max(bot_final_hand, 4)  # straight

    for i in range(len(bot_all_cards_no_dupes) - 4):
        if len(set(bot_hand_and_table_dye[i:i+5])) == 1:
            bot_final_hand = max(bot_final_hand, 5)  # flush

    if bot_four_of_a_kind:
        bot_final_hand = max(bot_final_hand, 7)  # four of a kind

    if bot_triplets:
        if bot_pairs:
            bot_final_hand = max(bot_final_hand, 6)  # full house
        else:
            bot_final_hand = max(bot_final_hand, 3)  # three of a kind

    if bot_pairs:
        if len(bot_pairs) > 1:
            bot_final_hand = max(bot_final_hand, 2)  # two pair
        else:
            bot_final_hand = max(bot_final_hand, 1)  # pair

    if hand_folded:
        print_result("bot", bot_hand_unformatted_value, bot_hand_unformatted_dye, money, raised_sum)
    elif final_hand > bot_final_hand:
        print_result("user", bot_hand_unformatted_value, bot_hand_unformatted_dye, money, raised_sum)
    elif final_hand < bot_final_hand:
        print_result("bot", bot_hand_unformatted_value, bot_hand_unformatted_dye, money, raised_sum)
    else:
        print_result("tie", bot_hand_unformatted_value, bot_hand_unformatted_dye, money, raised_sum)

    print(f"Your current balance is: {money}")
    user_command = handle_user_input("Would you like to play another round? (Yes/No) : ", ["yes", "no"])
    exit_if_no()