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
        self.__model = model

    def set_mileage(self, mileage):
        self.__mileage = mileage

    def set_price(self, price):
        self.__price = price

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_mileage(self):
        return self.__mileage

    def get_price(self):
        return self.__price
    
    def __str__(self):
        return f'make: {self.__make}\n' \
            f'model: {self.__model}\n' \
            f'mileage: {self.__mileage}\n' \
            f'price: {self.__price}'

#the Car class does not need to rewrite the make/model/mileage/price code because it gets it from the Automobile class which defines it there.

class Car(Automobile):
    def __init__(self, make, model, mileage, price, doors):
        #the super() function is referring to the superclass "Automobile".
        super().__init__(make, model, mileage, price)
        self.__doors = doors

    def set_doors(self, doors):
        self.__doors = doors
    #each subclass only needs to store it's own attribute because it gets the rest from Automobile.
    def get_doors(self):
        return self.__doors
    
class Truck(Automobile):
    def __init__(self, make, model, mileage, price, drive_type):
        super().__init__(make, model, mileage, price)
        self.__drive_type = drive_type

    def set_drive_type(self, drive_type):
        self.__drive_type = drive_type

    def get_drive_type(self):
        return self.__drive_type
    
class SUV(Automobile):
    def __init__(self, make, model, mileage, price, passengers):
        super().__init__(make, model, mileage, price)
        self.__passengers = passengers

    def set_passengers(self, passengers):
        self.__passengers = passengers

    def get_passengers(self):
        return self.__passengers
        

    