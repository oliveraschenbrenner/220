"""
Name: Oliver Aschenbrenner
sales_force.py

Problem: create a SalesForce class

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from sales_person import SalesPerson


class SalesForce:
    """
    here are the functions inside the SalesForce class
    """
    def __init__(self):
        """
        initializes instance variable, list of SalesPerson
        """
        self.sales_people = []

    def add_data(self, file_name):
        """
        imports information for all salespeople from the specified file. The imported data
        should be added to the sales_people list. Each line of the file will
        contain information in the form <employee_id>, <name>, <sale amount> <sale amount> ...
        """
        with open(file_name, "r") as infile:
            for line in infile:
                each_line = line.split(", ")
                person = SalesPerson(int(each_line[0]), each_line[1])
                sales = each_line[2].split()
                for i in sales:
                    person.enter_sale(float(i))
                self.sales_people.append(person)

    def quota_report(self, quota):
        """
        returns a list, where each element is itself a list of each seller’s employee_id,
        name, total sales, and a boolean value of whether or not they hit the specified
        quota - true if they hit it, false if they did not.
        """
        final_list = []
        for person in self.sales_people:
            second_list = [person.get_id(), person.get_name(),
                           person.total_sales(), person.met_quota(quota)]
            final_list.append(second_list)
        return final_list

    def top_seller(self):
        """
        Returns a list of SalesPerson objects with the highest sales amount.
        If there are no ties, the list should contain one record. In the case of a tie,
        the list should include all of the top sales people.
        """
        maximum = [self.sales_people[0]]
        max_sales = self.sales_people[0].total_sales()
        for person in range(1, len(self.sales_people)):
            if self.sales_people[person].total_sales() == max_sales:
                maximum.append(self.sales_people[person])
            if self.sales_people[person].total_sales() > max_sales:
                max_sales = self.sales_people[person].total_sales()
                for i in maximum:
                    maximum.remove(i)
                maximum.append(self.sales_people[person])
        return maximum

    def individual_sales(self, employee_id):
        """
        returns the SalesPerson with the given employee_id or None if the id does not exist.
        """
        for person in self.sales_people:
            if person.get_id() == employee_id:
                return person
        return None
