"""
This is the program's "brain." It handles user input, menu navigation, and calls functions from other files.
Example: Display menu options like "Add Expense" or "View Expenses" and call the respective function from `expense_handler.py`.
"""

from expense_handler import ExpenseEntry, ExpenseManager
from utils import is_valid_amount, is_valid_category, is_valid_date, is_valid_description

def get_user_input():

    questions = {
        "amount": "Enter the amount: ",
        "category": "Enter the category: ",
        "date": "Enter the date (DD-MM-YYYY): ",
        "description": "Enter a brief description: "
    }

    validated_data = {}

    # loop through each field input and validating it
    for field, prompt in questions.items():
        while True:
            user_input = input(prompt)
            if field == 'amount' and is_valid_amount(user_input):
                    validated_data[field] = float(user_input) # format and store
                    break
            elif field == 'category'and is_valid_category(user_input):
                    validated_data[field] = user_input.strip().lower() # normalize the input
                    break
            elif field == 'date' and is_valid_date(user_input):
                    validated_data[field] = user_input
                    break
            elif field == 'description' and is_valid_description(user_input):
                    validated_data[field] = user_input.strip()
                    break
            else:
                 print(f"Invalid input for {field}. Please try again!")
    
    return validated_data

