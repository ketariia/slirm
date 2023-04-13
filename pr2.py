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