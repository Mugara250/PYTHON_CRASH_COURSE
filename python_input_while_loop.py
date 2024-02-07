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


# Movie tickets
print("Welcome to Africanus Movie Theater! You will tell us your age and \nwe will tell you how much you must pay for your movie ticket.")
prompt = "\nWhat is your age? "

active = True
while active:
    age = input(prompt)


    if age == 'quit':
        active = False
    else:
        if int(age) < 3:
            print("Your ticket is free.")
        elif int(age) >= 3 and int(age) <= 12:
            print("Your ticket costs $10.")
        else:
            print("Your ticket costs $15")