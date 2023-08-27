class Restaurant:
    def __init__(self, name):
        self._name = name
        self._reviews = []

    def name(self):
        return self._name
    
    def add_review(self, review):
        self._reviews.append(review)

    def reviews(self):
        return self._reviews
    
    def customers(self):
        unique_customers = set()
        for review in self._reviews:
            unique_customers.add(review.customer())
        return list(unique_customers)
    
    def average_star_rating(self):
        total_rating = 0
        for review in self._reviews:
            total_rating += review.get_rating()
        if len(self._reviews) > 0:
            return total_rating / len(self._reviews)
        else:
            return 0

        

        