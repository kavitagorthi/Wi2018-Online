# -----------------------------------------------------------
# slicing_lab.py
#  functions that take sequences and return modified copies
# -----------------------------------------------------------


def exchange_first_last(seq):
    """
    Take a sequence and return a copy with the first and last items exchanged.
    :param seq: a sequence of items
    :return: seq with first/last items exchanged
    """

    if len(seq) < 2:
        return seq

    return seq[-1:] + seq[1:-1] + seq[:1]


def remove_every_other_item(seq):
    """
    Remove every other item in the seq.
    :param seq: a sequence of items
    :return: seq with every other item removed
    """
    if len(seq) < 2:
        return seq

    return seq[::2]

def remove_first4_last4_every_other(seq):
    """
    Remove first 4 items & last 4 items, and every other item in between
    :param seq: a sequence of items
    :return: seq with first 4, last 4 removed and every other item remaining removed
    """
    return remove_every_other_item(seq[4:-4])


def reverse(seq):
    """
    Reverse the given sequence.
    :param seq: a sequence of items
    :return: seq with elements in reverse order
    """
    return seq[::-1]


if __name__ == "__main__":
    test_set = ['The quick brown fox jumped over the lazy dog.',
                [0, 1, 2, 3, 4, 5],
                (0, 1, 2, 3, 4, 5),
                ]

    exch_set = ['.he quick brown fox jumped over the lazy dogT',
                [5, 1, 2, 3, 4, 0],
                (5, 1, 2, 3, 4, 0),
                ]

    remove_set = ['Teqikbonfxjme vrtelz o.',
                  [0, 2, 4],
                  (0, 2, 4),
                  ]

    remove4_set = ['qikbonfxjme vrtelz ',
                   [],
                   (),
                   ]

    reverse_set = ['.god yzal eht revo depmuj xof nworb kciuq ehT',
                   [5, 4, 3, 2, 1, 0],
                   (5, 4, 3, 2, 1, 0),
                   ]

    test_functions = [(exchange_first_last, exch_set),
                      (remove_every_other_item, remove_set),
                      (remove_first4_last4_every_other, remove4_set),
                      (reverse, reverse_set),
                      ]

    for func, result_set in test_functions:
        print("Testing {:s}".format(func.__name__))
        for index, test in enumerate(test_set):
            print(func(test))
            assert func(test) == result_set[index]
