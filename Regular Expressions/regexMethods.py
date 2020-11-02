import re

message = 'Agent Alice gave the secret documents to Agent Bob.'

namesRegex = re.compile(r'Agent \w+') # matches one or more letter characters
print(namesRegex.findall(message))

# find and replace using sub method 
classifiedMessage = namesRegex.sub('REDACTED', message)
print(classifiedMessage)

# classify only part of the name 
namesRegex = re.compile(r'Agent (\w)\w*')
classifiedMessage = namesRegex.sub(r'Agent \1*****', message) 
print(classifiedMessage)

# verbose method to make code more readable 
numberRegex = re.compile(r'''
(\d\d\d-)|      # area code (without parens, with dash)
(\(\d\d\d\) )  # -or- area code with parens and no dash
\d\d\d      # first 3 digits
-           # second dash
\d\d\d\d    # last four digits''', re.VERBOSE)  # whitespace is not part of the regex pattern

matchObject = numberRegex.findall('My phone number is 123-123-1234. Call me tomorrow.')
print(matchObject)