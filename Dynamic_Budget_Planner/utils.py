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

def is_valid_date(date_str, date_format="%Y-%m-%d"):
    try:
        date_obj = datetime.strptime(date_str, date_format)
        if date_obj > datetime.now():
            print(f"Cannot take future date's!")
            return False
        return True
    except ValueError as e:
        return str(e)
    except TypeError as e:
        return str(e)

ALLOWED_CATEGORIES = ["food", "housing", "transportation", "entertainment", "utilities", "other"]

def is_valid_category(category):
    if isinstance(category, str):
        return category.strip().lower() in ALLOWED_CATEGORIES
    elif isinstance(category, int):
        return 1 <= category >= len(ALLOWED_CATEGORIES)
    else:
        print("Invalid category type")
        return False