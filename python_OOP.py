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

# # Users
# class User:
#     """ Representing a user """

#     def __init__(self, first_name, last_name, age, email, phone_number):
#         """ Initializing our class attributes """
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         self.email = email
#         self.phone_number = phone_number

#     def describe_user(self):
#         """ Summarizing user information """
#         print("\nUser's information: ")
#         print(f"\nFirst Name: {self.first_name.title()}")
#         print(f"Last Name: {self.last_name.title()}")
#         print(f"Age: {self.age}")
#         print(f"Email: {self.email}")
#         print(f"Phone number: {self.phone_number}")

#     def greet_user(self):
#         """ Printing a personalized message to each user """
#         self.full_name = f"{self.first_name.title()} {self.last_name.title()}"
#         print(f"\nHello {self.full_name}")

# # Creating instances representing different users
# user_0 = User('tariq', 'mico', 22, 'tarigmic@gmail.com', +1_345_445_555)
# user_0.describe_user()
# user_0.greet_user()
# user_1 = User('victor', 'kanyangira', 23, 'vickanya@gmail.com', +1_043_400_555)
# user_1.describe_user()
# user_1.greet_user()
# user_2 = User('chris', 'mugabo', 22, 'chrismug@gmail.com', +1_343_485_555)
# user_2.describe_user()
# user_2.greet_user()

# # Number Served
# class Restaurant:
#     """ Modeling a restaurant """

#     def __init__(self, restaurant_name, cuisine_type):
#         """ Initializing our class attributes """
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#         self.number_served = 0

#     def describe_restaurant(self):
#         """ Displaying information about the restaurant """
#         print(f"\n{self.restaurant_name} restaurant cooks {self.cuisine_type} cuisine.")

#     def open_restaurant(self):
#         """ Restaurant is open """
#         print(f"\n{self.restaurant_name} restaurant is open!")

#     def set_number_served(self, number_served):
#         """ Set the number of customers been served """
#         self.number_served = number_served

#     def increment_number_served(self, number_served):
#         """ Increments the number of customers been served """
#         self.number_served += number_served

# # Modifying the number_served attribute directly
# restaurant = Restaurant('Ubumwe', 'Rwandan')
# print(f"Number of customers served: {restaurant.number_served}")
# restaurant.number_served = 3
# print(f"Number of customers served: {restaurant.number_served}")

# # Modifying the number_served attribute using the set_number_served() method
# restaurant.set_number_served(5)
# print(f"Number of customers served: {restaurant.number_served}")

# # Increasing the number of customers who've been served using the increment_number_served method
# restaurant.increment_number_served(3)
# print(f"Number of customers served: {restaurant.number_served}")

# # Login Attempts
# class User:
#     """ Representing a user """

#     def __init__(self, first_name, last_name, age, email, phone_number):
#         """ Initializing our class attributes """
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         self.email = email
#         self.phone_number = phone_number
#         self.login_attempts = 0

#     def describe_user(self):
#         """ Summarizing user information """
#         print("\nUser's information: ")
#         print(f"\nFirst Name: {self.first_name.title()}")
#         print(f"Last Name: {self.last_name.title()}")
#         print(f"Age: {self.age}")
#         print(f"Email: {self.email}")
#         print(f"Phone number: {self.phone_number}")

#     def greet_user(self):
#         """ Printing a personalized message to each user """
#         self.full_name = f"{self.first_name.title()} {self.last_name.title()}"
#         print(f"\nHello {self.full_name}")

#     def increment_login_attempts(self):
#         """ Increments the value of login_attempts by 1"""
#         self.login_attempts += 1

#     def reset_login_attempts(self):
#         """ Resets the value of login_attempts to 0 """
#         self.login_attempts = 0


# # Creating instances
# user_0 = User('rugogwe', 'thierry', 23, 'rugothierry@gmail.com', +250_789_034_577)
# print(user_0.login_attempts)
# # Calling the increment_login_attempts() several times to increase the value of login_attempts
# user_0.increment_login_attempts()
# print(user_0.login_attempts)
# user_0.increment_login_attempts()
# print(user_0.login_attempts)
# user_0.increment_login_attempts()
# print(user_0.login_attempts)
# user_0.increment_login_attempts()
# print(user_0.login_attempts)
# # Resetting the value of login_attempts to 0 using reset_login_attempts() method 
# user_0.reset_login_attempts()
# print(user_0.login_attempts)

# # Ice Cream Stand
# class Restaurant:
#     """ Modeling a restaurant """

#     def __init__(self, restaurant_name, cuisine_type):
#         """ Initializing our class attributes """
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#         self.number_served = 0

