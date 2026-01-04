# Convert a temp from Celsius to Fahrenheit
celsius = 32
fahrenheit = (celsius*9/5) + 32
rounded = int(round(fahrenheit))
print(f"If the temp in celsius is {celsius} then the temp in fahrenheit is {rounded}")

# These are all the data types
my_string = "I like sonic"
my_int = 268
my_float = 2.591
my_bool = True

print()
print(f"{my_string} is a string")
print(f"{my_int} is an integer")
print(f"{my_float} is a float")
print(f"{my_bool} is a boolean")

print()
print(type(my_string))
print(type(my_int))
print(type(my_float))
print(type(my_bool))

# Different ways to print strings with variables
name = "Adam"
town = "Ormskirk"

method1 = ("My name is " + name + " and I live in " + town)
method2 = ("My name is {} and I live in {}".format(name, town))
method3 = (f"My name is {name} and I live in {town}")

print()
print(method1)
print(method2)
print(method3)

# A while loop that won't break until a number is entered
print()
while True:
    try:
        cars = int(input("How many cars do you own? "))
        break
    except ValueError:
        print("Only enter a number")
if cars < 0:
    print("That's impossible, don't be stupid")
elif cars == 0:
    print("You must use public transport often then")
elif cars == 1:
    print("That's normal, look after it")
elif cars == 2:
    print("Nice, you must have a good job")
else:
    print("Wow, you must be rich")