spam = 'Hello world!'

 # upper method 
print(spam.upper())

# lower method 
print(spam.lower())

# isupper and islower method return a boolean value 
print(spam.islower())

print(spam.isupper())

# string formatting 
name = 'Alice'
place = 'Main Street'
time = '6 pm'
food = 'turnips'

print('Hello %s, you are invited to a party at %s at %s. Please bring %s.' %(name, place, time, food))