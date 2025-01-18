"""
This is the program's "brain." It handles user input, menu navigation, and calls functions from other files.
Example: Display menu options like "Add Expense" or "View Expenses" and call the respective function from `expense_handler.py`.
"""

from utils import is_valid_amount, is_valid_category, is_valid_date, is_valid_description
from expense_handler import ExpenseEntry

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
        
    validate_data = {}

    questions = {
        "amount": "Enter the amount: ",
        "category": "Enter the category: ",
        "date": "Enter the date (DD-MM-YYYY): ",
        "description": "Enter a brief description: "
    }

    # loop through each field input and validating it
    for key, question in questions.items():
        while True:
            user_input = input(question)
            if key == 'amount':
                if is_valid_amount(user_input):
                    validate_data[key] = float(user_input) # format and store
                    break
                else:
                    print("Invalid amount. Please enter a +ve number!")
            
            elif key == 'category':
                if is_valid_category(user_input):
                    validate_data[key] = user_input.strip().lower() # normalize the input
                    break
                else:
                    print("Invalid category. Chooose from the allowed list.")
                
            elif key == 'date':
                if is_valid_date(user_input):
                    validate_data[key] = user_input
                    break
                else:
                    print("Invalid date. Please use the format DD-MM-YYYY")
                
            elif key == 'description':
                if is_valid_description(user_input):
                    validate_data[key] = user_input.strip()
                    break
                else:
                    print("Description can't be empty!")

    # Once all are validated, finalize the entry
    try:
        new_expense = ExpenseEntry(**validate_data)