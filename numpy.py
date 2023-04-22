def sum_list(numbers):
    """
    Calculates the sum of the elements in the provided numpy array.

    Args:
        numbers (numpy array): The array to be summed.

    Returns:
        numpy array: The sum of the array.

    Examples:
        assert sum_list([1, 2, 3]) == 6
        assert sum_list(np.array([4, 5, 6])) == 15
        my_list = [1, 5, 6, 3, 9]
        assert sum_list(my_list) == 34
    """
    total = 0
    for num in numbers:
        total = total + num
    return total
