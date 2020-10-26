# print something five times 
print('My name is')
for i in range(5):
    print('Marco, for the ' + str(i) + 'th time.')
print('')

# for loop to calculate sum of 0 to 100
total = 0 
for num in range(101): 
    total = total + num
print(total)
print('')

# first loop written as a while loop
print('My name is')
i = 0
while i < 5:
    print('Marco, for the ' + str(i) + 'th time.')
    i  = i + 1
print('')

# loop using range 
print('This loop uses the range function')
for i in range (2,5): 
    print('This is the ' + str(i) + 'th iteration.')
print('')

# The range function can be called with one, two or three arguments 
# The first argument is when the loop will begin. 
# The second argument is when the loop will end. 
# The third is the set argument, it will go up or down by this amount. 
# break and continue can be used within loops

# Example with three arguments 
print('This loop uses the range function with three arguments')
for i in range (1,11,2):
    print('This is the ' + str(i) + 'th iteration of the loop with a step of 2.')