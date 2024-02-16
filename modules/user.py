""" A set of classes used to represent a user and an admin """
class User:
    """ Representing a user """

    def __init__(self, first_name, last_name, age, email, phone_number):
        """ Initializing our class attributes """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.phone_number = phone_number
        self.login_attempts = 0

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

    def increment_login_attempts(self):
        """ Increments the value of login_attempts by 1"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """ Resets the value of login_attempts to 0 """
        self.login_attempts = 0


# Creating the Privileges class that will be used whose instance will be used as an attribute in the Admin class
class Privileges():
    """ Representing Admin privileges """
    def __init__(self):
        """ Initializing class attribute(s) """
        self.privileges = ['can add post', 'can delete post', 'can ban user']
    def show_privileges(self):
        """ Lists administrator's set of privileges """
        print("The admnistrator's privileges are:")
        for privilege in self.privileges:
            print(f"\n - {privilege}")


# Creating an Admin class based on the User class
class Admin(User):
    """ Representing a specific kind of a user called admin using the Admin class """
    def __init__(self, first_name, last_name, age, email, phone_number):
        """ Initializing attributes of the User class and making them 
        available in the Admin class.
        Creating new attributes specific to the Admin class
        """
        super().__init__(first_name, last_name, age, email, phone_number)
        self.privileges = Privileges()
    
    def show_privileges(self):
        """ Lists administrator's set of privileges """
        print("The admnistrator's privileges are:")
        for privilege in self.privileges:
            print(f"\n - {privilege}")
