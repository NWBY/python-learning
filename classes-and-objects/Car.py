class Car:
    # We can also define class attributes that will be the same in every instance
    number_of_wheels = 4

    # Attributes that are created in the __init__ function are called instance attributes as they only exist once an instance is created
    def __init__(self, brand, model, colour):
        self.brand = brand
        self.model = model
        self.colour = colour
    
    # We can also define instance methods
    def full_description(self):
        return f'The car is a {self.brand} {self.model} in {self.colour}'
    
    def brand_description(self):
        return f'The car is a {self.brand}'