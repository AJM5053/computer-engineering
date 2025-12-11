# This function deposits an amount to a balance
def deposit(balance, amount):
    return balance + amount

# This function withdraws an amount from a balance
def withdraw(balance, amount):
    if amount <= balance:
        return balance - amount
    else:
        print("Not enough funds")
        return balance

# This main function will run the banking system
def main():
    balance = 100
    balance = deposit(balance, 170)
    balance = withdraw(balance, 80)
    print("\nYour final balance is", balance)

main()

message = "Glynn is a fool"

print()
# This slices from index 0 up to but not including index 5
name = message[0:5]
print(name)

# This slices from index 11 all the way to the end
insult = message[11:]
print(insult)

print()
# This splits the string at each comma into a list
my_data = "Adam,Marsh,22"
my_list = my_data.split(",")
print(my_list)

print()
greeting = "Hello there"
print(greeting.find("there")) # Outputs 6
print(greeting.find("shush")) # Outputs -1

print()
names = ["Adam","Sophia","Alex"]
print(names[1]) # Outputs Sophia
names[2] = "Erin" # Alex is replaced
names.append("Zahari") # Zahari is put on the end of the list
print(names)

scores = [77,89,55,94]
total_score = 0

print()
# This loops for every score to add them all to the total score
for score in scores:
    print(f"Processing score: {score}")
    total_score += score

print(f"\nThe total socre is {total_score}")

print()
student = {"Name":"Adam","Age":20,"Commutes":False,"Degree":"Computer Engineering"}
student["Age"] = 22 # Modifies a dictionary value
student["ID"] = 26470012 # Adds a new key-value pair

# This loop outputs the entire dictionary
for key, value in student.items():
    print(f"{key}: {value}")