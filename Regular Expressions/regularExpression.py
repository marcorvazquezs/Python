# non-regular expression example 
def isPhoneNumber(text):
    if len(text) != 12:
        return False # not phone number sized
    for i in range(0,3):
        if not text[i].isdecimal():
            return False # no area code 
    if text[3] != '-':
        return False # missing dash
    for i in range(4,7):
        if not text[i].isdecimal():
            return False # no first 3 three digits 
    if text[7] != '-':
        return False # missing second dash
    for i in range(8,12):
        if not text[i].isdecimal(): 
            return False # missing last four digits
    return True 

print('Please enter a phone number:')
phoneNumber = input()
print('')

print(isPhoneNumber(phoneNumber))
print('')

# another example - searches for phone number in message
message = 'Call me at 415-444-1011 tomorrow, or at 415-555-9999 for my office line.'
foundNumber = False 
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found:' + chunk)
        foundNumber = True 
if not foundNumber: 
    print('Could not find any phone numbers.')


# regular expression example 
import re 

# use r to use a raw string and ignore escape characters
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') 
matchObject = phoneNumRegex.search(message)  #searches string for first occurence of pattern and returns a match object 
print(matchObject.group()) # group method returns actual text

print(phoneNumRegex.findall(message)) # find all occurences of pattern in string 
