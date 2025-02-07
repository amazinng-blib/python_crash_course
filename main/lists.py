# A List is a collection which is ordered and changeable. Allows duplicate members.

# Create list
numbers = [1, 2, 3, 4, 5]
fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']

# Use a constructor
# numbers2 = list((1, 2, 3, 4, 5))

# Get a value
print(fruits[1])

# Get length
print(len(fruits))

# Append to list
fruits.append('Mangos')


# Remove from list
fruits.remove('Grapes')

# Insert into position
fruits.insert(2, 'Strawberries')

# Remove from position
fruits.pop(2)

# Reverse list
fruits.reverse()

# sort 
fruits.sort()



# Change a value
fruits[0] = 'Blueberries'

# Reverse sort
fruits.sort(reverse=True)



print(fruits)

