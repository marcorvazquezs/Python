#! python3

# Small program that returns file size of all files in a directory 

import os

totalSize = 0
for filename in os.listdir('C:\\Users\\Marco'):
    if not os.path.isfile(os.path.join('C:\\Users\\Marco', filename)):
        continue 
    totalSize = totalSize + os.path.getsize(os.path.join('C:\\Users\\Marco', filename))

print(totalSize)