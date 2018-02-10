#!/usr/bin/env python3
#
# Assignment: Mailroom, Part 1
# Chay Casso
# 2/10/2018

# Initial donor table with the donation values.
donor_table = [["William Gates, III", 401321.52], ["William Gates, III", 201342.71], ["Mark Zuckerberg", 123.45],
               ["Mark Zuckerberg", 5123.21], ["Mark Zuckerberg", 8213.11], ["Jeff Bezos", 877.33],
               ["Paul Allen", 152.42], ["Paul Allen", 30.54], ["Paul Allen", 825.21], ["Steve Ballmer", 5198.96],
               ["Steve Ballmer", 654.98]]
answer = ""


def thank_you(donor_table):
    answer = ""
    while answer != "quit":
        full_name = input("Please enter a full name.")
        if full_name.lower() == "list":
            print("Donor list:")
            donor_table_sort = donor_table.sort()
            current_name = ""
            for row in donor_table_sort:
                if current_name != row[0]:
                    current_name = row[0]
                    print(current_name)



def create_report():
    pass


# Main menu
while answer != "3":
    print("1. Send a Thank You")
    print("2. Create a Report")
    print("3. Quit")
    answer = input("Please select an option. >")
    if answer == "1": donor_table = thank_you(donor_table)
    if answer == "2": create_report()
    if answer == "3": print("Have a nice day.")