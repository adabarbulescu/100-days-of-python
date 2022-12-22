print("Welcome to the tip calculator.")
total = float(input("What was the total bill? $"))
no_people = int(input("How many people to split the bill? "))
tip = float(input("What percentage tip would you like to give? "))

paid_each_person = round((total * tip / 100 + total) / no_people, 2)
print(f"Each person should pay: {paid_each_person}$ ")
