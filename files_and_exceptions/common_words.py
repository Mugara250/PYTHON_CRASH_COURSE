#!/usr/bin/python3

from pathlib import Path

def count_common_words(filename, word):
    """ Counts the number of appearances of a word in the text. """
    path = Path(filename)

    try:
        contents = path.read_text()
    except FileNotFoundError:
        pass
    else:
        word_count = contents.lower().count(word)
        print(f"\n'{word}' appears in {filename} about {word_count} times!")


filenames = ['frankenstein.txt', 'pride_and_prejudice.txt', 'romeo_and_juliet.txt']
for filename in filenames:
    count_common_words(filename, 'the ')