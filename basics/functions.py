# To define a function need to use the `def` keyword
# Functions names should be all lowercase with underscores
def print_users_name():
    name = input('Enter your name: ')
    print('Hello ' + name + "!")
    
# To run a function we need to call it like below
# print_users_name()

# Functions can have parameters
def say_planet(planet):
    print(planet)
    
# say_planet('Mars')

# Functions can also return something
def get_squared(num):
    return num ** 2

squared = get_squared(3)
print(squared)
