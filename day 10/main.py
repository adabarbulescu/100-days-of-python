from art import logo


def addition(n1, n2):
    return n1 + n2


def multiplication(n1, n2):
    return n1 * n2


def division(n1, n2):
    return n1 / n2


def substraction(n1, n2):
    return n1 - n2


operations = {"+": addition, "-": substraction, "/": division, "*": multiplication}


def calculator():
    print(logo)

    continuation = "yes"
    while True:
        try:
            number = float(input("What's the first number?: "))
            break
        except ValueError:
            print("Please enter a valid number.")
            continue
    while continuation == "yes":
        operation_symbol = input("+\n-\n*\n/\n Pick an operation: ")
        if operation_symbol not in ("+", "-", "*", "/"):
            print("Invalid command. Please try again.")
            continue
        try:
            number2 = float(input("What's the next number?: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        calculation = operations[operation_symbol]
        result = calculation(number, number2)
        print(f"{number} {operation_symbol} {number2} = {result}")
        continuation = input(
            f"Type 'yes' if you want to continue with {result}, 'no' to start a new calculation and 'quit' to exit the programme.\n"
        ).lower()
        if continuation not in ("yes", "no", "quit"):
            print("Incorrect command. Please try again.")
            continue
        if continuation == "yes":
            number = result
        elif continuation == "no":
            calculator()
        else:
            break


calculator()
