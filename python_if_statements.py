#!/usr/bin/python3

# president_of_Rwanda = "Paul Kagame"
# print("Is the president_of_Rwanda == 'Paul Kagame'? I predict True")
# print(president_of_Rwanda == 'Paul Kagame')

# print("\nIs president_of_Rwanda != 'William Ruto'? I predict True")
# print(president_of_Rwanda != 'William Ruto')

# name = 'Mbonyumugara Mushi'
# user = 'mbonyumugara mushi'
# print((name == 'mbonyumugara mushi') or (user == 'mbonyumugara mushi'))

# veto_powers = ['USA', 'UK', 'France', 'Russia', 'China']
# print('France' not in veto_powers)

# Alien colours
# alien_colour = 'blue'

# if alien_colour == 'green':
#     print('You have just earned 5 points!')
# elif alien_colour == 'yellow':
#     print('You have earned 10 points!')
# elif alien_colour == 'red':
#     print('You have earned 15 points!')
# else:
#     print('You just earned 10 points!')

# Stages of life.
# age = 76

# if age < 2:
#     print('You are a baby!')
# elif age >= 2 and age < 4:
#     print('You are a toddler!')
# elif age >= 4 and age < 13:
#     print('You are a kid!')
# elif age >= 13 and age < 20:
#     print('You are a teenager!')
# elif age >= 20 and age < 65:
#     print('You are an adult!')
# else:
#     print('You are an elder!')

# Favorite fruits
# favorite_fruits = ['avocados', 'passion fruits', 'pineapples']

# if 'avocados' in favorite_fruits:
#     print('You really like avocados!')
# if 'passion fruits' in favorite_fruits:
#     print('You really like passion fruits!')
# if 'pineapples' in favorite_fruits:
#     print('You really like pineapples!')


# Users
# usernames = []

# if usernames:
#     for username in user_names:
#         if username == 'admin':
#             print('Hello admin, would you like a status report?')
#         else:
#             print(f'Hello {username}, thank you for logging in again.')
# else:
#     print('We need to find some users!')


# Checking usernames

# List of current users
current_users = ['Max', 'Emma', 'Ada', 'Mugara', 'Oscar']

# List of new users
new_users = ['Swics', 'Max', 'Matabz', 'Oscar', 'Patos']

## Creating a copy of current_users with lower case names
# current_users_lower = []
# for user in current_users:
#     lower = user.lower()
#     current_users_lower.append(lower)

# print(current_users_lower)

#The above piece of code can be written within one line
current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    # Checking if the lower case version of the new username is in current_users_lower
    if new_user.lower() in current_users_lower:
        print(f'Sorry, the username {new_user} has been used. Enter a new username please!')
    else:
        print(f'The username {new_user} is available')


# Ordinal numbers indicate their positions in a list.
# numbers = range(1, 10)

# for number in numbers:
#     if number == 1:
#         print('1st\n')
#     elif number == 2:
#         print('2nd\n')
#     elif number == 3:
#         print('3rd\n')
#     else:
#         print(f'{number}th\n')
