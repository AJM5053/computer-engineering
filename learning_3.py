# A for loop that prints the numbers 1 to 8, each with a string
for i in range(8):
    print(f"This is repetition number {i + 1}")

# A for loop that prints the multiples of 3 up to 30
print()
for i in range(3, 31, 3):
    print(i)

# Totaling the values in a list using a for loop
item_costs = [2.40, 3.99, 5.60, 2.99]
basket_cost = 0

for item_cost in item_costs:
    basket_cost += item_cost

print()
print(f"The total cost of items in the basket is {basket_cost}")

# A for loop that prints a 4x4 grid of asterisks
print()
for row in range(4):
    for column in range(4):
        print('*', end=' ')
    print()

# A for loop that prints a right-angled triangle of asterisks
print()
for r in range(1, 7):
    for c in range(r):
        print('*', end=' ')
    print()

# A while loop for a simple calculator that continues until the user quits
choice = ""

while choice != "3":
    print()
    print("---Welcome to the Calculator---")
    print("1. Multiply")
    print("2. Divide")
    print("3. Quit")
    print()

    choice = input("Please select an option: ")

    if choice == "1":
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        print(f"The result is {num1 * num2}")

    elif choice == "2":
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        print(f"The result is {num1 / num2}")

    elif choice == "3":
        print("Quitting, bye!")

    else:
        print("Invalid input, try again")

# A while loop that asks you to guess a randomly generated number
import random

random_number = random.randint(1, 1000)
print()
print("I've picked a number between 1 and 1000")

while True:
    try:
        guess = int(input("Take a guess: "))
    except ValueError:
        print("INVALID INPUT AGHHHHHHHHHHHHH!!!!!")
        continue

    if guess < random_number:
        print("Too low, try again")

    elif guess > random_number:
        print("Too high, try again")

    else:
        print("You got it!")
        break