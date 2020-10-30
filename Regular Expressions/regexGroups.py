import re

message = 'Call me at 415-444-1011 tomorrow, or at 415-555-9999 for my office line.'

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)') # add parentheses to group patterns
matchObject = phoneNumRegex.search(message)
print(matchObject.group()) 

print(matchObject.group(1))
print(matchObject.group(2))
print('')

# if message has parentheses and trying to find them in pattern 
message = 'Call me at (415)-444-1011 tomorrow, or at (415) 555-9999 for my office line.'

phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
matchObject = phoneNumRegex.search(message)

print(matchObject.group())
print(matchObject.group(1))
print(matchObject.group(2))
print('')