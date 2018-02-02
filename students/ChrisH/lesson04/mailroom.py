#!/usr/bin/env python3
# -----------------------------------------------------------
# mailroom.py
#  Part 1. Script to automate writing thank you emails to donors.
#  Uses only functions and data types learned about so far.
# -----------------------------------------------------------

# Global data structure
donor_data = [{'first_name':'Al', 'last_name': 'Donor1','donations': [10.00, 20.00, 30.00, 40.00, 50.00]},
              {'first_name':'Bert', 'last_name': 'Donor2','donations': [10.00]},
              {'first_name':'Connie', 'last_name': 'Donor3','donations': [10.00, 10.00, 10.01]},
              {'first_name':'Dennis', 'last_name': 'Donor4','donations': [10.00, 20.00, 20.00]},
              {'first_name':'Egbert', 'last_name': 'Donor5','donations': [10.39, 20.21, 10.59, 4000.40]},
              ]


def donor_names():
    """
    Iterates donor data structure to produce a list of donor names.
    :return: list of donor names
    """
    name_list = []
    for donor in donor_data:
        name_list.append(donor['first_name'] + ' ' + donor['last_name'])
    return name_list


def menu():
    """
    Prints the main user menu, retrieves user selection.
    :return: int according to user's selection
    """
    print("\nPlease choose one of the following options:")
    print("1) Send a Thank You")
    print("2) Create a Report")
    print("3) Quit")
    return int(input("> "))


def send_thank_you():
    """
    Prompts for donor name, if not present, adds user to data. Prompts for donation
    and adds it to donor's data. Prints a 'Thank You' email populated with the donor's data.
    :return: None
    """
    d_list = donor_names()
    while True:
        name = input("Enter a Full Name ('list' to show list of donors): ")
        if name == 'list':
            print(("{}\n" * len(d_list)).format(*d_list))
            continue
        if name not in d_list:
            donor_data.append((name, []))
        break

    amount = input("Enter a donation amount for {} : ".format(name))
    for donor in donor_data:
        if name in donor[0]:
            donor[1].append(float(amount))
            print(f"\nDear {name}, \n\nThank you for your donation of ${amount}.\n\nWarmest regards,\nLocal Charity")


def print_report():
    """
    Prints a formatted report on the donors with name, amount given, number of gifts, and average gift.
    :return: None
    """
    print("Donor Name                | Total Given | Num Gifts | Average Gift")
    print("------------------------------------------------------------------")
    for donor in donor_data:
        print(f"{donor[0]:26} $ {sum(donor[1]):>10.2f}   {len(donor[1]):>9}  ${sum(donor[1])/len(donor[1]):>12.2f}")

def nul():
    pass

if __name__ == "__main__":
    menu_functions = {1: send_thank_you, 2: print_report, 3: quit}
    while True:
        menu_functions.get(menu(), nul)()       # could also use 'lambda: None' instead of nul

