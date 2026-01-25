player_health = 150
print(f"Your starting health is {player_health}")

# A function that subtracts 30 from the given health and returns the new health
def take_damage(current_health):
    new_health = current_health - 30
    print("You took damage!")
    return new_health

player_health = take_damage(player_health)
print(f"Your health is now {player_health}")

print()
actions = 0
level = 1

# This while loop runs for levels 1, 2, and 3
while level < 4:
    print(f"Processing level {level}...")

    # A nested loop that runs level times
    for action in range(level):
        actions += 1

    level += 1

print(f"Actions performed: {actions}")

print()
my_data = "Age:Adam:22"
print(f"My messy data is {my_data}")

# Splitting a string
print()
parsed_data = my_data.split(":")
print(f"My parsed data is {parsed_data}")

# Access the item at index 1
print()
print(f"My name is {parsed_data[1]}")

print()
questions = ["What programming language is this?", "Which country is Oslo the capital of?", "What's 12*5?"]
answers = ["Python", "Norway", "60"]
score = 0

# A for loop that goes through a list of questions to ask using indexing
for i in range(len(questions)):
    print(f"Question {i + 1}:")
    user_answer = input(questions[i] + " ")
    
    # Checking the answers and allowing them to be case insensitive
    if user_answer.lower() == answers[i].lower():
        print("Correct!")
        score += 1
    else:
        print(f"Incorrect! The answer was {answers[i]}")

print()
print(f"Quiz complete! You answered {score}/{len(questions)} correctly")

# Creating a dictionary and looking people up in it
phonebook = {}
phonebook["Jack"] = "07262543890"
phonebook["Lucy"] = "07854344684"
phonebook["Rosie"] = "07882446785"

print()
print("--- Phonebook Search ---")
name_to_find = input("Who do you need to contact? ")
number = phonebook.get(name_to_find)

# Check if the number exists
if number:
    print(f"The number for {name_to_find} is {number}")
else:
    print(f"Sorry, {name_to_find} isn't in the phonebook")

# Looping to print all contacts
print()
print("--- Full Phonebook ---")
for name, number in phonebook.items():
    print(f"{name}: {number}")