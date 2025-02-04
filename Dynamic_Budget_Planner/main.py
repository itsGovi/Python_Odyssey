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

def get_search_input():
          
      search_question = {
        "1": "ID",
        "2": "Amount",
        "3": "Category",
        "4": "Date",
        "5": "Description",
        "6": "Exit"
      }

      print("\nHow would you like to search:")
      for key,value in  search_question:
            print(f"{key}: {value}")

      while True:
            choice = input("Enter your Choice (1-5): ").strip()

            if choice == "1":
                  search_value = input("Enter Expense ID: ").strip()
                  return {"id": search_value}
            elif choice == "2":
                  while True:
                        search_value = input("Enter amount: ").strip()
                        if is_valid_amount(search_value):
                              return {"amount": search_value}
                        else:
                              print("Invalid amount. Try Again.")
            elif choice == "3":
                  while True:
                        search_value = input("Enter category: ").strip()
                        if is_valid_category(search_value):
                              return {"category": search_value}
                        else:
                              print("Invalid category. Try Again.")
            elif choice == "4":
                  while True:
                        search_value = input("Enter date (DD-MM-YYYY): ").strip()
                        if is_valid_date(search_value):
                              return {"date": search_value}
                        else:
                              print("Invalid date. Try Again.")
            elif choice == "5":
                  search_value = input("Enter description keyword: ").strip()
                  return{"Description:": search_value}
            elif choice == "6":
                  print("See Ya!")
                  break

            else:
                  print("Invalid choice. Please select a number 1-6.")

def main():
    manager = ExpenseManager()

    
    while True:
        print("\nMenu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Update Expense")
        print("4. Delete Expense")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        if choice == "1":
              data = get_user_input()
              new_expense = ExpenseEntry(**data)
              manager.add_expense(new_expense)
              print("Expense added successfully!")
        elif choice == "2":
              for expense in manager.expenses:
                    print(expense.to_dict())
        elif choice == '3':
                  print("coming soon")
        elif choice == '4':
              print('Delete feature coming soon!')
        elif choice == '5':
              print("Goodbye!")
              break
        else:
              print("Invalid choice. Try again!")