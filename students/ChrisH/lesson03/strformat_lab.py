#!/usr/bin/env python3
# -----------------------------------------------------------
# strformat_lab.py
#  demonstrates basic Python string formatting
# -----------------------------------------------------------

# Task One
data = (2, 123.4567, 10000, 12345.67)
print("file_{:03d} :{:9.2f}, {:.2e}, {:.2e}".format(data[0], data[1], data[2], data[3]))

# Task Two
print("file_{:03d} :{:9.2f}, {:.2e}, {:.2e}".format(*data))
print(f"file_{data[0]:03d} :{data[1]:9.2f}, {data[2]:.2e}, {data[3]:.2e}")


# Task Three


def formatter(in_tuple):
    """
    Dynamically format a tuple of numbers with a format string.
    :param in_tuple: tuple of any length, containing numbers
    :return: formatted string of output text
    """
    in_tuple_length = len(in_tuple)
    form_string = "the {} numbers are: ".format(in_tuple_length)
    form_string += ', '.join(['{:d}'] * in_tuple_length)

    return form_string.format(*in_tuple)

print(formatter((2,3,5,7,9)))
print(formatter((2,3,5)))



