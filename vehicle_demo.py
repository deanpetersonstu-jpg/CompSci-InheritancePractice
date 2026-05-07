"""
1. What do all vehicles in this example have in common?
They are all vehicles
2. Which class should be the superclass?
The Automobile class
3. Which classes should be subclasses?
Truck, Car, SUV
4. Why would it be inefficient to write totally separate `Car`, `Truck`, and `SUV` classes with no inheritance?
You would have to add way more code that you would have to change individually
"""

class Automobile:
    def __init__(self, make, model, mileage, price):
        self.__make = make
        self.__model = model
        self.__mileage = mileage
        self.__price = price

    def set_make(self, make):
        self.__make = make

    def set_model(self, model):
        self.__model

    def set_mileage(self, mileage):
        self.__mileage

    def set_price(self, price):
        self.__price

    def get_make(self, make):
        return self.__make

    def get_model(self, model):
        return self.__model

    def get_mileage(self, mileage):
        return self.__mileage

    def get_price(self, price):
        return self.__price
    
    def __str__(self):
        return f'make: {self.__make}\n' \
            f'model: {self.__model}\n' \
            f'mileage: {self.__mileage}\n' \
            f'price: {self.__price}'


    