#     def describe_restaurant(self):
#         """ Displaying information about the restaurant """
#         print(f"\n{self.restaurant_name} restaurant cooks {self.cuisine_type} cuisine.")

#     def open_restaurant(self):
#         """ Restaurant is open """
#         print(f"\n{self.restaurant_name} restaurant is open!")

#     def set_number_served(self, number_served):
#         """ Set the number of customers been served """
#         self.number_served = number_served

#     def increment_number_served(self, number_served):
#         """ Increments the number of customers been served """
#         self.number_served += number_served

# # Creating a new class IceCreamStand based on the Restaurant class
# class IceCreamStand(Restaurant):
#     """ Representing a specific kind of restaurant called ice cream stand """
#     def __init__(self, restaurant_name, cuisine_type):
#         """ Initializing attributes of the Restaurant class and 
#         making them available in the IceCreamStand class.
#         Initializing attributes specific to the IceCreamStand class or ice cream stand restaurant.
#           """
#         super().__init__(restaurant_name, cuisine_type)
#         self.flavors = ['vanilla', 'avocado', 'mango', 'chocolate', 'blueberry']

#     def show_flavors(self):
#         print("The following is a list of ice cream flavors: ")
#         for flavor in self.flavors:
#             print(f"\t-{flavor}")

# # Creating an instance of our IceCreamStand and calling the show_flavors method
# ice_cream_stand = IceCreamStand('Ubumwe', 'Rwandan')
# ice_cream_stand.show_flavors()

# Admin
# class User:
#     """ Representing a user """

#     def __init__(self, first_name, last_name, age, email, phone_number):
#         """ Initializing our class attributes """
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         self.email = email
#         self.phone_number = phone_number
#         self.login_attempts = 0

#     def describe_user(self):
#         """ Summarizing user information """
#         print("\nUser's information: ")
#         print(f"\nFirst Name: {self.first_name.title()}")
#         print(f"Last Name: {self.last_name.title()}")
#         print(f"Age: {self.age}")
#         print(f"Email: {self.email}")
#         print(f"Phone number: {self.phone_number}")

#     def greet_user(self):
#         """ Printing a personalized message to each user """
#         self.full_name = f"{self.first_name.title()} {self.last_name.title()}"
#         print(f"\nHello {self.full_name}")

#     def increment_login_attempts(self):
#         """ Increments the value of login_attempts by 1"""
#         self.login_attempts += 1

#     def reset_login_attempts(self):
#         """ Resets the value of login_attempts to 0 """
#         self.login_attempts = 0

# # Creating an Admin class based on the User class
# class Admin(User):
#     """ Representing a specific kind of a user called admin using the Admin class """
#     def __init__(self, first_name, last_name, age, email, phone_number):
#         """ Initializing attributes of the User class and making them 
#         available in the Admin class.
#         Creating new attributes specific to the Admin class
#         """
#         super().__init__(first_name, last_name, age, email, phone_number)
#         self.privileges = ['can add post', 'can delete post', 'can ban user']
    
#     def show_privileges(self):
#         """ Lists administrator's set of privileges """
#         print("The admnistrator's privileges are:")
#         for privilege in self.privileges:
#             print(f"\n - {privilege}")

# # Creating an instance of Admin and calling the show_privileges() method
# user_0 = Admin('Paul', 'Palvis', 20, 'paulpal@gmail.com', +250_890_234_456)
# user_0.show_privileges()    
        

# # Privileges
# class User:
#     """ Representing a user """

#     def __init__(self, first_name, last_name, age, email, phone_number):
#         """ Initializing our class attributes """
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         self.email = email
#         self.phone_number = phone_number
#         self.login_attempts = 0

#     def describe_user(self):
#         """ Summarizing user information """
#         print("\nUser's information: ")
#         print(f"\nFirst Name: {self.first_name.title()}")
#         print(f"Last Name: {self.last_name.title()}")
#         print(f"Age: {self.age}")
#         print(f"Email: {self.email}")
#         print(f"Phone number: {self.phone_number}")

#     def greet_user(self):
#         """ Printing a personalized message to each user """
#         self.full_name = f"{self.first_name.title()} {self.last_name.title()}"
#         print(f"\nHello {self.full_name}")

#     def increment_login_attempts(self):
#         """ Increments the value of login_attempts by 1"""
#         self.login_attempts += 1

#     def reset_login_attempts(self):
#         """ Resets the value of login_attempts to 0 """
#         self.login_attempts = 0

# # Creating the Privileges class that will be used whose instance will be used as an attribute in the Admin class
# class Privileges():
#     """ Representing Admin privileges """
#     def __init__(self):
#         """ Initializing class attribute(s) """
#         self.privileges = ['can add post', 'can delete post', 'can ban user']
#     def show_privileges(self):
#         """ Lists administrator's set of privileges """
#         print("The admnistrator's privileges are:")
#         for privilege in self.privileges:
#             print(f"\n - {privilege}")

