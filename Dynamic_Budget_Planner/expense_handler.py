"""
Contains functions for core operations like:
    Adding an expense.
    Reading expenses from the file.
    Filtering or summarizing expenses.
Makes the code modular and reusable.
"""

from utils import is_valid_amount, is_valid_category, is_valid_date

class ExpenseEntry():
    def __init__(self, amount, category, date):
        if not is_valid_amount(amount):
            raise ValueError("Invalid input error! Amount must be +ve")
        if not is_valid_date(date):
            raise ValueError("Invalid date error! Please provide a valid date in MM-DD-YYYY format.")
        if not is_valid_category(category):
            raise ValueError("Invalid category error! Category not allowed")
        
        # Assigning values only after validation
        self.amount = amount
        self.date = date
        self.category = category
        
