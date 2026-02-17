"""
Home Security System
--------------------
This code represents logic that can be used in a home security system.
Factorts impacting if the alarm goes off are an open door (A), motion detected (B), and system armed (C).
"""

def get_input(prompt):
    """
    This ensures only inputs of 1 of 0 are accepted from the user.
    """
    while True:
        try:
            value = int(input(prompt))
            if value in (0, 1):
                return value
            else:
                print("Error: Please enter 1 or 0.")
        except ValueError:
            print("Error: Please enter 1 or 0.")

def alarm_test():
    """
    This applies the Boolean logic to determine if the alarm is triggered.
    """
    A = get_input("\nIs the door open? (1 for yes, 0 for no): ")
    B = get_input("Is motion detected? (1 for yes, 0 for no): ")
    C = get_input("Is the security system armed? (1 for yes, 0 for no): ")

    if (A == 1 or B == 1) and C == 1:
        print("Alarm triggered!")
    else:
        print("No alarm, system is safe.")

def main():
    while True:
        print("\n==== HOME SECURITY SYSTEM ====")
        print("1. Start Alarm Test")
        print("2. Exit")

        try:
            choice = int(input("Select an option: "))

            if choice == 1:
                alarm_test()

            elif choice == 2:
                print("\nExiting...")
                break

            else:
                print("Error: Please enter 1 or 2.")

        except ValueError:
            print("Error: Please enter 1 or 2.")

if __name__ == "__main__":
    main()