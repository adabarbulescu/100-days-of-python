from art import logo
import random

print(logo)


print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
to_guess = random.randint(1, 100)


def guess(no_lives):
    while no_lives >= 0:
        if no_lives == 0:
            print(f"You've run out of guesses. The answer was {to_guess}.")
            break
        try:
            player_guess = int(input("Make a guess: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        if player_guess < to_guess:
            print("Too low.")
            no_lives = no_lives - 1
            guess(no_lives)
        if player_guess > to_guess:
            print("Too high")
            no_lives = no_lives - 1
            guess(no_lives)
        if player_guess == to_guess:
            print(f"You got it. The answer was {to_guess}!")
            break


difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty == "easy":
    no_lives = 10
else:
    no_lives = 5

guess(no_lives)
