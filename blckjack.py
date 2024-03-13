print("Hey! Welcome to the blackjack game (made by UtCurse)")

import random

cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack=10", "Queen=10", "King=10", "Ace=11/1"]

# Creating an empty deck of cards...
deck = []
for card in cards:
    deck.append(f"{card}")

# This method will randomly shuffle the deck...
random.shuffle(deck)

# Creating a dictionary to map card strings to their numerical values
card_values = {
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
    "10": 10, "Jack=10": 10, "Queen=10": 10, "King=10": 10, "Ace=11/1": 11
}

def score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(computer_score,user_score):
    if user_score==computer_score:
        return "draw😶"
    elif computer_score==0:
        return "loose opponent has blackjack😑"
    elif user_score==0:
        return "win bcz of blackjack😍"
    elif user_score>21:
        return "you Loose,your score went over 21😫"
    elif computer_score>21:
        return "opponent went over you win🤐"
    elif user_score>computer_score:
        return "you win🙂"
    else:
        return "you loose😑"

# User & computer
user = []
computer = []
is_game_over = False
# Append-: adds a single item to the end of the existing list.
for i in range(2):
    user.append(card_values[deck.pop()])
    computer.append(card_values[deck.pop()])
while not is_game_over:

    user_score = score(user)
    computer_score = score(computer)
    print(f"Your cards {user} and your score {user_score}")
    
    if user_score == 0 or computer_score == 0 or user_score > 21:
        is_game_over = True
    else:
        deal=input("Type 'y'  to get another card,type 'n' to pass...")
        if deal=='y':
            user.append(card_values[deck.pop()])
        else:
            is_game_over=True
while computer_score!=0 and computer_score<17:
    computer.append(card_values[deck.pop()])
    computer_score=score(computer)

print(f"your final cards are {user} and score is{user_score}")
print(f"computer final cards are {computer} and score is{computer_score}")
print(compare(user_score,computer_score))