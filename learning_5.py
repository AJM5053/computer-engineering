# This is a global variable
my_score = 0

# A function that adds points to a current score
def add_points(current_score):
    new_score = current_score + 20
    return new_score

# Update the global variable using the function
print(f"Currently, my score is {my_score}")
my_score = add_points(my_score)
print(f"Now, my score is {my_score}")

# A function that converts a celsius temprature to fahrenheit
def celsius_to_fahrenheit(celsius_temp):
    fahrenheit = (celsius_temp * 9/5) + 32
    return fahrenheit

"""
My test plan for this function:
1. 5C should give 41F
2. 18C should give 62.6F
3. 25C should give 77F
"""

# Test cases
print()
print("Running temp tests...")
assert celsius_to_fahrenheit(5) == 41
assert celsius_to_fahrenheit(18) == 64.4
assert celsius_to_fahrenheit(25) == 77
print("Temp tests sucessful!")