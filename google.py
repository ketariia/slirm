# Function to sum a list of numbers
def sum_list(numbers):
    """
    Sum: adds the numbers in a list together and returns the result
    Input: numbers - a list of numbers
    Output: total - the total sum of the numbers in the list
    Example:
    >>> my_list = [1, 2, 3, 4, 5]
    >>> result = sum_list(my_list)
    >>> print(result)  # Output: 15
    """
    total = 0
    for num in numbers:
        total = total + num
    return total
