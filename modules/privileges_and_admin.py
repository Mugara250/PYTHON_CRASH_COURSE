# Importing the user module into this module so as to have class User defined
from user_module import User
""" A set of classes representing the admin user and their privileges """
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

# Privileges class
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
