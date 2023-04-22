my_list=[1,5,6,3,9]
def sum_list(numbers):
    total = 0
    for num in numbers:
        total = total + num
    return total
print(sum_list(my_list))
'''
:param my_list: A list of numbers, which the function will sum.
:returns: The sum of the elements in the `my_list`.

:param my_list: A list of elements to sum
:returns: The sum of the elements in the `my_list`.
'''