"""
Name: Oliver Aschenbrenner
sales_person.py

Problem: create a salesperson class

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


class SalesPerson:
    """
    here are functions inside the SalesPerson class, starting with __init__
    """
    def __init__(self, employee_id, name):
        """
        here are the instance variables
        """
        self.employee_id = employee_id
        self.name = name
        self.sales = []

    def get_id(self):
        """
        returns the sales person’s employee_id
        """
        return self.employee_id

    def get_name(self):
        """
        returns the sales person's name
        """
        return self.name

    def set_name(self, name):
        """
        sets the sales person’s name
        """
        self.name = name

    def enter_sale(self, sale):
        """
        adds the value of sale to the sales list
        """
        self.sales.append(sale)

    def total_sales(self):
        """
        returns the sum of the sales person’s sales
        """
        acc = 0
        for i in self.sales:
            acc = acc + i
        return acc

    def get_sales(self):
        """
        returns the list of sales
        """
        return self.sales

    def met_quota(self, quota):
        """
        returns True if the total sales meet or exceed the quota provided, otherwise returns False
        """
        if self.total_sales() >= quota:
            return True
        return False

    def compare_to(self, other):
        """
        other is another SalesPerson. returns -1 if other has more in total sales than self,
        1 if self has more in total sales than other, and 0 if their total sales are the same
        """
        if other.total_sales() > self.total_sales():
            return -1
        if other.total_sales() < self.total_sales():
            return 1
        return 0

    def __str__(self):
        """
        returns “<employee_id>-<name>: <total sales>”
        """
        return str(str(self.get_id()) + "-" + self.get_name() + ": "
                   + str(self.total_sales()))
