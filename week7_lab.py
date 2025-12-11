entry = input("\nPut something in your diary: ")

# Append is better for diaries as it perserves history
with open("diary.txt", "a") as f:
    # The newline character must be added manually
    f.write(entry + "\n")

print("\nEntry saved")

print("\n--- My Diary ---")
try:
    with open("diary.txt", "r") as f:
        content = f.read() # This reads all the previous entries to the diary file
        print(content)
except FileNotFoundError:
    print("No diary file found")

import csv

# Data to save
grades = {
    "Alice": [85, 90, 92],
    "Bob": [78, 81, 85],
    "Charlie": [95, 100, 98]
}

with open("grades.csv", "w", newline="") as f:
    writer = csv.writer(f)
    # Write the header
    writer.writerow(["Name", "Score1", "Score2", "Score3"])
    # Write the data
    for name, scores in grades.items():
        # Combine name and scores into one row
        row = [name] + scores
        writer.writerow(row)

print("Grades saved to grades.csv")

print("\n--- Student Averages ---")

with open("grades.csv", "r") as f:
    reader = csv.reader(f)
    # Skip the header row
    header = next(reader)

    for row in reader:
        name = row[0]
        # Convert string scores into integers
        socres = [int(s) for s in row[1:]]
        # Calculate the average
        average = sum(socres) / len(scores)
        # Format to 1 decimal place
        print(f"{name}: {average:.1f}")

import json

bag = [ # The list of dictionaries
    {"Item": "Notepad", "Cost": 5.99, "Importance": "High"},
    {"Item": "Pencil case", "Cost": 14.50, "Importance": "High"},
    {"Item": "Headphones", "Cost": 32.00, "Importance": "Medium"},
    {"Item": "Water bottle", "Cost": 1.40, "Importance": "Low"}
]

# Save as a json file
with open("save_bag.json", "w") as f:
    json.dump(bag, f, indent=4)

# Load the json file
with open("save_bag.json", "r") as f:
    loaded_data = json.load(f)

print("\nData loaded successfully:\n", loaded_data)