""" A class that can be used to represent a car. """
class Restaurant:
    """ Modeling a restaurant """

    def __init__(self, restaurant_name, cuisine_type):
        """ Initializing our class attributes """
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """ Displaying information about the restaurant """
        print(f"\n{self.restaurant_name} restaurant cooks {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        """ Restaurant is open """
        print(f"\n{self.restaurant_name} restaurant is open!")

    def set_number_served(self, number_served):
        """ Set the number of customers been served """
        self.number_served = number_served

    def increment_number_served(self, number_served):
        """ Increments the number of customers been served """
        self.number_served += number_served
