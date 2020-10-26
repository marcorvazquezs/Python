def hello():
    print('Hello!')
    print('How are you doing today?')
    print('Glad to hear!')
    print('')

hello()
hello()
hello()


# function using a parameter and passing arguments
def hi(name):
    print('Hello ' + name + '!')

# arguments 
hi('Alice')
hi('Bob')

# function with return statement
def plusOne(number):
    return number + 1

newNumber = plusOne(5)
print(newNumber)

