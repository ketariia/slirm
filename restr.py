def is_even(x):
    """
    Determines whether a number is even.

    Parameters:
        x (int): A number to check.
    Returns:
        bool: True if x does not have any remainder when divided by 2, False otherwise.
    """
    check_divisibility_by_2 = x % 2 == 0
    return check_divisibility_by_2

print(is_even(6)) # prints True
print(is_even(5)) # prints False
