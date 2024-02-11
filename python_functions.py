#!/usr/bin/python3

# # Message about what I'm learning about this chapter.
# def message():
#     """ A message about what I'm learning about this chapter """
#     print("Hello, I am currently learning about Python functions. I am specifically learning how to:\n1.Define them.\n2.Call them.\n3.Pass arguments and parameters into them.")

# message()

# # Favorite Book.
# def favorite_book(title):
#     print(f"One of my favorite books is {title.title()}")

# favorite_book('the god delusion')

# # T-shirt
# """ A function that prints the size of a shirt and the message printed on it """
# def make_shirt(size, message):
#     print(f"\nThe shirt's size is '{size}' and the message written on it is\n'{message}'")

# make_shirt('large', 'We are the world.') # Calling the function with positional arguments.
# make_shirt(size='medium', message="\Let's avoid toxic ideas!") # Calling the same function with keyword arguments.

# # Large Shirts.
# """ A function that prints the size of a shirt and the message printed on it """
# def make_shirt(size='large', message='I love Python'):
#     print(f"\nThe shirt's size is '{size}' and the message written on it is\n'{message}'")

# make_shirt()
# make_shirt('medium')
# make_shirt('small', 'Rwanda uri nziza')

# # Cities
# """ A function that displays the name of a city and the country it's located in. """
# def describe_city(name, country='Rwanda'):
#     print(f"\n{name.title()} is in {country.title()}.")

# describe_city('Kigali')
# describe_city('kaduna', 'nigeria')
# describe_city(country="cote d'ivoire", name='abidjan')

# # City names
# """ A function that returns the formatted string of a city and its country. """
# def city_country(city, country):
#     fullname = f"{city}, {country}"
#     return fullname.title()

# # Calling the function with different city-country pairs and printing the returned values.
# result = city_country('new york', 'united states')
# print(result)
# result = city_country('bengaluru', 'india')
# print(result)
# result = city_country('pretoria', 'south africa')
# print(result)

# # Album
# """ A function that returns a dictionary describing an album i.e. the artist's name and the album title """
# def make_album(artist_name, album_title, songs_number=None):
#     if songs_number:
#         album = album = {'artist': artist_name.title(), 'title': album_title.title(), 'songs': songs_number}
#         return album
#     else:
#         album = {'artist': artist_name.title(), 'title': album_title.title()}
#         return album
# # Calling the function with different artist-album pairs and printing the returned values.
# album1 = make_album('kendrick lamar', 'damn')
# print(album1)
# album2 = make_album('burna boy', 'love damini')
# print(album2)
# album3 = make_album('the eagles', 'eagles')
# print(album3)
# album4 = make_album('3 doors down', 'away from the sun', '9')
# print(album4)

# # User Albums
# """ A function that returns a dictionary describing an album i.e. the artist's name and the album title """
# def make_album(artist_name, album_title, songs_number=None):
#     if songs_number:
#         album = album = {'artist': artist_name.title(), 'title': album_title.title(), 'songs': songs_number}
#         return album
#     else:
#         album = {'artist': artist_name.title(), 'title': album_title.title()}
#         return album
    
# # A while loop that will help us collect information from users about an artist and their album title
# while True:
#     print("\nPlease enter the name of any artist you want and the title\nof their album")
#     print("(enter 'q' at any time to quit!)")

#     name_artist = input("Artist's name: ")

#     # We can provide an option for the user to quit the program using the if statement and the break statement as well.
#     if name_artist == 'q':
#         break

#     title_album = input("Album title: ")

#     if title_album == 'q':
#         break

#     # Calling the function to help display the information input by the user in a dictionary format.
#     user_input = make_album(name_artist.title(), title_album.title())
#     print(user_input)


# # Messages
# """ A function that prints text messages stored in a list separately """
# def show_messages(messages):
#     # for loop for looping through the list and printing each message stored in it separately
#     for message in messages:
#         print(message)

# # Creating the list containing messages and calling the function by passing it that list.
# messsages = ['No pain, no gain.', "He who has a 'why' can bear any 'how'.", 'Veni, vidi, vicci.']
# show_messages(messsages)

# # Sending messages
# """ A function that prints each text message and moves each message to a new list called sent_messages """
# # Printing messages.
# def send_messages(messages):
#     sent_messages = []
#     for message in messages:
#         print(f"Sending message: \n{message}")
#         sent_messages.append(message)

#     return sent_messages

# # # Calling the function
# # messages = ['No pain, no gain.', "He who has a 'why' can bear any 'how'.", 'Veni, vidi, vicci.']
# # sent_messages = send_messages(messages)
# # # Printing the lists to make sure the messages were moved correctly
# # print(f"Original list: {messages}")
# # print(f"List of sent messages: {sent_messages}")    
    
# # Archived messages
# # Calling the function send_messages with a copy of the list of messages
# messages = ['No pain, no gain.', "He who has a 'why' can bear any 'how'.", 'Veni, vidi, vicci.']
# sent_messages = send_messages(messages[:])
# # Printing both lists to show that the original list has been retained
# print(f"Original list: {messages}")
# print(f"List of sent messages: {sent_messages}")

# # Sandwiches
# """ A function that accepts a list of items a person wants on a sandwich and prints a summary of the sandwich being ordered """
# def sandwich(*features):
#     """Summarize the sandwich being ordered """
#     print("\nThe sandwich being ordered has the following features: ")
#     for feature in features:
#         print(f"- {feature}")

# # Calling the function three times
# sandwich('vegetables')
# sandwich('spinach', 'cheese')
# sandwich('sausage', 'butter', 'coconuts')

# # User profile
# """ Obtaining user information """
# def build_profile(first, last, **user_info):
#     user_info['first_name'] = first
#     user_info['last_name'] = last
#     return user_info

# # Calling our function
# user_info = build_profile('Mushi', 'Mbonyumugara', age='23', occupation='unemployed')
# print(user_info)

# # Cars
# """ Car informataion """
# def make_car(manufacturer, model, **car_info):
#     car_info['manufacturer_name'] = manufacturer
#     car_info['model_name'] = model
#     return car_info

# # Calling the function
# car_info = make_car('toyota', 'carina', color='dark blue')
# print(car_info)
