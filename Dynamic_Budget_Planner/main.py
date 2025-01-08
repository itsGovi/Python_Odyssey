"""
This is the program's "brain." It handles user input, menu navigation, and calls functions from other files.
Example: Display menu options like "Add Expense" or "View Expenses" and call the respective function from `expense_handler.py`.
"""

from file_handler import read_json, write_json

file_path = 'Dynamic_Budget_Planner/data/expenses(test_v1).json'

# test data
expenses = [
    {"amount": 500, "date": "2024-12-22", "category": "Food", "description": "Lunch"}
]
write_json(file_path, expenses)

data = read_json(file_path)
print(f"Expenses Data:\n {data}")