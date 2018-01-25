"""Lesson03 - Assignment 1 - Sequence slicing."""


def exchange_first_last(seq):
    """Return a copy of seq with the 1st and last items excahnged."""
    raise NotImplementedError


def remove_every_other(seq):
    """Return a copy of seq with every other item removed."""
    raise NotImplementedError


def remove_first_last_4_and_every_other(seq):
    """Return a copy of seq with the first and last 4 items removed,
and every other item in between."""
    raise NotImplementedError


def reverse_elements(seq):
    """Return a copy of seq with the elements reversed (just with slicing)."""
    raise NotImplementedError


def reorder_middle_last_first(seq):
    """Return a copy of seq with the middle third, then last third, \
then the first third in the new order."""
    raise NotImplementedError


# TESTING SECTION

def test_exchange_first_last():
    a_string = "this is a string"
    a_tuple = (2, 54, 13, 12, 5, 32)

    assert exchange_first_last(a_string) == "ghis is a strint"
    assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)
    raise NotImplementedError



def test_remove_every_other():
    raise NotImplementedError


def test_remove_first_last_4_and_every_other():
    raise NotImplementedError


def test_reverse_elements():
    raise NotImplementedError


def test_reorder_middle_last_first():
    raise NotImplementedError


def main():
    test_exchange_first_last()
    test_remove_every_other()
    test_remove_first_last_4_and_every_other()
    test_reverse_elements()
    test_reorder_middle_last_first()


if __name__ == '__main__':
    main()
