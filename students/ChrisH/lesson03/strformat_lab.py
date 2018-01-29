#!/usr/bin/env python3
# -----------------------------------------------------------
# strformat_lab.py
#  demonstrates basic Python string formatting
# -----------------------------------------------------------

# Task One
data = (2, 123.4567, 10000, 12345.67)

print("file_{:03d} :{:9.2f}".format(data[0], data[1]))

'file_002 :   123.46, 1.00e+04, 1.23e+04'
'file_002 :   123.46'

print("{:8.2f}".format(data[1]))

