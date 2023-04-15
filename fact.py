
def factorial(n):
    if n <= 0:
        return 
    else:
        return n * factorial(n-1)
n = int(input('ваше число'))
print('факториал числа =')   
print(factorial(n))