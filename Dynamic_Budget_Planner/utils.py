"""
Contains helper functions like:
Validating inputs (e.g., checking if the date is valid).
Formatting outputs (e.g., displaying expenses in a table).
"""

from datetime import datetime


def is_valid_amount(amount):
    """
    checking if value is int and +ve
    """
    return isinstance(amount, (int, float)) and amount > 0 #we use `isinstance` to check if the input is even a no.?

def is_valid_date(date_str):
    try:
        date_obj = datetime.strptime(date_str, "%d-%m-%Y")
        if date_obj > datetime.now():
            print(f"Cannot take future date's! - {date_obj}")
            return False
        return True
    except ValueError as e:
        return False
    except TypeError as e:
        return False


def is_valid_category(category, alllowed_categories=None):
    if alllowed_categories is None:
        alllowed_categories = ["food", "housing", "transportation", "entertainment", "utilities", "other"]
    if isinstance(category, str):
        return category.strip().lower() in alllowed_categories
    elif isinstance(category, int):
        return 1 <= category >= len(alllowed_categories)
    else:
        print("Invalid category type")
        return False

def is_valid_description(description):
    return isinstance(description, str) and description.strip != "" #checking it's not empty