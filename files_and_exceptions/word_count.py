#!/usr/bin/python3

from pathlib import Path

def count_words(filename):
    """ Count the approximate number of words in a file. """
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        pass
    else:
        # Count the approximate number of words in a file.
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words")

filenames = ['alice.txt', 'siddharta.txt', 'moby_dick.txt']

# Loop that helps us count approximate number of words in multiple files.
for filename in filenames:
    path = Path(filename)
    count_words(path)