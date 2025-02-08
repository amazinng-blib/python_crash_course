# Python has functions for creating, reading, updating, and deleting files.

# Open a  file
myFile = open('myFile.txt', 'w')


# Get some info
print('Name: ', myFile.name )
print('is Closed: ', myFile.closed )
print('Opening mode: ', myFile.mode )


# Write to file
myFile.write('I love python')
myFile.write(' and JavaScript.')
myFile.close()

# Append to file
myFile = open('myFile.txt', 'a')
myFile.write('I also like php')
myFile.close()


# Read from a file
myFile = open('myFile.txt', 'r+')
text = myFile.read(100)
print(text)