from art import logo

alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]


def encrypt(text, shift):
    shifted = ""
    for letter in text:
        if letter in alphabet:
            # ord(letter) - 97: put the letter in the range 0-25
            # + n % 26: add the shift
            #%26: in case the shift leaves the range 0-25
            # +97 readd the unicode order
            # chr(): returns the caracter from unicode index
            shifted += chr((ord(letter) - 97 + shift % 26) % 26 + 97)
        else:
            shifted += letter
    print(f"Here's the {direction}d result: {shifted}")


def decrypt(text, shift):
    shifted = ""
    for letter in text:
        if letter in alphabet:
            shifted += chr((ord(letter) - 97 - shift % 26) % 26 + 97)
        else:
            shifted += letter
    print(f"Here's the {direction}d result: {shifted}")


def caesar(text, shift, direction):
    if direction == "encode":
        encrypt(text, shift)
    else:
        decrypt(text, shift)


print(logo)
continuation = "yes"

while continuation == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if direction not in ("encode", "decode"):
        print("Invalid command. Please try again.")
        continue
    else:
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        caesar(text, shift, direction)
        continuation = input(
            "Type 'yes' if you want to go again. Otherwise type 'no'.\n"
        ).lower()
        if continuation == "yes":
            continue
        else:
            break
