# assign values to list called supplies 
supplies = ['pens', 'staplers', 'notebooks', 'binders']

# loops and prints values within the supplies list
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i] + '.')

# using a list with multiple assignment of variables 
cat = ['fat', 'orange', 'loud']
size, color, disposition = cat #assigns list values to variables in order

print(size)
print(color)
print(disposition)
print('')

# variable swapping 
a = 'AAA'
b = 'BBB'
a,b = b,a

print(a)
print(b)
print('')

# augmented assignment 
spam = 42 
spam += 1 

print(spam)
print('')

# index returns the number in the list 
listNumber = cat.index('fat') #returns 0
print(listNumber)
print('')

# append to add objects to end of list 

