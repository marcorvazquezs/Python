import re

# using regex pipes 
message = 'Batmobile lost a wheel.'

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
matchObject = batRegex.search(message)
print(matchObject.group())

matchObject = batRegex.search('Batmotorcycle lost a wheel.')
print(matchObject) # if pattern is not matched the match object becomes a none value type
print(type(matchObject))
