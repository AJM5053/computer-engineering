entry = input("Make an entry to your file: ")

# Append is good practice as it preserves history
with open("Entries.txt", "a") as f:
    # Add the newline character manually
    f.write(entry + "\n")

print("\nEntry saved")

print("\n--- Entries File ---")
try:
    with open("Entries.txt", "r") as f:
        # Read all previous entries to this file
        content = f.read()
        print(content)
except FileNotFoundError:
    print("That file doesn't exist")

import csv

# This data will be saved to a CSV file
sprints = {
    "Sonic": [701, 697, 714],
    "Tails": [94, 103, 92],
    "Knuckles": [85, 93, 79],
    "Shadow": [688, 695, 703]
}

with open("Top_speeds.csv", "w", newline="") as f:
    writer = csv.writer(f)
    # This will be the header
    writer.writerow(["Name", "Sprint1", "Sprint2", "Sprint3"])
    # Now the data is needed
    for name, speeds in sprints.items():
        # Name and sprints must share a row
        row = [name] + speeds
        writer.writerow(row)

print("\nData saved to CSV file")

print("\n--- Speed Averages ---")

with open("Top_speeds.csv", "r") as f:
    reader = csv.reader(f)
    # Skip the header row
    header = next(reader)

    for row in reader:
        name = row[0]
        # Convert the speeds from strings to integers
        speeds = [int(s) for s in row[1:]]
        # Now the average calculation
        average = sum(speeds) / len(speeds)
        # Format to 1 decimal place
        print(f"{name} has an average speed of {average:.1f}mph")

import json

bag = [ # A list of dictionaries
    {"Item": "steak", "Cost": 6.49, "Importance": "Medium"},
    {"Item": "lucozade", "Cost": 2.55, "Importance": "Low"},
    {"Item": "waffles", "Cost": 2.19, "Importance": "High"},
    {"Item": "eggs", "Cost": 1.53, "Importance": "Medium"}
]

# Save this bag as a JSON file
with open("groceries.json", "w") as f:
    json.dump(bag, f, indent=4)

# Now load that file
with open("groceries.json", "r") as f:
    bag_data = json.load(f)

print("\nHere's your bag:\n", bag_data)