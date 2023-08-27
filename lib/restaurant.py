class Restaurant:
    def __init__(self, name=str):
        self._name = name
        self._reviews = []

    def name(self):
        return self._name
    
    def add_reviews(self, review):
        self._reviews.append(review)

    def reviews(self):
        return self._reviews
    
    def reviewed_customers(self):
        unique_customers = set()
        for review in self._reviews:
            unique_customers.add(review.customer())
        return list(unique_customers)

        