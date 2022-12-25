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
        return "Win with a Blackjack."
    elif computer_score == 0:
        return "You lose. Opponent has Blackjack."
    elif player_score > 21:
        return "You went over. You lose"
    elif computer_score > 21:
        return "You win. Opponent went over."
    elif player_score > computer_score:
        return "You win."
    else:
        return "You lose."


def check_if_over(player, computer):
    if (
        (calculate_score(player)) == 0
        or calculate_score(computer) == 0
        or calculate_score(player) > 21
    ):
        return 1


def game():
    player = []
    computer = []
    print(logo)
    continuation = "y"

    # de aici incepe while ul
    while continuation == "y":
        continuation = input(
            "Do you want to play a game of Blackjack? Type 'y' or 'n': "
        )
        if continuation == "n":
            break
        else:
            for i in range(2):
                player.append(dealcards())
                computer.append(dealcards())
            print(f"Your cards: {player}, current score: {calculate_score(player)}")
            print(f"Computer's first card: {computer[0]}")
            if check_if_over(player, computer) == 1:
                # the game ends
                # print your cards
                # deal computer more cards
                # compare and choose a winner
                break

            else:
                # the game continues
                continuation = input("Type 'y' to get another card, type 'n' to pass: ")
                if continuation == "n":
                    break
                else:
                    player.append(dealcards())
                    computer.append(dealcards())

                    if check_if_over(player, computer) == 1:
                        break


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    game()
