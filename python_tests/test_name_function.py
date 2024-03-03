#!/usr/bin/python3

from name_function import get_formatted_name

def test_first_last_name():
    """ Does the function work for names like 'Kenza Mugabo'? """
    formatted_name = get_formatted_name('kenza', 'mugabo')
    assert formatted_name == 'Kenza Mugabo'

def test_first_last_middle_name():
    """ Does the function work for name like 'Paul Ntawukamenya Palvis'? """
    formatted_name = get_formatted_name('paul', 'palvis', 'ntawukamenya')
    assert formatted_name == 'Paul Ntawukamenya Palvis'