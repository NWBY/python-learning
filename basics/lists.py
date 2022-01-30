# Lists are basically arrays but have no fixed size
# List items can be different data types: users = ['sam', 24, true]
users = []
users.append('sam')
users.append('courtney')

# Can also define and declare at the same time
users = ['sam', 'courtney']

# Can access by index
firstUser = users[0]

# Can also loop through lists
for user in users:
    print(user)
    
moreUsers = ['ruby', 'marnie']

# Get list length
len(users)

# Union two lists with extend function
users.extend(moreUsers)

# Insert item at index
users.insert(1, 'paul')

# Remove item by value
users.remove('sam')

# Clear every item in list
# users.clear()

# Remove last element from list
# users.pop()

# Check if item exists in array - returns error if not in list, if it is then returns index
users.index('ruby')

# Count how many times an item exists in a list
users.count('courtney')

# Copy a list
users2 = users.copy()