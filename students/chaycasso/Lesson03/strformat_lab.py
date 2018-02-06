#!/usr/bin/env python3
#
# String Format Lab
# Chay Casso, 2/6/2018

# Task One
# Write a format string that will take the following four element tuple:
# ( 2, 123.4567, 10000, 12345.67)
# and produce:
# 'file_002 :   123.46, 1.00e+04, 1.23e+04'

initial_tuple = (2, 123.4567, 10000, 12345.67)
resultant_string = "file_{:0>3d} : {:.2f}, {:.2e}, {:.2e}".format(*initial_tuple)
print(resultant_string)

# Task Two
# Using your results from Task One, repeat the exercise, but this time using an alternate type of format string
resultant_string2 = f"file_{initial_tuple[0]:0>3d} : {initial_tuple[1]:.2f}, {initial_tuple[2]:.2e}, " \
                    f"{initial_tuple[3]:.2e}"
print(resultant_string2)

# Task Three
# Dynamically Building up Format Strings

# Rewrite:
# "the 3 numbers are: {:d}, {:d}, {:d}".format(1,2,3)
# to take an arbitrary number of values.


def formatter(in_tuple):
    length = len(in_tuple)
    form_string = f"the {length} numbers are: "
    for i in range(length):
        form_string.join("{in_tuple[i]:d}:")
    return form_string.format(*in_tuple)

print(formatter((2,3,5)))
print(formatter((2,3,5,7,9)))