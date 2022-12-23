from hangman_words import word_list
from hangman_art import logo, stages
import random
from replit import clear

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6
print(logo)


# Create blanks
display = []
already_guessed = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    clear()

    if guess in already_guessed:
        print(f"{' '.join(display)}")
        print(stages[lives])
        print(f"You've already guessed with the letter '{guess}', pick another letter.")
    else:
        already_guessed.append(guess)

        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter

        print(f"{' '.join(display)}")

        if "_" not in display:
            end_of_game = True
            print("\nGeninus, genius, genius! You won!")
            # print(logo2)

        if guess not in chosen_word:
            lives -= 1

        if not end_of_game:
            print(stages[lives])
            if guess not in chosen_word:
                print(f"'{guess}' is not in the word, you lost 1 life.")

        if lives == 0:
            end_of_game = True
            print("The man has been hung, you lose.")
            print(f"\nThe word was '{chosen_word}'")
