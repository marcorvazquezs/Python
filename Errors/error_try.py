# this function handles the error when trying to divide by zero
def div42by(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: You tried to divide by zero.')

print(div42by(2))
print(div42by(12))
print(div42by(0))
print(div42by(1))
print('')

# input validation 
print('How many dogs do you have?')
numDogs = input()
try:
    if int(numDogs) >= 5:
        print('That is a lot of dogs!')
    elif int(numDogs) >= 1 and int(numDogs) < 5:
        print('That is not that many dogs.')
    else: 
        print('That is not a valid number of dogs.')
except ValueError:
    print('You did not enter a number.')

    