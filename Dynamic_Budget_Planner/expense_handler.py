"""
Contains functions for core operations like:
    Adding an expense.
    Reading expenses from the file.
    Filtering or summarizing expenses.
Makes the code modular and reusable.
"""

from utils import is_valid_amount, is_valid_category, is_valid_date, is_valid_description
import uuid

class ExpenseEntry():
    def __init__(self, amount, category, date, id, description):
        if not is_valid_amount(amount):
            raise ValueError("Invalid input error! Amount must be +ve")
        if not is_valid_date(date):
            raise ValueError("Invalid date error! Please provide a valid date in MM-DD-YYYY format.")
        if not is_valid_description(description):
            raise ValueError("Description can't be empty")
        if not is_valid_category(category):
            raise ValueError("Invalid category error! Category not allowed")
        self.id = uuid.uuid4() # Generating a unique id for each datapoint

        # Assigning values only after validation
        self.amount = amount
        self.date = date 
        self.category = category
        
class ExpenseManager():
    def __init__(self):
        self.expenses = []
        
    def add_expense(self, expense):
        if isinstance(expense, ExpenseEntry):
            self.expenses.append(expense)
        else:
            raise ValueError("Invalid expense entry!")
        
    def update_expense(self, expense_id, **kwargs):
        for expense in self.expenses:
            if expense.id == expense_id:
                for key, value in kwargs.items():
                    if key == "amount":
                        is_valid = is_valid_amount(value)
                    elif key == "category":
                        is_valid = is_valid_category(value)
                    elif key == "date":
                        is_valid = is_valid_date(value)
                    elif key == "description":
                        is_valid = is_valid_description(value)
                    else:
                        raise ValueError("Invalid attritube: {key}") # Handling invalid keys
                    
                    if is_valid:
                        setattr(expense, key, value)
                    else:
                        raise ValueError(f"Invalid {key}: {value}")
                return # existing the loop after updating

        raise ValueError("Expense not found")
    
    def delete_expense(self, expense_id, delete_all=True, arrtibutes_to_delete=None):
        for expense in self.expenses:
            if expense.id == expense_id:
                if 0 <= expense_id <= len(self.expenses):
                    expense = self.expenses[expense_id]
                    
                    if delete_all:
                        self.expenses.pop(expense)
                        print(f"Deleted expense {expense_id}!")
                    else:
                        if arrtibutes_to_delete:
                            for attr_name, new_value in arrtibutes_to_delete:
                                if attr_name == "1":
                                    # amount
                                    ...
                                elif attr_name == '2':
                                    # category
                                    ...
                                elif attr_name == '3':
                                    # date
                                    ...
                                elif attr_name == '4':
                                    # description
                                    ...