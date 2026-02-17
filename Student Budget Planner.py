"""
Student Budget Planner
----------------------
The following application was made in preperation for an assessment
"""

def safe_input(prompt: str) -> str | None:
    try:
        return input(prompt)
    except (KeyboardInterrupt, EOFError):
        print("\n[!] Input cancelled")
        return None
    
def get_valid_string(prompt: str) -> str | None:
    while True:
        text = safe_input(prompt)
        if text is None:
            return None
        cleaned_text = text.strip().title()
        if cleaned_text:
            return cleaned_text
        print("Error: Input can't be empty")

def get_valid_category(prompt: str, categories: list[dict]) -> str | None:
    while True:
        text = safe_input(prompt)
        if text is None:
            return None
        
        cleaned_text = text.strip().title()
        if cleaned_text in categories:
            return cleaned_text
        
        print(f"Error: Category must be one of {categories}")

def get_positive_float(prompt: str) -> float | None:
    while True:
        text = safe_input(prompt)
        if text is None:
            return None
        try:
            value = float(text)
            if value > 0:
                return value
            print("Error: Please enter a number greater than zero")
        except ValueError:
            print("Error: Please enter a valid number")

from datetime import datetime

def get_valid_date(prompt: str) -> str | None:
    while True:
        text = safe_input(prompt)
        if text is None:
            return None
        
        try:
            datetime.strptime(text, "%Y-%m-%d")
            return text
        except ValueError:
            print("Error: Please use the correct format for date")

def calculate_total(expenses: list[dict]) -> float:
    return sum(e["Amount"] for e in expenses)

def add_expense(expenses: list[dict]) -> None:
    print("\n--- Add New Expense ---")
    name = get_valid_string("Enter expense name: ")
    if name is None:
        return
    
    amount = get_positive_float("Enter amount (£): ")
    if amount is None:
        return
    
    date = get_valid_date("Enter date (YYYY-MM-DD): ")
    
    valid_categories = ["Food", "Transport", "Utilities", "Entertainment", "Other"]
    category = get_valid_category("Category: ", valid_categories)
    if category is None:
        return

    expenses.append({
        "Name": name,
        "Amount": amount,
        "Date": date,
        "Category": category
    })

    print("Expense added successfully")

def main() -> None:
    expenses = []

    while True:
        print("\n=== STUDENT BUDGET PLANNER ===")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Calculate Total")
        print("4. Quit")

        choice = safe_input("Pick an option: ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            print(f"\nCurrent Expenses: {expenses}")
        elif choice == "3":
            total = calculate_total(expenses)
            print(f"Total spent: £{total:.2f}")
        elif choice == "4":
            print("Quitting...")
            break
        else:
            print("Invalid option. Please try again")

if __name__ == "__main__":
    main()