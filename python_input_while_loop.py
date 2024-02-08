#!/usr/bin/python3


# # Rental car.
# rental_car = input("What kind of rental do you want? ")

# if rental_car == 'bmw':
#     print(f"Let me see if I can find you a {rental_car.upper()}.")
# else:
#     print(f"Let me see if I can find you a {rental_car.title()}.")

# # Restaurant seating
# number_dinner_group = input("How many people are in your dinner group? ")
# number_dinner_group = int(number_dinner_group)

# if number_dinner_group > 8:
#     print("They'll have to wait for a table.")
# else:
#     print("Their table is ready")

# # Multiples of ten
# multiple_of_ten = input("Enter a number please: ")
# multiple_of_ten = int(multiple_of_ten)

# if multiple_of_ten % 10 != 0:
#     print(f"{multiple_of_ten} is not a multiple of ten.")
# else:
#     print(f"{multiple_of_ten} is a multiple of ten")

# Pizza toppings
# prompt = "\nWhat topping would you like to be added to your pizza? "
# prompt += "\nEnter 'quit' to exit the program. "

# pizza_topping = ""
# while pizza_topping != 'quit':
#     pizza_topping = input(prompt)
    
#     if pizza_topping != 'quit':
#         print(f"I have added {pizza_topping.title()} to your pizza.")

# This is one of the ways to terminate the loop by prompting the user to input 'quit'.

# Another method for exiting the loop is to use a flag. This can help when you have like a game that has multiple conditions that can terminate it.
# prompt = "\nWhat topping would you like to be added to your pizza? "
# prompt += "\nEnter 'quit' to exit the program. "

# active = True # A flag that will help monitor whether or not the program should continue running.
# while active:
#     pizza_topping = input(prompt)

#     if pizza_topping == 'quit':
#         active = False
#     else:
#         print(f"I have added {pizza_topping.title()} to your pizza!")


# We can also use the break statement to exit the while loop.
# prompt = "\nWhat topping would you like to be added to your pizza? "
# prompt += "\nEnter 'quit' to exit the program. "

# while True:
#     pizza_topping = input(prompt)

#     if pizza_topping == 'quit':
#         break
#     else:
#         print(pizza_topping)


# # Movie tickets
# print("Welcome to Africanus Movie Theater! You will tell us your age and \nwe will tell you how much you must pay for your movie ticket.")
# prompt = "\nWhat is your age? "

# active = True
# while active:
#     age = input(prompt)


#     if age == 'quit':
#         active = False
#     else:
#         if int(age) < 3:
#             print("Your ticket is free.")
#         elif int(age) >= 3 and int(age) <= 12:
#             print("Your ticket costs $10.")
#         else:
#             print("Your ticket costs $15")


# # Using a while loop to move items from one list, unconfirmed users, to another list,confirmed users.

# unconfirmed_users = ['robin', 'hirwa', 'nkubito'] # List of unconfirmed users
# confirmed_users = [] # Empty list that will store confirmed users

# # We loop through our list as we verify each user using the while loop while we also add the verified users to the confirmed users list.
# while unconfirmed_users: # This means as long as the unconfirmed users list is not empty since we can't loop through an empty list.
#     current_user = unconfirmed_users.pop() # We remove the last item from the unconfirmed users list and store it in the current_users variable.
    
#     # Verifying each user and adding them to the confirmed_users list
#     print(f"Verifying user: {current_user.title()}")
#     confirmed_users.append(current_user)


# # Displaying the confirmed users
# print("\nThe following users have been confirmed:")
# for confirmed_user in confirmed_users:
#     print(confirmed_user.title())


# # Using a while loop and the remove method to remove all instances of a value from a list.

# # A list of pets with the value 'cat' appearing several times.
# pets = ['dog', 'rabbit', 'mouse', 'cat', 'goldfish', 'cat', 'dog']

