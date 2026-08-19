# This is code that follows a good pattern when it comes to variable scope
player_score = 0 # This is global

def add_points(current_score): # Accept a parameter
    """ Adds 10 points to a given score and returns the new score """
    new_score = current_score + 10
    print(f"Inside the function, the new score is {new_score}")
    return new_score # Return the new value

print(f"\nOutside the function, the player score is {player_score}")

# Capture the returned value and update the global variable
player_score = add_points(player_score)

print(f"Outside the function, the player score is {player_score}")

"""
This is pseudocode for a divide(a, b) function

START
  FUNCTION divide(a, b):

    // Check for the error condition
    IF b is equal to 0:
      PRINT "Error: Cannot divide by zero"
      RETURN None
    ELSE:
      // Perform the calculation
      result = a / b
      RETURN result
    END IF

  END FUNCTION
END
"""

# This is a function that converts a celsius temprature to fahrenheit
def celsius_to_fahrenheit(celsius_temp):
    fahrenheit = (celsius_temp * 9/5) + 32
    return fahrenheit

"""
My test plan for celsius_to_fahrenheit:
1. Test freezing point: 0C should be 32F
2. Test boiling point: 100C should be 212F
3. Test room temperature: 21C should be 70F
4. Test a negative value: -10C should be 14F
"""

# Unit tests
print("\nRunning temperature tests...")
assert celsius_to_fahrenheit(0) == 32
assert celsius_to_fahrenheit(100) == 212
assert celsius_to_fahrenheit(21) == 69.8
assert celsius_to_fahrenheit(-10) == 14
print("Temperature tests sucessful!")

def calculate_factorial(n):
   """Calculates the factoral of a positive integer"""
   total = 1 # FIX: Set to 1 instead of 0
   for i in range(1, n + 1):
      total = total * i # This logic is now correct                 
   return total
   
# Unit tests
print("\nRunning factoral tests...")
assert calculate_factorial(5) == 120
assert calculate_factorial(1) == 1
assert calculate_factorial(0) == 1
print("Factoral tests sucessful!")

result = calculate_factorial(5)
print(f"\nThe factoral of 5 is {result}") # Now correctly prints 120
