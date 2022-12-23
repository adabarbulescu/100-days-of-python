import random

game_choices = {
    0: """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
    1: """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
""",
    2: """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""",
}


def printlose(comp_choice):
    print("Computer chose:")
    print(game_choices[comp_choice])
    print("You lose.")


def printwin(comp_choice):
    print("Computer chose:")
    print(game_choices[comp_choice])
    print("You win.")


def printdraw(comp_choice):
    print("Computer chose:")
    print(game_choices[comp_choice])
    print("It's a draw!")


print("Welcome to Rock - Paper - Scissors Game!")
while True:
    user = input(
        "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"
    )

    if user not in ("0", "1", "2"):
        print("Invalid command. Please try again.")
        continue
    else:
        user = int(user)
        break
comp_choice = random.randint(0, 2)
print(game_choices[user])
if user == 0 and comp_choice == 1:
    printlose(comp_choice)
elif user == 0 and comp_choice == 2:
    printwin(comp_choice)
elif user == 1 and comp_choice == 2:
    printlose(comp_choice)
elif user == 1 and comp_choice == 0:
    printwin(comp_choice)
elif user == 2 and comp_choice == 0:
    printlose(comp_choice)
elif user == 2 and comp_choice == 1:
    printwin(comp_choice)
else:
    printdraw(comp_choice)