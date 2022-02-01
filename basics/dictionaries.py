# Dictionaries store data in key value pairs similar to an Object in JS
# Defined in {} like objects
user = {
    'name': 'Sam',
    'age': 24,
    'nationality': 'British'
}

# Can access keys by square bracket with key name
# print(user['age'])

# Can also access with get function, can also pass default value as second parama to get function
print(user.get('car', 'Renault'))