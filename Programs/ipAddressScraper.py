#! python3

# import regex and pyperclip module
import re, pyperclip

# regex to match IP Addresses
ipRegex = re.compile(r'''
(
\d{1,3}        # first octet
\.             # first period 
\d{1,3}        # second octet 
\.             # second period
\d{1,3}        # third octet 
\.             # third period 
\d{1,3}        # fourth octet
)
''', re.VERBOSE)

# take list of IP addresses from clipboard 
text = pyperclip.paste()

# search matching IP address pattern
extractedIPs = ipRegex.findall(text)

count = 0 # variable to count number of resulting IP addresses

for ipAddress in extractedIPs: 
    count+=1

# cleanup results 
results = '\n'.join(extractedIPs)

# print results
if count >= 1:
    print('The following ' + str(count) + ' IP Addresses were found:\n')
    print(results)
else:
    print('No IP Addresses were found.')
