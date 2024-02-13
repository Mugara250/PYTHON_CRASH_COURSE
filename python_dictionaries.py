#!/usr/bin/python3

# Dictionary storing information about Joslyn Manzi
# person = {
#     'first_name': 'Joslyn',
#     'second_name': 'Manzi',
#     'age': '22',
#     'city': 'Kigali',
# }

# print(person['first_name'])
# print(person['second_name'])
# print(person['age'])
# print(person['city'])

# People's favorite numbers
# favorite_numbers = {
#     'Nicholas': 4,
#     'Thierry': 7,
#     'Beni': 8,
#     'Tony': 9,
#     'Lee': 10,
# }

# print(f'Nicholas: {favorite_numbers["Nicholas"]}')
# print(f'Thierry: {favorite_numbers["Thierry"]}')
# print(f'Beni: {favorite_numbers["Beni"]}')
# print(f'Tony: {favorite_numbers["Tony"]}')
# print(f'Lee: {favorite_numbers["Lee"]}')

# Glossary
# glossary = {
#     'conditional test': 'an expression that can evaluated as "True" or "False".',
#     'dictionary': 'a collection of key-value pairs.',
#     'list': 'a collection of items in a particular order',
#     'tuple': "a list with (). It is used to store values that can't be changed.",
#     'append()': 'an inbuilt Python that adds a new item to a list.'
# }

# print(f'conditional test:\n{glossary["conditional test"]}')
# print(f'dictionary:\n{glossary["dictionary"]}')
# print(f'list:\n{glossary["list"]}')
# print(f'tuple:\n{glossary["tuple"]}')
# print(f'append():\n{glossary["append()"]}')

# A dictionary containing individuals' favorite programming languages
# favourite_languages = {
#     'boris': 'python',
#     'manzi': 'c',
#     'jean paul': 'javascript',
#     'rukundo': 'python',
# }

# Looping through all the key-value pairs of the above dictionary
# for name, language in favourite_languages.items():
#     print(f"{name.title()}'s favourite language is {language.title()}.")


# Looping through all the keys of the favourite_languages dictionary
# for name in favourite_languages.keys():
#     print(name.title())

# Accessing the value of the keys insided the loop by using the current key
# friends = ['manzi', 'boris']
# for name in favourite_languages.keys():
#     print(f"Hey {name.title()}")

#     if name in friends:
#         language = favourite_languages[name].title()
#         print(f"\t{name.title()}, I see you love {language}")

# Checking if a certain individual was polled
# if 'clemence' not in favourite_languages.keys():
#     print("Clemence, please take our poll!")

# Looping through all keys in order using the sorted() method
# for name in sorted(favourite_languages.keys()):
#     print(f"{name.title()}, thank you for taking the poll.")

# # Looping through all the values using the values() method
# print('The following languages have been polled:')
# for language in set(favourite_languages.values()):
#     print(language.title())
# The values() method doesn't take into account the repeated values. Therefore, in order to avoid repetition, we use the set() method. A set is a collection of of unique items.

# # Glossary
# glossary = {
#     'conditional test': 'an expression that can evaluated as "True" or "False".',
#     'dictionary': 'a collection of key-value pairs.',
#     'list': 'a collection of items in a particular order',
#     'tuple': "a list with (). It is used to store values that can't be changed.",
#     'append()': 'an inbuilt Python method that adds a new item to a list.',
#     'set': 'a collection of unique items.',
#     'values()': 'an inbuilt Python method that returns values from a dictionary without their associated keys.',
#     'keys()': 'an inbuilt Python method that returns a sequence of keys from a dictionary.',
#     'items()': 'an inbuilt Python method that returns a sequence of key-value pairs from a dictionary.',
#     'variable': "a label assigned to a value which helps in referencing it once there's a need to access it",
# }

# for term, definition in glossary.items():
#     print(f"Term: {term}")
#     print(f"Definition: {definition}\n")

# Rivers 
# rivers = {
#     'nile': 'sudan',
#     'congo': 'drc',
#     'niger': 'nigeria',
# }

# Loop that prints a sentence about each river.
# for river, country in rivers.items():
#         if country == 'drc':
#                 print(f"The {river.title()} river runs through {country.upper()}")
#         else:
#                 print(f"The {river.title()} river runs through {country.title()}")


