import pprint

# message to be counted
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'

# sets empty count dictionary
count = {}

# loop through each character in message
for character in message.upper():
    count.setdefault(character, 0)  # if character is not a key in dictionary it is added, if it already exists it just returns 0
    count[character] = count[character] + 1 # adds 1 to the value of the character key

pprint.pprint(count)