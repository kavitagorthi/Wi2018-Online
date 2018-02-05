#Slicing Lab Exercise
#Chay Casso, 2/4/18

#Write some functions that take a sequence as an argument, and return a copy of that sequence:


a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)


def exchange_first_last(seq):
    """with the first and last items exchanged."""
    return seq[-1:] + seq[1:-1] + seq[:1]


assert exchange_first_last(a_string) == "ghis is a strint"
assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)

def every_other_item(seq):
    """with every other item removed."""
    return seq[::2]


assert every_other_item(a_string) == "ti sasrn"
assert every_other_item(a_tuple) == (2, 13, 5)


a_longer_tuple = (2, 54, 13, 12, 5, 32, 65, 22, 81, 9, 43, 4)


def every_other_inner(seq):
    """with the first and last 4 items removed, and every other item in between."""
    return seq[4:-4:2]


assert every_other_inner(a_string) == " sas"
assert every_other_inner(a_longer_tuple) == (5, 65)

