import datetime

class Truck:

    def __init__(self, truck_id, packages, departure_time):
        self.truck_id = truck_id
        self.max_capacity = 16
        self.speed = '18mph'
        self.packages = packages
        self.load = len(self.packages)
        self.hub = "4001 South 700 East"
        self.address = self.hub
        self.mileage = 0
        self.departure_time = departure_time
        self.current_time = departure_time

    def load_package(self, package):
        if package is not None and self.load <= self.max_capacity:
            self.packages.append(package)
            self.load += 1

    def return_to_hub(self, mileage):
        self.mileage += mileage
        self.address = self.hub
        self.current_time += datetime.timedelta(hours=mileage / 18)