# # Looping throught the list to remove all the instances of the 'cat' value.
# while 'cat' in pets:
#     pets.remove('cat')

# print(pets)

# # Using a while loop to fill a dictionary using input().

# # Creating a poll that takes responses from various users about what countries they would like to visit and storing the individual responses in a dictionary.

# responses = {} # empty dictionary to store individual responses from the poll.

# # A flag to help us monitor the polling process.
# polling_active = True

# # A while loop that collects responses from various individuals.
# while polling_active:
#     # Prompting the person's name and response.
#     name = input("\nWhat is your name? ")
#     response = input("What country would you like to visit? ")

#     # Store the response in the dictionary.
#     responses[name] = response

#     # Check whether there's anyone who wants to take the poll.
#     repeat = input("Would you like to let another person respond? (yes/no) ")
#     if repeat == 'no':
#         polling_active = False

# # Displaying the polling results.
# print("\n--- Poll results ---")
# print(responses)
# for name, response in responses.items():
#     print(f"\n{name.title()} would like to visit {response.title()}")


# # Deli exercise about sandwiches orders and finished sandwiches.

# # Sandwiches ordered
# sandwich_orders = ['pastrami', 'american club', 'tuna', 'combination', 'simple']
# # Empty sandwiches to represent finished sandwiches
# finished_sandwiches = []

# # Looping through the sandwich_orders list and printing a message for each order.
# for sandwich_order in sandwich_orders:
#     print(f"I made your {sandwich_order} sandwich.")
#     # Moving each sandwich made to the list of finished sandwiches. This is the same as saying moving sandwichers from the sandwich_orders list to the finished_sandwiches.
#     finished_sandwiches.append(sandwich_order)

# #Display the sandwiches made.    
# print("\nThe following sandwiches were made:")
# for finished_sandwich in finished_sandwiches:
#     print(f"{finished_sandwich}")


# # No pastrami.
# # Sandwiches ordered
# print("The Deli has run out of pastrami!")
# sandwich_orders = ['pastrami', 'american club', 'tuna', 'pastrami', 'combination', 'pastrami', 'simple']
# # Empty sandwiches to represent finished sandwiches
# finished_sandwiches = []
# # Removing all instances of 'pastrami'
# while 'pastrami' in sandwich_orders:
#     sandwich_orders.remove('pastrami')

# # Looping through the sandwich_orders list and printing a message for each order that's been made.
# for sandwich_order in sandwich_orders:
#     print(f"I made your {sandwich_order} sandwich.")
#     # Moving each sandwich made to the list of finished sandwiches. This is the same as saying moving sandwichers from the sandwich_orders list to the finished_sandwiches.
#     finished_sandwiches.append(sandwich_order)

# # Display the sandwiches made.    
# print("\nThe following sandwiches were made:")
# for finished_sandwich in finished_sandwiches:
#     print(f"{finished_sandwich}")


# A program that polls users about their dream vacation

# # Dictionary to store the results of the poll.
# responses = {}

# # Create a flag to monitor the polling process.
# polling_active = True
# # Use a while loop to poll and store them in the responses dictionary.
# while polling_active:
#     # We prompt the user to input their name and response.
#     name = input("\nWhat is your name? ")
#     response = input("If you could visit one place in the world, where would you go? ")

#     # We store the response in the responses dictionary
#     responses[name] = response

#     # We establish the exiting condition of the loop with the help of the flag.
#     repeat = input("\nWould you like to let others respond? (yes or no) ")
#     if repeat == 'no':
#         polling_active = False


# # Displaying the results of the poll
# print("\n--- Poll results ---")
# for name, response in responses.items():
#     print(f"{name.title()} would like to visit {response.title()}!")


# # Using the continue statement in the while loop

# # Looping through numbers 1-10 and printing the odd numbers only

# current_number = 0

# while current_number < 10:
#     current_number += 1

#     if current_number % 2 == 0:
#         continue

#     print(current_number)