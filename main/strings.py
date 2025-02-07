# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = 'Brad'
age = 37

# Concatenate

# print('Hello, my name is ' + name + ' and I am ' + str(age) + ' years old')

# String Formatting

# Arguments  by position
# print('My name is {name} and I am {age}'.format(name = name, age=age))

# F-Strings
# print(f"Hello, my name is {name} ad I am {age} years old")

# String Methods

s = 'hello world'
# capitalize string
print(s.capitalize())
# Make upper case
print(s.upper())
#make all ower case
print(s.lower())
# Swap case
print(s.swapcase())
# get len
print(len(s))
# Replace
print(s.replace('world', 'everyone'))
# Split into a list
print(s.split())
# Find position
print(s.find('r'))
# is all alphanumeric
print(s.isalnum())
# is all alpha
print(s.isalpha())
# count
sub='h'
print(s.count(sub))
# startswith
print(s.startswith('hello'))
# endswith
print(s.endswith('d'))

