name = input('whats ur name')
age = int(input('how old r u')) 
if age < 18:
    print('haha kid')
elif age < 30:
    print('u r young')
elif age < 50:
    print('nice, middle-aged')
elif age > 50:
    print('u r old')   
else:
    print('u must be an immortal being')  


"""
Script for asking user's name and age.
Depending on how old the user is, different response message is printed.
Example Input:
Name: [Name]
Age: [Number greater than 18 and less than 50]
Example Output:
nice, middle-aged
"""
 