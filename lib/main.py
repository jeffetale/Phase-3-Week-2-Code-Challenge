from customer import Customer
from restaurant import Restaurant
from review import Review

# Create customer and restaurant instances
customer1 = Customer("John", "Doe")
customer2 = Customer("Jane", "Smith")
restaurant1 = Restaurant("Yummy Bites")
restaurant2 = Restaurant("Tasty Treats")

# Add reviews to customers and restaurants
customer1.add_review(restaurant1, 4.5)
customer1.add_review(restaurant2, 3.8)
customer2.add_review(restaurant1, 3.0)

# Get unique restaurants reviewed by a customer
print(f"{customer1.full_name()} has reviewed the following restaurants:")
for r in customer1.restaurants():
    print(r.name())

# Get unique customers who reviewed a restaurant
print(f"\n{restaurant1.name()} has been reviewed by:")
for c in restaurant1.customers():
    print(c.full_name())

# Get all customers and their reviews
all_customers = Customer.all()
for c in all_customers:
    print(f"Customer: {c.full_name()}")
    for r in c.reviews():
        print(f"  Restaurant: {r.restaurant().name()}, Rating: {r.get_rating()}")

# Get all reviews
all_reviews = Review.all()
for r in all_reviews:
    print(f"\nCustomer: {r.customer().full_name()}, Restaurant: {r.restaurant().name()}, Rating: {r.get_rating()}")

# Get the number of reviews authored by a customer
print(f"\n{customer1.full_name()} has authored {customer1.num_reviews()} reviews")
print(f"{customer2.full_name()} has authored {customer2.num_reviews()} reviews")

# Return the name that matches a customer's full name
customer = Customer.find_by_name("John Doe")
if customer:
    print(f"\nFound customer: {customer.full_name()}")
else:
    print("Customer not found")

# Return the names that matches a customers' given name
matching_customers = Customer.find_all_by_given_name("John")
for customer in matching_customers:
    print(f"\nFound customer: {customer.full_name()}")

# Get average star rating for restaurants based on reviews
print(f"\n{restaurant1.name()} has an average star rating of {restaurant1.average_star_rating()}")


