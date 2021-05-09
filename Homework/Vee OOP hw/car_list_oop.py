# class
class Vehicle:
    # a
    # constructor
    def __init__(self, name, price, car_type='sports', color='red'):
        self.name = name
        self.price = price
        self.car_type = car_type
        self.color = color
    # set the default value for the type and
    # color fields of the Vehicle class object

    def description(self):
        return f'Color: {self.color}, type: {self.car_type}, name: {self.name}, $: {self.price}.'


# b
# creating vehicle list
vehicle_list = []
# c
for count in range(3):
    name = input("Provide name: ")
    price = input("Provide price: ")
    option = input("Would you like to provide type and color? yes/no: ")
    new_vehicle = Vehicle(name, price)
    if option == "yes":
        new_vehicle.car_type = input("Provide type: ")
        new_vehicle.color = input("Provide color: ")
    vehicle_list.append(new_vehicle.description())
for vehicle in vehicle_list:
    print(vehicle)
