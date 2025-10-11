# @abstractmethod - A decorator indicating abstract methods.

from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, brand, model, fuel_type):
        self.brand = brand
        self.model = model
        self.fuel_type = fuel_type

    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

    def get_details(self):
        print(f"Brand of vehicle: {self.brand}, Model of vehicle : {self.model}, Fuel Type of vehicle: {self.fuel_type}")
       
class Car(Vehicle):
    def start_engine(self):
        print("Car engine has started")

    def stop_engine(self):
        print("Car engine has stopped")

class bike(Vehicle):
    def start_engine(self):
        print("Bike engine has started")

    def stop_engine(self):
        print("Bike engine has stopped")

c = Car("Toyota", "Camry", "Petrol")
b = bike("Yamaha", "FZ", "Petrol")

c.get_details()
c.start_engine()
c.stop_engine()

b.get_details()
b.start_engine()
b.stop_engine()

       

