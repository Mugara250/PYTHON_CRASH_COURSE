#!/usr/bin/python3

def get_formatted(city, country, population=''):
    """ Returns a neatly formatted string in the form City, Country """
    if population:
        formatted = f"{city.title()}, {country.title()} - population {population}"
    else:
        formatted = f"{city.title()}, {country.title()}"
    return formatted