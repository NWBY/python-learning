# Lists are basically arrays but have no fixed size
users = []
users.append('sam')
users.append('courtney')

# Can also define and declare at the same time
users = ['sam', 'courtney']

# Can access by index
print(users[0])

# Can also loop through lists
for user in users:
    print(user)