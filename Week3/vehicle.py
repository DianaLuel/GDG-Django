class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.__year = year

    def describe(self):
        return f"This is a {self.make} {self.model} from {self.__year}."

    def get_year(self):
        return self.__year

class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors

    def describe(self):
        return f"This is a {self.make} {self.model} with {self.num_doors} doors from {self.get_year()}."

class Bike(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)

    def describe(self):
        return f"This is a {self.make} {self.model} bike from {self.get_year()}."

def vehicle_info(vehicle):
    print(vehicle.describe())

car = Car("Toyota", "Corolla", 2023, 4)
bike = Bike("Yamaha", "MT-07", 2022)

vehicle_info(car)
vehicle_info(bike)