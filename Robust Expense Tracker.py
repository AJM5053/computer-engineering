"""
ROBUST EXPENSE TRACKER
----------------------
This has been built in peperation for the portfolio task 1 assessment.
The code below is inspired by code provided by Saad.
"""

def safe_input(prompt):
    """
    This custom input function handles user interruptions safely.
    """
    # A try block is used because the standard input() function is dangerous.
    try:
        # Attempt to read input from the user normally.
        return input(prompt)
    
    # If the user presses Ctrl+C or Ctrl+D...
    except (KeyboardInterrupt, EOFError):
        # ...we catch the error here so the program doesn't crash.
        print("\n[!] Input cancelled by user.")

        # None is returned to tell other functions to stop what they're doing.
        return None
    
def get_valid_string(prompt):
    """
    This asks the user for a string and ensures it isn't empty.
    It's used for expense name.
    """
    # Start an infinite loop. We'll only break out when we get valid input.
    while True:
        # Call the safe_input function instead of using the standard input.
        user_input = safe_input(prompt)

        # Check if the user pressed Ctrl+C? (Is the input None?)
        if user_input is None:
            return None # Exit the function and pass the signal up.
        
        # Sanitize by removing any spaces from the start and end of the string.
        cleaned_input = user_input.strip()

        # Validate by checking if the string is empty after cleaning.
        if cleaned_input == "":
            # Complain to the user if it's empty.
            print("Error: Input can't be empty. Please try again.")
            # Use continue to jump back to the start of the loop to ask again.
            continue

        # The input is valid if this line is reached so return it.
        return cleaned_input
    
def get_positive_float(prompt):
    """
    This asks for a number and ensures it's a valid decimal greater than zero.
    It's used for expense amount.
    """
    while True:
        # Get the raw string input safely.
        user_input = safe_input(prompt)

        # Check for cancellation.
        if user_input is None:
            return None
        
        # Attempt to convert the string to a float.
        try:
            # This line will crash if the user enters invalid input like "abc"
            value = float(user_input)

        # Catch the ValueError if conversion failed.
        except ValueError:
            # Tell the user what went wrong without crashing.
            print(f"Error: {user_input} isn't a valid number. Please try again.")
            # Loop again to give them another chance.
            continue

        # Check that the number is positive.
        if value <= 0:
            print("Error: Input must be greater than zero. Please try again.")
            continue

        # Return the valid number.
        return value

def get_choice(prompt, options):
    """
    This forces the user to pick from a specific list of options.
    It's used for expense category.
    """
    while True:
        # Get input safely.
        user_input = safe_input(prompt)

        if user_input is None:
            return None
        
        # Sanitize by converting to title case so it looks nice.
        cleaned_input = user_input.strip().title()

        # Validate by checking if their input exists in our allowed list.
        if cleaned_input in options:
            return cleaned_input
        
        # If not, show the valid options and loop again.
        print(f"Error: Invalid choice. Your options are {', '.join(options)}")

def add_expense_feature(expense_list):
    """
    This is the logic for the add expense menu option.
    """
    print("\n--- Add New Expense ---")

    # Get the name using the helper function. It handles the loops and errors.
    name = get_valid_string("Enter expense name: ")

    # If name is None, it means the user hit Ctrl+C so stop adding.
    if name is None:
        return
    
    # Get the amount. This guarantees we get a valid positive number.
    amount = get_positive_float("Enter amount (£): ")
    if amount is None:
        return
    
    # Get the category. We define exactly what categories are allowed for this task.
    valid_categories = ["Food", "Transport", "Utilities", "Entertainment", "Other"]
    category = get_choice("Enter category: ", valid_categories)
    if category is None:
        return
    
    # Save the data by creating a dictionary to group these pieces of data together.
    expense_record = {
        "Name": name,
        "Amount": amount,
        "Category": category
    }

    # Add this diectionary to the main list of expenses.
    expense_list.append(expense_record)

    # Confirm success to the user.
    print(f"Success: Added {name} for £{amount:.2f} in {category}")

def main():
    """
    This is the main program loop
    """
    # Create an empty list to store all our expenses
    my_expenses = []
    
    # This loop keeps the program running until the user chooses to quit
    while True:
        print("\n=== EXPENSE TRACKER MENU ===")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Quit")

        # We reuse safe_input here so the meun doesn't crash on Ctrl+C
        choice = safe_input("Select an option: ")

        # Basic menu logic
        if choice == "1":
            add_expense_feature(my_expenses)

        elif choice == "2":
            # A simple print to show this works
            print(f"\nCurrent Expenses: {my_expenses}")

        elif choice == "3" or choice is None:
            # Quit cleanly
            print("Quitting...")
            break

        else:
            print("Invalid selection. Please try again.")

# This line ensures we're runnung the file directly, not importing it
if __name__ == "__main__":
    main()