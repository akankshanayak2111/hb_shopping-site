"""Customers at Hackbright."""


class Customer(object):
    """Ubermelon customer."""

    # TODO: need to implement this

    def __init__(self,
                 first_name,
                 last_name,
                 email,
                 password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def __repr__(self):
        """Convenience method to show information about customers."""

        return "<Customer: %s, %s>" % (
            self.first_name, self.last_name)


def read_customer_data_from_file(filepath):

    customer_data = {}

    for line in open(filepath):
        (first_name,
        last_name,
        email,
        password) = line.strip().split("|")

        customer_data[email] = Customer(first_name,
                                        last_name,
                                        email,
                                        password)
    return customer_data


def get_by_email(customer_email):

    return customer_data[customer_email]

customer_data = read_customer_data_from_file("customers.txt")
