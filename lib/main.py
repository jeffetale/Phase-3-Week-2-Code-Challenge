from customer import Customer
from restaurant import Restaurant
from review import Review


customer1 = Customer("Robert", "Smith")
customer2 = Customer("John", "Doe")
customer3 = Customer("Mary", "Jane")

restaurant1 = Restaurant("Pizza Hut")
restaurant2 = Restaurant("Domino's")
restaurant3 = Restaurant("KFC")

#review1 = Review(customer1, restaurant1, 5)
#review2 = Review(customer2, restaurant2, 4)
#review3 = Review(customer3, restaurant3, 3)

customer1.add_review(restaurant1, 4.5)
customer1.add_review(restaurant2, 3.8)
customer2.add_review(restaurant1, 3.0)


