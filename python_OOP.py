#!/usr/bin/python3

# # Restaurant
# class Restaurant:
#     """ Modeling a restaurant """

#     def __init__(self, restaurant_name, cuisine_type):
#         """ Initializing our class attributes """
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type

#     def describe_restaurant(self):
#         """ Displaying information about the restaurant """
#         print(f"\n{self.restaurant_name} restaurant cooks {self.cuisine_type} cuisine.")
#     def open_restaurant(self):
#         """ Restaurant is open """
#         print(f"\n{self.restaurant_name} restaurant is open!")


# # Making an instance 'restaurant' from our class Restaurant.
# restaurant = Restaurant('Ubumwe', 'Rwandan')
# print(f"{restaurant.restaurant_name} restaurant.")
# print(f"{restaurant.cuisine_type} cuisine.")
# # Calling both class methods
# restaurant.describe_restaurant()
# restaurant.open_restaurant()
        
# Other instances
# restaurant_0 = Restaurant('Chiacchierare', 'Italian')
# restaurant_0.describe_restaurant()
# restaurant_1 = Restaurant('China Moon', 'Chinese')
# restaurant_1.describe_restaurant()
# restaurant_2 = Restaurant('Tuko Pamoja', 'Kenyan')
# restaurant_2.describe_restaurant()

# Users
class User:
    """ Representing a user """

    def __init__(self, first_name, last_name, age, email, phone_number):
        """ Initializing our class attributes """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.phone_number = phone_number

    def describe_user(self):
        """ Summarizing user information """
        print("\nUser's information: ")
        print(f"\nFirst Name: {self.first_name.title()}")
        print(f"Last Name: {self.last_name.title()}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")
        print(f"Phone number: {self.phone_number}")

    def greet_user(self):
        """ Printing a personalized message to each user """
        self.full_name = f"{self.first_name.title()} {self.last_name.title()}"
        print(f"\nHello {self.full_name}")

# Creating instances representing different users
user_0 = User('tariq', 'mico', 22, 'tarigmic@gmail.com', +1_345_445_555)
user_0.describe_user()
user_0.greet_user()
user_1 = User('victor', 'kanyangira', 23, 'vickanya@gmail.com', +1_043_400_555)
user_1.describe_user()
user_1.greet_user()
user_2 = User('chris', 'mugabo', 22, 'chrismug@gmail.com', +1_343_485_555)
user_2.describe_user()
user_2.greet_user()