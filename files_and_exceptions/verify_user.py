#!/usr/bin/python3

from pathlib import Path
import json

def get_stored_username(path):
    """ Get stored username if available """
    if path.exists():   
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None

def get_new_username(path):
    """ Prompts for a new username """
    username = input("What is your name? ")
    contents = json.dumps(username.title())
    path.write_text(contents)
    return username

def greet_user():
    path = Path('username.json')
    username = get_stored_username(path)

    if username:
        correct_user = input(f"Are you {username}? (Enter 'yes' or 'no') ")
        if correct_user == 'yes':
            print(f"Welcome back, {username}!")
            return
        
        
    # Incorrect username, prompt for a new username
        username = get_new_username(path)
        print(f"We'll remember you when you come back, {username.title()}!")

greet_user()