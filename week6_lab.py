player_health = 100

# Add a current health parameter
def take_damage(current_health):
    """
    This subtracts 20 from the given health value and returns the new health
    """
    new_health = current_health - 20
    print("\nPlayer took damage!")
    # Return the calculated value
    return new_health

player_health = take_damage(player_health)
print(f"Player health is {player_health}")

total_actions = 0
player_level = 1


print()
# A while loop that runs for levels 1, 2, and 3
while player_level < 4:
    print(f"Processing Level {player_level}...")

    # A nester for loop that runs player_level times
    for action in range(player_level):
        total_actions += 1

    player_level += 1

print(f"Total actions: {total_actions}")

log_data = "Score:Player_1:2500"

# Use .split() to break the string into a lost at each :
parsed_data = log_data.split(":")

# Print the whole list
print(f"\nParsed list: {parsed_data}")

# Access the item at index 1
print(f"You are: {parsed_data[1]}")

# Access the item at index 2
print(f"Your score: {parsed_data[2]}")

print()
# Create parallel lists
questions = ["What's 5+9?", "What's the capital of Italy?", "What keyword defines a function?"]
answers = ["14", "Rome", "def"]

# Starting score
score = 0

# Loop using range(len(questions))
for i in range(len(questions)):
    # Ask the question using the index
    print(f"Question {i + 1}:")
    user_answer = input(questions[i] + " ")

    # Check the answer and use .lower to make the check case insensitive
    if user_answer.lower() == answers[i].lower():
        print("Correct!")
        score += 1
    else:
        print(f"Incorrect! The answer was {answers[i]}")

# Print the final score
print(f"\nQuiz complete! You scored {score}/{len(questions)}")

# Start with an empty dictionary
phonebook = {}

# Add contacts
phonebook["Alice"] = "07219675446"
phonebook["Bob"] = "07992407532"

print("\n--- Phonebook Search ---")

# Ask for a name to look up
name_to_find = input("Who do you want to find? ")

# Retrieve the value using the key
number = phonebook.get(name_to_find)

if number: # This checks if number exists
    print(f"The number for {name_to_find} is {number}")
else:
    print(f"Sorry, {name_to_find} isn't in the phonebook")

# Add a new contact
phonebook["Charlie"] = "07243994115"

# Loop and print all contacts
print("\n--- Full Phonebook ---")
for name, number in phonebook.items():
    print(f"{name}: {number}")