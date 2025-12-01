"""
This file will be for using while loops and for loops, both introduced in week 3
"""
for i in range(10): # This prints the numbers 1 to 10 with a string
    print(f"This is repetition number {i + 1}")

print()
for i in range(2, 20, 2): # This prints the even numbers between 1 and 20
    print(i)

print()
card_payments = [6.99, 4.20, 10.00, 8.99, 13.48]
total_card_payments = 0

for card_payment in card_payments: # This calculates the total of the card payments
    total_card_payments += card_payment

print(f"The total of the card payments is {total_card_payments}")

print()
for row in range(5): # This prints a 5x5 grid of asterisks
    for column in range (5):
        print('*', end=' ')
    print()

print()
for r in range(1, 6): # This prints a right-angled triangle of asterisks
    for c in range(r):
        print('*', end=' ')
    print()

choice = ''

while choice != 'q': # This is a simple calculator that continues until the user quits
    print("---Calculator Menu---")
    print("1. Add")
    print("2. Subtract")
    print("q. Quit")

    choice = input("Please select an option: ")

    if choice == '1':
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        print(f"The result is: {num1 + num2}")

    elif choice == '2':
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number:"))
        print(f"The result is: {num1 - num2}")

    elif choice == 'q':
        print("Closing the calculator, bye!")

    else:
        print("Invalid choice, try again")

import random

print()
random_number = random.randint(1, 100) # This is a number guessing game
print("I'm thinking of a number between 1 and 100")

while True:
    try:
        guess = int(input("Have a guess: "))
    except ValueError:
        print("Invalid input, try again.")
        continue

    if guess < random_number:
        print("Too low, try again.")

    elif guess > random_number:
        print("Too high, try again.")

    else:
        print("You got it!")
        break