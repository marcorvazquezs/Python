import re 

# Search for pattern at the beginning using the ^ character
beginsWithRegex = re.compile(r'^Hello')
matchObject = beginsWithRegex.search('Hello there!')
print(matchObject.group())

matchObject = beginsWithRegex.search('He said "Hello!"')
print(matchObject == None)
print('')

# Search for pattern at the end using the $ character
endsWithRegex = re.compile(r'world!$')
matchObject = endsWithRegex.search('Hello world!')
print(matchObject.group())

matchObject = endsWithRegex.search('Hello world! jalsjdkjlajsk')
print(matchObject == None)
print('')

# Use both ^ and $ characters to match entire text, has to both begin and end with the pattern 
allDigitsRegex = re.compile(r'^\d+$')
matchObject = allDigitsRegex.search('12345678919')
print(matchObject.group())
print('')

# Use . character to match any character except new line 
atRegex = re.compile(r'.at') # matches anything followed by at
print(atRegex.findall('The cat in the hat sat on the flat mat.'))

atRegex = re.compile(r'.{1,2}at') # matches any one or two characters followed be at, including whitespace
print(atRegex.findall('The cat in the hat sat on the flat mat.'))

# match anything 
message = 'First Name: Marco Last Name: Vazquez'
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
matchObject = nameRegex.findall(message)
print(matchObject)

# .* uses greedy mode, this is a non-greedy match using .*?
serve = '<To serve humans> for dinner.>'
nonGreedyRegex = re.compile(r'<(.*?)>')
print(nonGreedyRegex.findall(serve))

# greedy match 
greedyMatch = re.compile(r'<(.*)>')
print(greedyMatch.findall(serve))

# . does not match new line 
prime = 'Server the public trust.\nProtect the innocent.\nUpload the law.'
dotStar = re.compile(r'.*')
print(dotStar.search(prime))

# make . match new line also 
dotStar = re.compile(r'.*', re.DOTALL)
print(dotStar.search(prime))

# case insensitive match 
vowelRegex = re.compile(r'[aeiou]', re.IGNORECASE)
print(vowelRegex.findall('Al, why does your programming book talk about Robocop so much?'))