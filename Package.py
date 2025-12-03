class Package:
    """
    A class modeling a package and its required properties within a delivery service.
    """

    def __init__(self, package_id, address, city, state, zipcode, delivery_deadline, weight, special_notes):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.delivery_deadline = delivery_deadline
        self.weight = weight
        self.special_notes = special_notes
        self.status = "Currently at Hub"
        self.depart_time = None
        self.delivery_time = None


    def update_status(self, user_selected_time):
        if self.depart_time is not None:
            self.status = "En Route"
        if self.delivery_time is not None:
            self.status = "Delivered"


    def show_package_status(self):
        return (f"Package ID: {self.package_id}\t\t"
                f"Address: {self.address}\t\t"
                f"Delivery Deadline: {self.delivery_deadline}\t\t"
                f"Status: {self.status}\t\t"
                f"Time of Delivery: {self.delivery_time}")

    def __str__(self):
        return (f"Package ID: {self.package_id}\n"
                f"Address: {self.address}\n"
                f"City: {self.city}\n"
                f"State: {self.state}\n"
                f"Zipcode: {self.zipcode}\n"
                f"Delivery Deadline: {self.delivery_deadline}\n"
                f"Package Weight: {self.weight}\n"
                f"Status: {self.status}\n"
                f"Departure Time: {self.depart_time}\n"
                f"Time of Delivery: {self.delivery_time}")


    def __repr__(self):
        return  (f"Package ID: {self.package_id}\n "
                 f"Address: {self.address}\n"
                 f"City: {self.city}\n"
                 f"State: {self.state}\n"
                 f"Zipcode: {self.zipcode}\n"
                 f"Delivery Deadline: {self.delivery_deadline}\n"
                 f"Package Weight: {self.weight}\n"
                 f"Status: {self.status}\n"
                 f"Time of Delivery: {self.delivery_time}\n\n")
