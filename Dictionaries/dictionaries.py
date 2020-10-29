# example of a dictionary  

myDog = {'size': 'fat', 'color': 'white', 'disposition': 'quiet'}
print('My dog has ' + myDog['color'] + ' fur.')
print('')

# dictionaries are unordered, order of keys and values does not matter 
eggs = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
ham = {'species': 'cat', 'name': 'Zophie', 'age': '8'}

#check if a key exists in a dictionary
print('name' in eggs)
print('')

# lists keys of a dictionary 
print(list(eggs.keys()))
print('')

# list values of a dictionary 
print(list(eggs.values()))
print('')

# lists both keys and values of a dictionary 
print(list(eggs.items()))
print('')

# use dictionary keys in a for loop
for k in eggs.keys():
    print(k)
print('')

for v in eggs.values(): 
    print(v)
print('')

for k, v in eggs.items():
    print(k, v)
print('')