from Car import Car

car = Car('Volvo', 'XC40', 'white')

#print(car)

# Can access both instance and class attributes using the dot notation
print(car.brand)

# Attributes can also be changed dynamically
car.model = 'XC60'