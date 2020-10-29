# create new string from slices
name = 'Zophie a cat'
newName = name[0:7] + 'the' + name[8:12]
print(newName)

# References strings vs lists 
spam = 42 
cheese = spam # simply copies spam value to cheese variable
spam = 100 # changing value in spam does not change the value of cheese
print(spam)
print(cheese)
print('')

numbers = [0,1,2,3,4,5]
cheese = numbers  # cheese actually references the numbers list, does not store a copy of the list
cheese[1] = 'Hello!' #changing index 1 in cheese also changes it in the numbers list 
print(cheese)
print(numbers)
print('')

# how to create a completely new copy of a list 
import copy

letters = ['A', 'B', 'C', 'D']
cheese = copy.deepcopy(letters)
cheese[1] = 42 #changing list cheese does not change letters list since it is a separate copy
print(cheese)
print(letters)
print('')

# The \ line continuation character can be used to stretch Python instructions across multiple lines