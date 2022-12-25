import random
from art import logo
from replit import clear

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def dealcards():
    card = random.choice(cards)
    return card


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(player_score, computer_score):
    if player_score > 21 and computer_score > 21:
        return "You went over. You lose"
    if player_score == computer_score:
        return "Draw."
    elif player_score == 0:
        player_score = 21
        return "Win with a Blackjack."
    elif computer_score == 0:
        computer_score = 21
        return "You lose. Opponent has Blackjack."
    elif player_score > 21:
        return "You went over. You lose"
    elif computer_score > 21:
        return "You win. Opponent went over."
    elif player_score > computer_score:
        return "You win."
    else:
        return "You lose."


def check_if_over(player_score, computer_score):
    if player_score == 0 or computer_score == 0 or player_score > 21:
        return 1


def game():
    player = []
    computer = []
    print(logo)
    continuation = "y"
    for i in range(2):
        player.append(dealcards())
        computer.append(dealcards())

    while continuation == "y":
        player_score = calculate_score(player)
        computer_score = calculate_score(computer)

        print(f"Your cards: {player}, current score: {player_score}")
        print(f"Computer's first card: {computer[0]}")
        if check_if_over(player_score, computer_score) == 1:
            continuation = "n"
            break

        else:
            # the game continues
            dealing = input("Type 'y' to get another card, type 'n' to pass: ")
            if dealing == "y":
                player.append(dealcards())
            else:
                continuation = "n"
    while computer_score != 0 and computer_score < 17:
        computer.append(dealcards())
        computer_score = calculate_score(computer)

    print(f"Your final hand: {player}, final score: {player_score}")
    print(f"Computer's final hand: {computer}, final score: {computer_score}")
    print(compare(player_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    clear()
    game()
