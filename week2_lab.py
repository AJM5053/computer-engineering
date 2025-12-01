"""
This program converts a temperature from Celsius to Fahrenheit
"""
Celsius = 15
# This number represents the temprature in celsius inputted by the user
Fahrenheit = (Celsius*9/5) + 32
# This is the formula that converts the input in celsius to fahrenheit which is stored as a variable
rounded = int(round(Fahrenheit))
print(f"If the tempratuire in celsius is {Celsius} then the temprature in fahrenheit is {rounded}")
# This prints a statement that says what the fahrenheit will be depending on the celsius
"""
The value of the celsius variable directly impacts the value of the fahrenheit variable. If the celsius changes to a higher
number, the fahrenheit becomes higher. If the celsius changes to a lower number, the fahrenheit becomes lower. The fahrenheit
varable gives a float each time so I'm using the rounded variable which gives the rounded integer of the fahrenheit varable
"""
my_string = "I'm from Widnes"
my_int = 8239
my_float = 64.91
my_bool = False
print(f'"{my_string}" is a string')
print(f'"{my_int}" is an integer')
print(f'"{my_float}" is a float')
print(f'"{my_bool}" is a boolean')
print(type(my_string))
print(type(my_int))
print(type(my_float))
print(type(my_bool))
"""
Python allows you to change a variable type later because it is a dynamically typed language. This means Python doesn't 
lock in a variable to a specific type when you first assign it a value. Instead, it focuses on the value itself, not the variable type
"""
Name = "Adam"
Course = "Computer Engineering"
Movie = "World War Z"
Greeting = ("My name is " + Name + ". I study " + Course + " and my favourite movie is " + Movie)
print(Greeting)
Greeting2 = "My name is {}. I study {} and my favourite movie is {}".format(Name, Course, Movie)
print(Greeting2)
print(f"My name is {Name}. I study {Course} and my favourite movie is {Movie}")
while True:
    try:
        age = int(input("Please enter your age: "))
        break
    except ValueError:
        print("You must enter a number")
if age < 0:
    print("Stop being silly")
elif age < 13:
    print("You're a child")
elif age < 18:
    print("You're a teenager")
elif age < 70:
    print("You're an adult")
elif age < 110:
    print("You don't have much time left")
else:
    print("You're lying")