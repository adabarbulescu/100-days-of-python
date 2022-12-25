import random
from art import logo


def welcome_message():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")


def choose_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "easy":
        return 10
    else:
        return 5


def get_guess():
    while True:
        try:
            guess = int(input("Make a guess: "))
            return guess
        except ValueError:
            print("Invalid input. Please enter a number.")


def evaluate_guess(guess, to_guess):
    if guess < to_guess:
        print("Too low.")
        return False
    if guess > to_guess:
        print("Too high")
        return False
    if guess == to_guess:
        print(f"You got it. The answer was {to_guess}!")
        return True


def game_over(no_lives):
    print(f"You've run out of guesses. The answer was {to_guess}.")


def play_game(no_lives):
    to_guess = random.randint(1, 100)
    while no_lives >= 0:
        guess = get_guess()
        if evaluate_guess(guess, to_guess):
            return
        no_lives = no_lives - 1
    game_over(no_lives)


def main():
    welcome_message()
    no_lives = choose_difficulty()
    play_game(no_lives)


main()
