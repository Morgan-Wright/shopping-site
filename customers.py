"""Customers at Ubermelon."""


class Customer(object):
    """Ubermelon customer."""

    def __init__(self, firstname, lastname, email, password):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password
    
    def __repr__(self):
        """Convenience method to show info on user"""    
        return f"<Customer: {self.firstname} {self.lastname}, {self.password}>"

def read_customers_from_file(filepath):
    """Read customers from file and populate dictionary of customers.
    Dictionary will be {email: Customer object}
    """
    
    customers = {}
    
    with open(filepath) as file:
        for line in file:
            firstname, lastname, email, password = line.strip().split("|")
            customers[email] = Customer(firstname, lastname, email, password)
            
    return customers

def get_by_email(email):
    """Given an email address, return matching customer."""
    return customers[email]

customers = read_customers_from_file("customers.txt")