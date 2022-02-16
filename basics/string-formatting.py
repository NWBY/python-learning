dog = 'Ruby'
age = 10

print('%s is %d years old' % (dog, age))

# %s is for strings or lists or other objects
# %d is for integers
# %f is for floats
# %.4f is for limiting floats to only displaying so many digits after the decimal point, in this example its 4 decimal places

# Can also use the much easier f-Strings
f'Hello {dog}, you are {age} years old'