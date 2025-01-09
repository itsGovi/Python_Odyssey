"""
Contains helper functions like:
Validating inputs (e.g., checking if the date is valid).
Formatting outputs (e.g., displaying expenses in a table).
"""

def is_valid_amount(amount):
    """
    checking if value is int and +ve
    """
    return isinstance(amount, (int, float)) and amount > 0 #we use `isinstance` to check if the input is even a no.?

def is_valid_date(date):
    