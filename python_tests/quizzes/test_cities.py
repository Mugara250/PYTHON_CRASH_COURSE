#!/usr/bin/python3

from city_functions import get_formatted

def test_city_country():
    """ Does the function work for 'Santiago, Chile'? """
    formatted = get_formatted('santiago', 'chile')
    assert formatted == 'Santiago, Chile'

def test_city_country_population():
    """ Does the function work for 'Santiago, Chile - population 50000000'? """
    formatted = get_formatted('santiago', 'chile', '50000000')
    assert formatted == 'Santiago, Chile - population 50000000'