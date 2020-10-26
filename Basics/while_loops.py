# while loop 
eggs = 0 
while eggs < 5: 
    print('We need more eggs.')
    eggs = eggs + 1
print('')

# using continue to skip a loop iteration
ham = 0 
while ham < 5:
    ham = ham + 1 
    if ham == 3:
        continue
    print('We have ' + str(ham) + ' hams.')
print('')

# input validation using while loop 
name = ''
while name != 'marco':
    print('Please type your name.')
    name = input()
print('')
print('Thank you!')
print('')

# using break to stop an infinite loop 
yourName = ''
while True:
    print('Please type your name.')
    yourName = input()
    if yourName == 'your name':
        break  # breaks out of infinite loop
print('')
print('Thank you!')