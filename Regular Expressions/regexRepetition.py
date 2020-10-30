import re 

# ? regex - pattern can appear 0 or 1 time in string 
batRegex = re.compile(r'Bat(wo)?man')
matchObject = batRegex.search('The Adventures of Batman')
print(matchObject.group())
print('')

matchObject = batRegex.search('The Adventures of Batwoman')
print(matchObject.group())
print('')


# Search for optional area code 

# This version requires area code
phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
matchObject = phoneRegex.search('My phone number is 850-300-1022. Call me tomorrow.')
print(matchObject.group())

# This version makes the area code optional 
phoneArea = 'My phone number is 850-300-1022. Call me tomorrow.'
phoneShort = 'My phone number is 300-1022. Call me tomorrow.'

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
matchObject = phoneRegex.search(phoneArea)
print('The phone number found was: ' + matchObject.group() + '.')
print('')

matchObject = phoneRegex.search(phoneShort)
print('The phone number found was: ' + matchObject.group())
print('')

# using * - pattern appears 0 or more times 
batRegex = re.compile(r'Bat(wo)*man')
matchObject = batRegex.search('The Adventures of Batwowowoman')
print(matchObject.group())
print('')

# using + - pattern MUST appear at least once 
batRegex = re.compile(r'Bat(wo)+man')
matchObject = batRegex.search('The Adventures of Batman')
print(matchObject == None)

# use {} to match pattern a number of times 
haRegex = re.compile(r'(Ha){3}')
matchObject = haRegex.search('He said "HaHaHa"')
print(matchObject.group())