#!/usr/bin/python3
# A for loop is used when you want to do the same action with every item in a list.
# countries = ['Rwanda', 'Senegal', 'Nigeria', 'Burundi']
# for country in countries: # this line tells Python to retrieve the first value from the list 'countries' and associate it with the variable 'country'.
    # print(country) # This line of code tells Python to then print the retrieved value.
# The above for loop code can be read as "for every country in the list of countries, print the country's name".
#   print(f"{country} is a beautiful country.")
#   print(f"I can't wait to see {country}. \n")

# print("Looking forward to visiting these countries.") # since this line is not indented, it means that it is outside our loop hence being printed once.


# Favorite types of pizzas
# pizzas = ['veggie pizza', 'cheese pizza', 'pepperoni pizza']
# for pizza in pizzas:
#     print(f"I like {pizza.title()}!")

# print("I really love pizza!")

# Animals that have a common characteristic.
# animals = ['tiger', 'lion', 'jaguar', 'panther']
# for animal in animals:
#     print(f"A {animal} is part of the cat family.")

# print("These are animals are part of the same cat family.")

# Counting from 1 to 20, inclusive.
# for number in range(1, 21):
#     print(number)

# List containing numbers from one to one million
# numbers = range(1, 1_000_001)
# print([min(numbers), max(numbers)])
# print(sum(numbers))

# Using the third argument of the range() function to make a list of odd numbers for 1 to 20
# odd_numbers = range(1, 21)
# for number in odd_numbers:
#     print(number)

# Printing the multiples of 3 from 3 to 30.
# multiples_of_three = range(3, 31, 3)
# for number in multiples_of_three:
#     print(number)

# The first ten cubes.
# cubes = []

# numbers = range(1, 11)
# for number in numbers:
#     cube = number ** 3
#     cubes.append(cube)

# for cube in cubes:
#     print(cube)

# Using a list comprehension to generate a list of the first 10 cubes.

# cubes = [number ** 3 for number in range(1, 11)]
# # Slicing a list
# print("Here are the first three cubes:")
# for cube in cubes[:3]:
#     print(cube)

# print("Here are the middle cubes:")
# for cube in cubes[3:7]:
#     print(cube)

# print("Here are the last three cubes:")
# for cube in cubes[7:]:
#     print(cube)
# Using slice to make a new list called natural_number_cubes using the old list cubes

# natural_number_cubes = cubes[:]

# natural_number_cubes.append(1003)
# print(natural_number_cubes)


# Tuple that contains five simple foods (buffet-style restaurants offers only five basic foods)

menu = ('rice', 'kawunga', 'spinach', 'plantains', 'potatoes')
# for food in buffet:
#     print(food)

menu = ('pasta', 'pizza', 'spinach', 'plantains', 'potatoes')
for food in menu:
    print(food)