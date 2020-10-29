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
spam = ['cat', 'dog', 'bat']
spam.append('moose')

print(spam)
print('')

# insert to add objects at a specific index in the list 
spam.insert(0, 'chicken')
print(spam)
print('')

# remove a value in an index regardless of value 
del spam[0]
print(spam)
print('')

# remove a specific value from list 
spam.remove('bat')
print(spam)
print('')

# sort items in list
numbers = [2, 5, 3.14, 1, -7]
numbers.sort()
print(numbers)
print('')

animals = ['ants', 'cats', 'dogs', 'badgers', 'elephants']
animals.sort()
print(animals)
print('')

# to sort in reverse order use list.sort(reverse=True)
# sorting happens in "ASCII-betical" order. To sort normally pass key=str.lower
# list.sort(key=str.lower)