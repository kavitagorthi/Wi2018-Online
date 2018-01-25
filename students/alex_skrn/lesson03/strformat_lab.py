#!/usr/bin/env python3

# Task 1
def task_one(a_tuple):
    raise NotImplementedError


# Task 2
def task_one_2(a_tuple):
    """Alternative implementation."""
    raise NotImplementedError


# Task 3
def formatter(a_tuple):
    L = len(a_tuple)
    form_string = "the {} numbers are: " + ", ".join(["{:d}"]*L)
    # print(form_string)
    return form_string.format(L, *a_tuple)


# Task 4

def change_positions(a_tuple):
    raise NotImplementedError


# Task 5 - f-strings

def f_formatter(a_list):
    raise NotImplementedError

# Task 6

def display_col():
    raise NotImplementedError


# TESTING SECTION
def test_task_one():
    string = 'file_002 :   123.46, 1.00e+04, 1.23e+04'
    assert task_one(2, 123.4567, 10000, 12345.67) == string

    
def test_task_2():
    string = 'file_002 :   123.46, 1.00e+04, 1.23e+04'
    assert task_one(2, 123.4567, 10000, 12345.67) == string


def test_formatter():
    assert formatter((2,3,5)) == 'the 3 numbers are: 2, 3, 5'
    assert formatter((2,3,5,7,9)) == 'the 5 numbers are: 2, 3, 5, 7, 9'


def test_change_positions():
    assert change_positions(( 4, 30, 2017, 2, 27)) == '02 27 2017 04 30'


def test_f_formatter():
    output = "The weight of an orange is 1.3 and the weight of a lemon is 1.1"
    assert f_formatter(['oranges', 1.3, 'lemons', 1.1]) == output


def test_display_col():
    raise NotImplementedError
    

def main():
    test_task_one()
    test_task_2()
    test_formatter()
    test_change_positions()
    test_f_formatter()
    test_display_col()

if __name__ == '__main__':
    main()
