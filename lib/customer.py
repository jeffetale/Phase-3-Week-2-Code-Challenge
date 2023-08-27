class Customer:

    all_customers = []

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        Customer.all_customers.append(self)

    def given_name(self):
        return self.first_name
    
    def family_name(self):
        return self.last_name
    
    def full_name(self):
        return self.first_name + " " + self.last_name
    
    @classmethod
    def all(cls):
        return cls.all_customers

