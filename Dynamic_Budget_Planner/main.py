"""
This is the program's "brain." It handles user input, menu navigation, and calls functions from other files.
Example: Display menu options like "Add Expense" or "View Expenses" and call the respective function from `expense_handler.py`.
"""
while True:
    print("\nHello, what are you here for?")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Update Expense")
    print("4. Delete Expense")
    
    try:
        choice = int(input("Enter your choice(1-4)"))
        if 1 <= choice <= 4:
            break #valid input exitsing the loop
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
    except ValueError:
        print("Invalid input. Please enter a number!")
        
    if choice == ['1', 'add expense'.lower()]:
        