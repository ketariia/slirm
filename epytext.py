# @brief This function calculates the sum of the elements in list
# @param numbers <list> a list of numbers
# @return int the sum of the numbers
def sum_list(numbers):
    # The actual implementation of the function
    total = 0
    for num in numbers:
        total = total + num
    return total
