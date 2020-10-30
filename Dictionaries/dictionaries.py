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

# get method to access dictionary key to avoid errors if key does not exist. 
print(eggs.get('age', 0)) #looks for age key in dictionary, if key does not exist then it returns 0

# another get method example 
picnicItems = {'apples': 5, 'cups': 2}
print('I am bringing ' + str(picnicItems.get('napkins', 0)) + ' napkins to the picnic.')
print('')

# default method sets a key and value if the key isn't already set in the dictionary 
eggs.setdefault('color', 'black')
print(eggs)
print('')