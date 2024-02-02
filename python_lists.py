#!/usr/bin/python3

#Printing each item in the list separately using their individual index
# names = ['Boris', 'Gashema', 'Tim', 'Fred']
# names.append('Denis')
# print(f"Hello {names[0]}, how are you doing?")
# names[0] = 'Torrey'
# print(names)
# print(f"Hello {names[0]}, how are you doing?")
# print(f"Hello {names[1]}, how are you doing?")
# print(f"Hello {names[2]}, how are you doing?")
# print(f"Hello {names[3]}, how are you doing?")

#Quotes by different philosophers

# philosophers = ['Bertrand Russell', 'Arthur Schopenhauer', 'Friedrich Nietzche', 'Albert Camus']
# print(f"'Life is a pendulum swinging backward and forward between pain and boredom', {philosophers[1]}.")
# print(f"{philosophers[3]} once said, 'The struggle itself towards the heights is enough to fill a man's heart. One must imagine Sysphuss happy'.")
# print(f"'To understand the actual world as it is, not as it should be, is the beginning of wisdom', said {philosophers[0]}.")
# print(f"One of the famous qoutes by one of the well-renowned German existentialist philosopher of all time,{philosophers[2]}, says that'He who has a why can bear any how'.")

# Adding new elements to an empty list

# friends = []
# friends.append('Torrey')
# friends.append('Gift')
# friends.append('Carlos')
# friends.append('Pacifique')
# friends.append('Rugogwe')
# # inserting a new element into the list at the 3rd position
# friends.insert(2, 'Ted')
# # deleting or removing the newly added item from the list
# # del friends[2]
# # print(friends)

# # we can remove an item from a list and work with it afterwards
# popped_items = []
# popped_items.append(friends.pop(0))
# popped_items.append(friends.pop(3))
# popped_items.append(friends.pop(2))
# print(friends)
# print(popped_items)

# # removing an item from a list using its value
# removed = 'Carlos'
# popped_items.remove(removed)
# print(f"One of my friends, {removed}, has been removed from my list of friends")
# print(popped_items)

# A list of people I can invite for dinner
potential_invites = ['Jonathan', 'Joan', 'Gloria']
print(len(potential_invites))
# # Messages inviting them
# print(f"Hello {potential_invites[0]}, it is my pleasure to invite you to dine with me.")
# print(f"Hello {potential_invites[1]}, it is my pleasure to invite you to dine with me.")
# print(f"Hello {potential_invites[2]}, it is my pleasure to invite you to dine with me.")
# # Message informing about one who won't make it to the dinner
# print(f"Unfortunately, {potential_invites.pop(2)} will not be able to make it tonight.")
# # Replacing them
# replacement = potential_invites.append('Kalisa')

# # New invitations
# print(f"Hello {potential_invites[0]}, it is my pleasure to invite you to dine with me.")
# print(f"Hello {potential_invites[1]}, it is my pleasure to invite you to dine with me.")
# print(f"Hello {potential_invites[2]}, it is my pleasure to invite you to dine with me.")

# # Informing people that I've got a new table
# print("Hello, it is with great excitement to announce to you that we have now got a new bigger dinner table which now will help us invite as many guests as possible.")

# # Adding new guests
# potential_invites.insert(0, 'Samir')
# potential_invites.insert(1, 'Jed')
# potential_invites.insert(2, 'Elysee')

# # New invitations
# print(f"Hello {potential_invites[0]}, it is my pleasure to invite you to dine with me.")
# print(f"Hello {potential_invites[1]}, it is my pleasure to invite you to dine with me.")
# print(f"Hello {potential_invites[2]}, it is my pleasure to invite you to dine with me.")
# print(f"Hello {potential_invites[3]}, it is my pleasure to invite you to dine with me.")
# print(f"Hello {potential_invites[4]}, it is my pleasure to invite you to dine with me.")
# print(f"Hello {potential_invites[5]}, it is my pleasure to invite you to dine with me.")

# # Announcement about a change of plans regarding the number of invitations
# print("Unfortunately, our new bigger dinner table won't arrive very soon hence us being force to reduce the number of invitations to only two. We are deeply sorry for such an inconvenience.")

# # Announcing to those whose invitation has been cancelled.
# print(f"Sorry {potential_invites.pop(0)}, your invitation has been cancelled.")
# print(f"Sorry {potential_invites.pop(1)}, your invitation has been cancelled.")
# print(f"Sorry {potential_invites.pop(2)}, your invitation has been cancelled.")
# print(f"Sorry {potential_invites.pop(0)}, your invitation has been cancelled.")

# # Announcing to those who are still invited.
# print(f"Hello {potential_invites[0]}, you are still invited.")
# print(f"Hello {potential_invites[1]}, you are still invited.")

# # Making our list empty
# del potential_invites[0]
# del potential_invites[0]
# print(potential_invites)

# # A list of places I would like to visit some day.
# places = ['giza', 'nyungwe', 'birunga', 'akagera']
# print(places)

# # Printing the list in alphabetical order using the sorted() function without necessarily modifying the old list
# print(sorted(places))
# print(places)

# # Printing the list in reverse alphabetical order using sorted() function without necessarily modifying the old list.

# print(sorted(places, reverse=True))
# print(places)

# # Reversing the order of our list using the reverse() method.
# places.reverse()
# print(places)

# # Re-reversing our list
# places.reverse()
# print(places)

# # Changing our list so that it's stored in alphabetical order using the sort() method. This permanently changes the original list.

# places.sort()
# print(places)

# # Storing our list in a reverse-alphabetical order using the sort() method. We use reverse=True as an argument.
# places.sort(reverse=True)
# print(places)