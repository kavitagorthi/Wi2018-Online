#!/usr/bin/env python3

"""Lesson03 - Assignment 2 - String formatting."""

# Task 1
def get_padding_zeros(num_zeros):
    """Ruturn  a str containg num_zeros of padding zeros."""
    return ''.join(['0'] * num_zeros)

def get_file_num(an_integer):
    """Return a string like 'file_002' from an_integer."""
    length = len(str(an_integer))
    num_zeros = 3 - length
    padding_zeros = get_padding_zeros(num_zeros)
    file_num = 'file_' + padding_zeros + str(an_integer)
    return file_num


def get_rounded_float_string(a_float):
    """Return a str containing a float rounded to 2 digits afer  decimal."""
    rounded_float_s = str(round(a_float[1], 2))
    return rounded_float_s


def convert_int_to_sci_not(an_int):
    """Return a str with an_int in sci notation, 2 decimal places shown."""
    # Eg. 10000 --> 1.00e+04; 2 --> 2.00e+00; -300 --> 3.00e-02
    absol_val = abs(an_int)

    if an_int > 0:

    elif an_int < 0:

    elif an_int == 0:


def convert_float_to_sci_not(a_float):
    """Return a str with a_float in sci notation, 3 significant digits."""
    # Eg. 12345.67 > 1.23e+04
    raise NotImplementedError


def task_one_style_formatter(a_tuple):
    """Return the task-one-style formatted string."""
    # Eg. ( 2, 123.4567, 10000, 12345.67) -->
    # 'file_002 :   123.46, 1.00e+04, 1.23e+04'
    item_one = get_file_num(a_float[0])
    item_two = get_rounded_float_string(a_float[1])
    item_three = convert_int_to_sci_not(a_float[2])
    item_four = convert_float_to_sci_not(a_float[3])
    return '{}: {}, {}, {}'.format(item_one, item_two, item_three, item_four)



# Task 2
def task_one_style_formatter2(a_tuple):
    """Alternative implementation."""
    raise NotImplementedError


# Task 3
def task_three_style_formatter(a_tuple):
    """Returns a str like, eg., 'the 3 numbers are: 1, 2, 3'."""
    length = len(a_tuple)
    form_string = "the {} numbers are: " + ", ".join(["{:d}"] * length)
    # print(form_string)
    return form_string.format(length, *a_tuple)


# Task 4
def change_positions(a_tuple):
    """."""
    # Eg., (4, 30, 2017, 2, 27) --> '02 27 2017 04 30'

    # Add padding zeros to all numbers if required and save them as strings
    a_list = []
    for num in a_tuple:
        if num < 10:
            a_list.append('0' + str(num))
        else:
            a_list.append(str(num))

    # Re-arrange the numbers
    seq = a_list[3], a_list[4], a_list[2], a_list[0], a_list[1]

    return "{} {} {} {} {}".format(*seq)



# Task 5 - f-strings
def f_formatter1(a_list):
    """."""
    # Eg., ['oranges', 1.3, 'lemons', 1.1] -->
    # The weight of an orange is 1.3 and the weight of a lemon is 1.1

    f_string = (f"The weight of an {a_list[0][:-1]} is {a_list[1]} "
                f"and the weight of a {a_list[2][:-1]} is {a_list[3]}")

    return f_string


def f_formatter2(a_list):
    """."""
    # Eg., ['oranges', 1.3, 'lemons', 1.1] -->
    # The weight of an ORANGE is 1.56 and the weight of a LEMON is 1.32

    f_string = (f"The weight of an {a_list[0][:-1].upper()} "
                f"is {a_list[1] * 1.2} "
                f"and the weight of a {a_list[2][:-1].upper()} "
                f"is {a_list[3] * 1.2}")

    return f_string

# Task 6

def display_col():
    """."""
    form_str = "{:6}{:>20}{:5}{:6}{:>20}"
    print(form_str.format('First', '$9999.01', '', 'Second', '$99988.09'))
    print(form_str.format('3rd', '$9.01', '', 'Fouth', '$8.09'))


def display_col2(a_tuple):
    """."""
    print(''.join(["{:10d}"] * 10).format(*a_tuple))




# TESTING SECTION
def test_task_one_style_formatter():
    """."""
    string = 'file_002 :   123.46, 1.00e+04, 1.23e+04'
    assert task_one_style_formatter((2, 123.4567, 10000, 12345.67)) == string

    print("Passed test_task_one_style_formatter")

def test_task_one_style_formatter2():
    """."""
    string = 'file_002 :   123.46, 1.00e+04, 1.23e+04'
    assert task_one_style_formatter2((2, 123.4567, 10000, 12345.67)) == string

    print("Passed test_task_one_style_formatter2")


def test_task_three_style_formatter():
    """."""
    res1 = 'the 3 numbers are: 2, 3, 5'
    res2 = 'the 5 numbers are: 2, 3, 5, 7, 9'
    assert task_three_style_formatter((2,3,5)) == res1
    assert task_three_style_formatter((2,3,5,7,9)) == res2

    print("Passed task_three_style_formatter")


def test_change_positions():
    """."""
    assert change_positions(( 4, 30, 2017, 2, 27)) == '02 27 2017 04 30'

    print("Passed test_change_positions")


def test_f_formatter1():
    """."""
    output = "The weight of an orange is 1.3 and the weight of a lemon is 1.1"
    assert f_formatter(['oranges', 1.3, 'lemons', 1.1]) == output

    print("Passed test_f_formatter")


def test_f_formatter2():
    """."""
    res = "The weight of an ORANGE is 1.56 and the weight of a LEMON is 1.32"
    assert f_formatter(['oranges', 1.3, 'lemons', 1.1]) == res

    print("Passed test_f_formatter")


def test_display_col():
    """."""
    raise NotImplementedError

    print("Passed test_display_col")


def run_tests():
    """Run all tests."""
    test_task_one_style_formatter()
    test_task_one_style_formatter2()
    test_task_three_style_formatter()
    test_formatter()
    test_change_positions()
    test_f_formatter1()
    test_f_formatter2()
    test_display_col()

if __name__ == '__main__':
    run_tests()
    print(task_one_style_formatter((2, 123.4567, 10000, 12345.67)))
    print(task_one_style_formatter2((2, 123.4567, 10000, 12345.67)))
    print(task_three_style_formatter((2,3,5,7,9)))
    print(change_positions((4, 30, 2017, 2, 27)))