# Loop that prints the name of each river in the dictionary.
# for river in rivers:
#     print(river.title())


# Loop that prints the name of each country in the dictionary.
# for country in rivers.values():
#     if country == 'drc':
#         print(country.upper())
#     else:
#         print(country.title())


# Poll of favourite programming languages
# favourite_languages = {
#     'boris': 'javascript',
#     'manzi': 'c',
#     'jean paul': 'python',
#     'rukundo': 'javascript',
# }

# for language in set(favourite_languages.values()):
#     print(language.title())

# # People who should take the poll.
# pollers = ['boris', 'robert', 'manzi', 'john']

# # Looping through the above list.
# for poller in pollers:
#     if poller in favourite_languages:
#         print(f"{poller.title()}, thank you for responding.")
#     else:
#         print(f"{poller.title()}, take the poll please!")


# Information about different people.
# people_info = {
#     'person_1': {
#         'first_name': 'joslyn',
#         'last_name': 'karenzi',
#         'city': 'kigali',
#     },
#     'person_2': {
#         'first_name': 'boris',
#         'last_name': 'nyilindekwe',
#         'city': 'kampala',
#     },
#     'person_3': {
#         'first_name': 'fred',
#         'last_name': 'ndahiro',
#         'city': 'vancouver',
#     },
# }

# for person, personal_info in people_info.items():
#     print(f"\n{person.title()}")
#     full_name = f"{personal_info['first_name']} {personal_info['last_name']}"
#     location = personal_info['city']

#     print(f"\tFull name: {full_name.title()}")
#     print(f"\tLocation: {location.title()}")

# A list with dictionaries which contain information about pets.
# pet_0 = {
#     'name': 'max',
#     'animal': 'dog',
#     'owner': 'golbert',
# }

# pet_1 = {
#     'name': 'babu',
#     'animal': 'rabbit',
#     'owner': 'delice',
# }

# pet_2 = {
#     'name': 'shito',
#     'animal': 'mouse',
#     'owner': 'angelo',
# }

# pet_3 = {
#     'name': 'titi',
#     'animal': 'cat',
#     'owner': 'liza',
# }

# pet_4 = {
#     'name': 'vipora',
#     'animal': 'snake',
#     'owner': 'rusibana',
# }

# pets = [pet_0, pet_1, pet_2, pet_3, pet_4]

# for pet in pets:
#     print(f"\nPet:")
#     print(f"\tName: {pet['name'].title()}")
#     print(f"\tType of animal: {pet['animal'].title()}")
#     print(f"\tName: {pet['name'].title()}")

# Favorite places
# favorite_places = {
#     'peter': ['paris', 'montreal', 'nairobi'],
#     'lorna': ['gisenyi', 'convention', 'miami'],
#     'yvonne': ['marriot', 'papyrus', 'dubai'],
# }

# for person, places in favorite_places.items():
#     print(f"\n{person.title()}:")
#     for place in places:
#         print(f"\n\t{place.title()}")

# People's favorite numbers
# favorite_numbers = {
#     'nicholas': [4, 5, 9],
#     'thierry': [7, 3],
#     'beni': [1, 3, 5],
#     'tony': [9, 4, 12],
#     'lee': [5, 13, 5, 8],
# }

# for person, numbers in favorite_numbers.items():
#     print(f"\n{person.title()}'s favorite numbers are:")
#     for number in numbers:
#         print(f"\n\t{number}")


# Cities
cities = {
    'kigali': {
        'country': 'rwanda',
        'population': '1_288_000',
        'fact': 'one of the cleanest cities in Africa',
    },
    'new York': {
        'country': 'usa',
        'population': '8_335_897 ',
        'fact': 'one of the most culturally diverse city in the world.',
    },
    'vatican': {
        'country': 'vatican',
        'population': '764',
        'fact': 'residence of the Pope',
    },
}

for city, city_info in cities.items():

    if city_info['country'] == 'usa':
        print(f"\n{city.title()}:")
        print(f"\n\t{city_info['country'].upper()}")
        print(f"\n\t{city_info['population']}")
        print(f"\n\t{city_info['fact'].title()}")
    else:
        print(f"\n{city.title()}:")
        print(f"\n\t{city_info['country'].title()}")
        print(f"\n\t{city_info['population']}")
        print(f"\n\t{city_info['fact'].title()}")
    