# class Admin(User):
#     """ Representing a specific kind of a user called admin using the Admin class """
#     def __init__(self, first_name, last_name, age, email, phone_number):
#         """ Initializing attributes of the User class and making them 
#         available in the Admin class.
#         Creating new attributes specific to the Admin class
#         """
#         super().__init__(first_name, last_name, age, email, phone_number)
#         self.privileges = Privileges()

# # Creating an instance of Admin and calling the show_privileges() method
# user_0 = Admin('Paul', 'Palvis', 20, 'paulpal@gmail.com', +250_890_234_456)
# user_0.privileges.show_privileges()    


# # Car
# class Car():
#     """ Modelling a car """

#     def __init__(self, brand, model, year):
#         """ Initializing attributes of our Car class """
#         self.brand = brand
#         self.model = model
#         self.year = year

#     def describe_car(self):
#         """ Describing the car """
#         fullname = f"{self.brand.title()} {self.model.title()} {self.year}"
#         return fullname

# # Create a separate Battery class and use its instance as an attribute of the ElectricCar class
# class Battery():
#     """ Modelling a battery for an electric car """

#     def __init__(self, battery_power=35):
#         """ Initializing the battery's attributes """
#         self.battery_power = battery_power

#     # Define other methods specific to the battery
    
#     # Increments battery power
#     def increment_battery_power(self, number):
#         """ Incrementing battery power """
#         self.battery_power += number

#     # Battery range according to its power
#     def get_range(self):
#         """ Prints a statement about the car's range based on it's battery power """
#         if self.battery_power == 35:
#             range = 140
#         elif self.battery_power == 65:
#             range = 220

#         print(f"This car can go about {range} miles on a full charge.")

#     # Upgrade
#     def upgrade_battery_power(self):
#         """ Checks the battery size and sets the power to 70 if it isn't already """
#         if self.battery_power < 65:
#             self.battery_power = 65
#     def describe_battery(self):
#         """ Describing the car's battery """
#         print(f"The car's battery power is {self.battery_power}-kwH.")

# # Creating an ElectricCar class based on the Car class
# class ElectricCar(Car):
#     """ Modelling aspects of a car, specific to electric vehicles """

#     def __init__(self, brand, model, year):
#         """ Initializing the attributes of the Car class and 
#         making them available in the ElectricCar class.
#         Creating new attributes specific to the ElectricCar class.
#         """
#         super().__init__(brand, model, year)
#         self.battery_power = Battery()


#     # Overriding methods from the Car class e.g fill_gas_tank().
#     def fill_gas_tank(self):
#         """ Electric cars don't have gas tanks """
#         print("This car doesn't have a gas tank.")

    
# # Creating an instance of the ElectricCar class and calling the show_battery() method
# car = ElectricCar('tesla', 'model 3', 2023)
# print(car.describe_car())
# car.battery_power.describe_battery()
# car.battery_power.get_range()
# car.battery_power.upgrade_battery_power()
# car.battery_power.describe_battery()
# car.battery_power.get_range()


# Dice
# Importing the module we will need in our program
from random import randint
class Die:
    """ Representing a die """
    def __init__(self, sides=6):
        """ Initializing class attributes """
        self.sides = sides

    def roll_die(self):
        """A method that prints a random number between 1 and the
        number of sides the die has.
        """
        print(randint(1,self.sides))



# # Making a 6-sided die and rolling it 10 times
# die = Die()
# die.roll_die()
# die.roll_die()
# die.roll_die()
# die.roll_die()
# die.roll_die()
# die.roll_die()
# die.roll_die()
# die.roll_die()
# die.roll_die()
# die.roll_die()
# die.roll_die()

# # Making 10-sided die and rolling it 10 times.
# die_10 = Die(10)
# die_10.roll_die()
# die_10.roll_die()
# die_10.roll_die()
# die_10.roll_die()
# die_10.roll_die()
# die_10.roll_die()
# die_10.roll_die()
# die_10.roll_die()
# die_10.roll_die()
# die_10.roll_die()
# die_10.roll_die()

# # Making a 20-sided die and rolling it 10 times.
# die_20 = Die(20)
# die_20.roll_die()
# die_20.roll_die()
# die_20.roll_die()
# die_20.roll_die()
# die_20.roll_die()
# die_20.roll_die()
# die_20.roll_die()
# die_20.roll_die()
# die_20.roll_die()
# die_20.roll_die()
# die_20.roll_die()


# Lottery
        