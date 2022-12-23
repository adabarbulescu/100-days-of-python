from replit import clear
from art import logo


moreusers = "yes"
Bidders = {}


def find_highest(bids):
    winner = 0
    name = ""
    for key, value in Bidders.items():
        if value >= winner:
            winner = value
            name = key

    print(f"The winner is {name} with a bid of ${winner}.")


while moreusers == "yes":
    clear()
    print(logo)
    print("Welcome to the secret auction program.")
    name = input("What is your name? ")
    try:
        bid = int(input("What is your bid? $"))
    except ValueError:
        print("Invalid command. Please try again.")
        continue
    Bidders[name] = bid
    moreusers = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
    if moreusers in ("yes", "no"):
        if moreusers == "yes":
            clear()
        else:
            clear()
            find_highest(bid)
    else:
        print("Invalid command. Please try again.")
        continue
