#!/usr/bin/env python

# establish the starting tuple
starting_tuple = (2, 123.4567, 10000, 12345.67)

# Task 1
def task1(st):
	print("file_{:03d}: {:05.2f}, {:.2E}, {:.2E}".format(*st))

task1(starting_tuple)

# Task 2: Alternative format
def task2(st):
	print("file_{file_number}: {val1}, {val2}, {val3}".format(file_number = "{:03d}".format(st[0]), val1 = "{:05.2f}".format(st[1]), val2 = "{:.2E}".format(st[2]), val3 = "{:.2E}".format(st[3])))

task2(starting_tuple)

# Task 3

