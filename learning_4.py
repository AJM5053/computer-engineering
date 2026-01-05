# The difference between local and global variables
test = "This is global"

def test_scope():
    test = "This is local"
    print(test)

test_scope()
print(test)

# A calculator built using functions
print()
print("---Function Calculator---")

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide (a, b):
    if b != 0:
        return a / b
    else:
        return "Dividing by 0 is impossible!"
    
while True:
    num1 = float(input("Enter your first number: "))
    num2 = float(input("Enter your second number: "))
    operator = input("Pick your operator (+, -< *, /): ")

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

    print(f"Your result is {result}")

    again = input("Would you like to do something else? (yes/no): ")
    if again == "no":
        print("Exiting...")
        break

# Functions that run depending on a choice
print()
def start_scene():
    print("You just got home from work and you're starving. Do you make food or go for a walk? (1 or 2)")
    choice = input("> ")
    if choice == "1":
        food_choice()
    else:
        walk_choice()

def food_choice():
    print("You make yourself a steak and it's lovely. Do you now go to bed or exercise? (1 or 2)")
    choice = input("> ")
    if choice == "1":
        print("You enjoy a long deep sleep")
    else:
        print("You have a good workout session")

def walk_choice():
    print("You go for a long walk but it makes your stomach worse? Do you go to Greggs or Wetherspoons? (1 or 2)")
    choice = input("> ")
    if choice == "1":
        print("You get 3 sausage rolls from Greggs, you fatty!")
    else:
        print("You enjoy a lovely ham & mushroom pizza")

start_scene()