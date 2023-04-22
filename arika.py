my_list=[1,5,6,3,9]
def sum_list(numbers):
    total = 0
    for num in numbers:
        total = total + num
    return total
print(sum_list(my_list))