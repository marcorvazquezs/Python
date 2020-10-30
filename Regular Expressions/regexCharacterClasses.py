import re

# make your own character classes 
vowelRegex = re.compile(r'[aeiou]') # will match any vowel 
print(vowelRegex.findall('Robocop eats baby food.'))

lettersRegex = re.compile(r'[a-zA-z]') # you can use ranges 
print(lettersRegex.findall('Robocop eats baby food.'))

#negative character classes 
consonantRegex = re.compile(r'[^aeiouAEIOU]') # match any character except vowels, including punctuation
print(consonantRegex.findall('Robocop eats baby food.'))