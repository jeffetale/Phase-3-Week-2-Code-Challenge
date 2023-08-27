class Customer:

    all_customers = []

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self._reviews = []
        Customer.all_customers.append(self)        

    def given_name(self):
        return self.first_name
    
    def family_name(self):
        return self.last_name
    
    def full_name(self):
        return self.first_name + " " + self.last_name
    
    def restaurants(self):
        unique_restaurants = set()
        for review in self._reviews:
            unique_restaurants.add(review.restaurant())

        return list(unique_restaurants)
    
    @classmethod
    def all(cls):
        return cls.all_customers

