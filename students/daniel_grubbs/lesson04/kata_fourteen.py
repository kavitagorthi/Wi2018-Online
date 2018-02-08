#!/usr/bin/env python3

# Kata Fourteen Assignment
# Daniel Grubbs
import random

file_name = 'sherlock_small.txt'
contents = []

# Grab the contents of the file and update the contents list
with open(file_name) as f:
    for line in f:
        contents += line.strip().split()


def main():
    print_header()
    trigrams(contents)


def print_header():
    """Print the header of the program."""
    print('------------------------------------')
    print('             Lesson04')
    print('     Kata Fourteen Assignment')
    print('------------------------------------\n')


def trigrams(content):
    """Take the contents and create the trigrams."""
    for item in range(len(content) - 2):
        buld_tupls = tuple(contents[item: item + 2])
        # test to make sure that two items are in a tuple
        # print(buld_tupls)
        # print(type(buld_tupls))


trigrams(contents)

if __name__ == '__main__':
    main()
