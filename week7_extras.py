# The with statement guarantees the file will be closed, even if errors occur
with open("my_file.txt", "w") as f:
    # f is our file handle whereas w is the mode
    f.write("This is a test sentence")
    # The file is automatically closed at this point

try: # Now to read the file I just made
    with open("my_file.txt", "r") as f:
        content = f.read()
        print()
        print(content)
except FileNotFoundError:
    print("\nYour file couldn't be found")

# Writing multiple lines to a .txt file
data_to_save = ["First line", "Second line", "Third line"]
with open("log.txt", "w") as f:
    for line in data_to_save:
        f.write(line + "\n") # Don't forget the newline character

# Reading those lines
with open("log.txt", "r") as f:
    lines = f.readlines()
    # Stripping the \n
    clean_lines = [line.strip() for line in lines]
    print()
    print(clean_lines)

import csv

# Writing to a .csv file
gradebook = {"Ben":[85,90], "Sarah":[92,88]}

with open("grades.csv", "w", newline="") as f:
    writer = csv.writer(f)
    for student, scores in gradebook.items():
        writer.writerow([student] + scores)

# Reading from a .csv file
new_gradebook = {}
with open("grades.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        # A row is always a list of strings
        new_gradebook[row[0]] = [int(s) for s in row[1:]]

print()
print(new_gradebook)

import json

example_data = [
    {"item":"Sword","Price":40},
    {"item":"Potion","Price":10}
]

# Writing to a .json file
with open("data.json", "w") as f:
    json.dump(example_data, f, indent=4) # This makes it readable

# Reading from a .json file
with open("data.json", "r") as f:
    loaded_data = json.load(f)

print()
print(loaded_data == example_data) # True

def load_data():
    try:
        with open("data.json", "r") as f:
            return json.load(f) # Load data if the file exists
    except FileNotFoundError:
        print("No data found, starting fresh")
        return []
    except json.JSONDecodeError:
        print("Data is corrupt, starting fresh")
        return []

# Program start
example_data = load_data()
print()
print(example_data)