# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 
# Create a tuple
fruits = ('Apples', 'Oranges', 'Grapes', 'Pears')
# fruits2 = tuple(('Apples', 'Oranges', 'Grapes'))

# Single value needs trailing .comma
fruits2 = ('Apples',)

# Get a value from tuple
print(fruits[1])

# can't change a value
# fruits[0] = 'Banana'


# Delete tuple
del fruits2

# print(len(fruits))


# A Set is a collection which is unordered and unindexed. No duplicate members.

# Create a set

fruits_set = {'Apples', 'Oranges', 'Mangos'}

# Check if in set
print('Apples' in fruits_set)

# Add to set
fruits_set.add('Grapes')

# Remove from set
fruits_set.remove('Grapes')

# Clear set
fruits_set.clear()

# Delete set
del fruits_set
print(fruits_set)