# Try except is basically Python's implementation of try catch

# If the user enters a string it will error
# We catch the error with try except
# Can catch specific errors and handle them by specifying the error
# We can also store the error in a variable using `as <variable>`
try: 
    age = int(input('Enter your age: '))
    print(age)
except ValueError as err:
    print(err)
    print('You need to enter a number dummy!')

