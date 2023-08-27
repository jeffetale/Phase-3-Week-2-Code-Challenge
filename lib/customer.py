from review import Review

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
        reviewed_restaurants = set()
        for review in self._reviews:
            reviewed_restaurants.add(review.restaurant())
        return list(reviewed_restaurants)
    
    def add_review(self, restaurant, rating):
        new_review = Review(self, restaurant, rating)
        self._reviews.append(new_review)

    def reviews(self):
        return self._reviews
    
    def num_reviews(self):
        return len(self._reviews)
    
    @classmethod
    def find_by_name(cls, name):
        for customer in cls.all_customers:
            if customer.full_name() == name:
                return customer
        return None

    @classmethod
    def all(cls):
        return cls.all_customers
    
    @classmethod
    def find_all_by_given_name(cls, given_name):
        matching_customers = []
        for customer in cls.all_customers:
            if customer.given_name() == given_name:
                matching_customers.append(customer)
        return matching_customers
        

