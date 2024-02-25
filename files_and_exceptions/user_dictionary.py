#!/usr/bin/python3

from pathlib import Path
import json

def get_stored_user_info(path):
    """ Get stored user info if available """
    if path.exists():   
        contents = path.read_text()
        user_info = json.loads(contents)
        return user_info
    else:
        return None

def get_new_user_info(path):
    """ Prompts for a new user info """
    username = input("What is your name? ")
    age = input("What is your age? ")
    location = input("Where are you located? ")

    user_info = {
        'username': username.title(),
        'age' : age,
        'location': location.title(),
    }

    contents = json.dumps(user_info)
    path.write_text(contents)
    return user_info

def greet_user():
    """ Greet user by name, and then tell them more information about them """
    path = Path('user_info.json')
    user_info = get_stored_user_info(path)

    if user_info:
        print(f"Welcome back, {user_info['username']}.")
        print(f"You're {user_info['age']} years old.")
        print(f"You are located in {user_info['location']}.")
    else:
        user_info = get_new_user_info(path)
        print(f"We'll remember you when you come back, {user_info['username']}!")

greet_user()