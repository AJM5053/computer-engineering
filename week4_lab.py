# This is a number guessing game
secret_number = 79

while True:
    guess = int(input("Guess the secret number: "))

    if guess == secret_number:
        print("You got it, well done!")
        break
    elif guess < secret_number:
        print("Too low, try again")
    else:
        print("Too high, try again")

print()
# This is a function that converts a celsius temprature to fahrenheit
def celsius_to_fahrenheit(celsius_temp):
    fahrenheit = (celsius_temp * 9/5) + 32
    return fahrenheit

c_temp = 30
f_temp = celsius_to_fahrenheit(c_temp)

print(f"{c_temp} celsius is equal to {f_temp} fahrenheit")

print()
# This demonstrates the difference between local and global variables
my_variable =  "This is global"

def test_scope():
    my_variable = "This is local"
    print(my_variable)

test_scope()
print(my_variable)

"""
Python created a local variable inside the function that temporarily shadowed the global one.
The global variable outside the function didn't change therefore the outputs differed.
"""

print()
# This is a calculator built using functions
print("Welcome to the function calculator")

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "You can't divide by 0!"
    
while True:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operator = input("Pick an operator (+, -, *, /)")

    if operator == "+":
        result = add(num1, num2)
    elif operator == "-":
        result = subtract(num1, num2)
    elif operator == "*":
        result = multiply(num1, num2)
    elif operator == "/":
        result = divide(num1, num2)
    else:
        result = "an error!"

    print(f"The result is {result}")

    again = input("Do you want to do another calculation? (yes/no):").lower()
    if again == "no":
        print("Shutting down, bye")
        break

print()
# Refactoring scenes using functions
def start_scene():
    print("You're in your kitchen and start to feel hungry. Do you eat an apple or a taco?")
    choice = input("> ").lower()
    if choice == "apple":
        apple_choice()
    else:
        taco_choice()

def apple_choice():
    print("The apple didn't fill you up. Do you go to subway or go to bed?")
    choice = input("> ").lower()
    if choice == "subway":
        print("You bought a subway but felt annoyed about spending money")
    else:
        print("You enjoyed a long, deep sleep")

def taco_choice():
    print("The taco was delicous. Do you go to the pub or to the library?")
    choice = input("> ").lower()
    if choice == "pub":
        print("You have a fun night with your friends")
    else:
        print("You get a lot of studying done")

start_scene()