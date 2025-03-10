# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries


# Create dictionary

person = {
    "first_name" : "John",
    "last_name" : "Doe",
    "age": 30
}

# person2 = dict(first_name = "Sara", last_name = "Williams")


# Get value
print(person['first_name'])
print(person.get('last_name'))


# Add key/ value

person['phone'] = '07061847132'
print(person)

# Get dict keys
print(person.keys())


# Get dict items
print(person.items())

# copy dict

person2 = person.copy()
person2['city'] = "Boston"
print(person2)


# Remove an item
del(person["age"])
person.pop('phone')


# Clear
person.clear()

# Get length
print(len(person2))

# List of dict

people = [
    {"name":"Martha", "age": 30},
    {"name":"Kevin", "age": 25}
]

print(people[0]["age"])
