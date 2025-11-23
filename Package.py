class Package:

    def __init__(self, package_id, address, city, state, zipcode, delivery_deadline, weight, special_notes, status):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.delivery_deadline = delivery_deadline
        self.weight = weight
        self.special_notes = special_notes
        self.status = status
        self.loading_time = None
        self.delivery_time = None

    def __str__(self):
        return (f"Package ID: {self.package_id}\n"
                f"Address: {self.address}\n"
                f"City: {self.city}\n"
                f"State: {self.state}\n"
                f"Zipcode: {self.zipcode}\n"
                f"Delivery Deadline: {self.delivery_deadline}\n"
                f"Package Weight: {self.weight}\n"
                f"Special Notes: {self.special_notes}\n"
                f"Status: {self.status}\n"
                f"Loading Time: {self.loading_time}\n"
                f"Time of Delivery: {self.delivery_time}")


    def __repr__(self):
        return  (f"Package ID: {self.package_id}\n"
                 f"Address: {self.address}\n"
                 f"City: {self.city}\n"
                 f"State: {self.state}\n"
                 f"Zipcode: {self.zipcode}\n"
                 f"Delivery Deadline: {self.delivery_deadline}\n"
                 f"Package Weight: {self.weight}\n"
                 f"Special Notes: {self.special_notes}\n"
                 f"Status: {self.status}\n"
                 f"Loading Time: {self.loading_time}\n"
                 f"Time of Delivery: {self.delivery_time}\n\n")
