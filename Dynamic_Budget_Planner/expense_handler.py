"""
Contains functions for core operations like:
    Adding an expense.
    Reading expenses from the file.
    Filtering or summarizing expenses.
Makes the code modular and reusable.
"""

from utils import is_valid_amount, is_valid_category, is_valid_date, is_valid_description
import uuid
from file_handler import read_json, write_json
import json

class ExpenseEntry():
    def __init__(self, amount, category, date, id, description=""):
        if not is_valid_amount(amount):
            raise ValueError("Invalid input error! Amount must be +ve")
        if not is_valid_date(date):
            raise ValueError("Invalid date error! Please provide a valid date in MM-DD-YYYY format.")
        if not is_valid_description(description):
            raise ValueError("Description can't be empty")
        if not is_valid_category(category):
            raise ValueError("Invalid category error! Category not allowed")

        # Assigning values only after validation
        self.id = id if id else str(uuid.uuid4()) # Generating a unique id for each datapoint (or) if-else loop to get the available one's
        self.amount = amount
        self.date = date 
        self.category = category
        self.description = description
        
    def to_dict(self):
        return vars(self)

class ExpenseManager():
    def __init__(self, file_path = 'data\expenses.json'):
        self.file_path  = file_path
        self.expenses = self.load_expenses()

    def load_expenses(self):
        raw_data = read_json(self.file_path)
        return [ExpenseEntry(**exp) for exp in raw_data] # converting dict to objs
    
    def save_expenses(self):
        data = [exp.to_dict() for exp in self.expenses]
        write_json(self.file_path, data)

    def add_expense(self, expense):
        if isinstance(expense, ExpenseEntry):
            self.expenses.append(expense)
            self.save_expenses()
        else:
            raise ValueError("Invalid expense entry!")

    def list_expenses(self, limit=10):
        """Showing the most recent expenses to help users with unique ID identification"""
        print("\nRecent Expenses:")
        print("-" * 60)
        print(f"{'ID':<8} | {'Amount':<8} | {'Category':<15} | {'Date':<12} | {'Description'}")
        print("-" * 60)

        for exp in self.expenses[-limit:]:
            print(f"{exp.id[:6]:<8} | {exp.amount:<8} | {exp.category:<15} | {exp.date:<12} | {exp.description}")

        print("-" * 60)

    def get_update_input(self):
        expense_id = input("Enter expense_id to update: ")
        fields_to_update = {}

        print("\n What field(s) do you want to update?")
        fields = ["1. amount", "2. category", "3. date", "4. description", "5. Cancel Update"]
        for i in fields:
            print(i)

        while True:
            choice = input("What field do you want to change? ")
            if choice in ['1', 'amount']:
                new_amount = int(input("Enter new amount "))
                fields_to_update["amount"] = new_amount
            elif choice in ['2', 'category']:
                print("food", "housing", "transportation", "entertainment", "utilities", "other")            
                new_category = input("Enter new category ")
                fields_to_update["category"] = new_category
            elif choice in ['3', 'date']:
                new_date = input("Enter new date (DD-MM-YYYY) ")
                fields_to_update["date"] = new_date
            elif choice in ['4', 'description']:
                new_description = input("Enter new description ")
                fields_to_update["description"] = new_description
            elif choice in ['5', 'cancel update']:
                print("Update Cancelled")
                return None, None
            else:
                print("Invalid choice. Try again")

            another = input("Update another field? (y/n): ").lower()
            if another != 'y':
                break
        
        return expense_id, fields_to_update

    def find_expense_by_input(self, expense_id):
        for expense in self.expenses:
            if expense.id == expense_id:
                return expense
        return None # Expense not found

    def delete_expense(self, expense_id):
        for expense in self.expenses:
            if expense.id == expense_id:
                self.expenses.remove(expense)
                self.save_expenses()
                return
        
        raise ValueError(f"Expense with ID {expense_id} not found!")
    
    def update_expenses(self):
        #still figureing out what to write!
        ...