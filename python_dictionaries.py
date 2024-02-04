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
favourite_languages = {
    'boris': 'javaScript',
    'manzi': 'c',
    'jean paul': 'python',
    'rukundo': 'javascript',
}

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

# Looping through all the values using the values() method
print('The following languages have been polled:')
for language in set(favourite_languages):
    print(language.title())
# The values() method doesn't take into account the repeated values. Therefore, in order to avoid repetition, we use the set() method. A set is a collection of of unique items.