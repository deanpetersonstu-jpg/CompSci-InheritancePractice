from vehicles import Car, Truck, SUV

car = Car("Porsche", "911", "72,000", "$36,000.00", "2")
truck = Truck("Ford", "F-150", "200,000", "$11,200.00", "4WD" )
suv = SUV("Cadillac", "Escalade", "20,000", "$170,000.00", "8")

inventory = print(f"""
USED CAR INVENTORY

The following car is in inventory:
Make: {car.get_make()}
Model: {car.get_model()}
Mileage: {car.get_mileage()}
Price: {car.get_price()}
Number of doors: {car.get_doors()}

The following pickup truck is in inventory:
Make: {truck.get_make()}
Model: {truck.get_model()}
Mileage: {truck.get_mileage()}
Price: {truck.get_price()}
Drive type: {truck.get_drive_type()}

The following SUV is in inventory:
Make: {suv.get_make()}
Model: {suv.get_model()}
Mileage: {suv.get_mileage()}
Price: {suv.get_price()}
Passenger capacity:{suv.get_passengers()}
""")

"""
1. Which class is the superclass? Automobile

2. Which classes are subclasses? Car, Truck, SUV

3. What attributes are inherited by all three subclasses? make, model, mileage, price

4. What attribute is unique to the `Car` class? number of doors

5. What attribute is unique to the `Truck` class? drive type

6. What attribute is unique to the `SUV` class? passenger capacity

7. Why is inheritance useful in this example? you don't need to rewrite every attribute that applies to every vehicle making it a lot easier and simple.

8. What could go wrong if you copied and pasted the same automobile code into all three subclasses instead? There could be an error because there's a lot of steps and it wouldn't have the right inheritance.
"""