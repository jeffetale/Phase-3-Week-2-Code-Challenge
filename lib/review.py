class Review:
    all_reviews = []

    def __init__(self, customer, restaurant, rating=int):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating
        Review.all_reviews.append(self)

    def rating(self):
        return self.rating
    
    @classmethod
    def all(cls):
        return cls.all_reviews