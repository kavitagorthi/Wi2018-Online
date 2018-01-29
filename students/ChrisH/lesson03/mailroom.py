#!/usr/bin/env python3
# -----------------------------------------------------------
# mailroom.py
#  Part 1. Script to automate writing thank you emails to donors.
#  Uses only functions and data types learned about so far.
# -----------------------------------------------------------

donor_data = [('Al Donor1', [10, 20, 30, 40, 50]),
              ('Bert Donor2', [10]),
              ('Connie Donor3', [10, 10, 10]),
              ('Dennis Donor4', [10, 20, 20]),
              ('Egbert Donor5', [10, 20, 10, 4000]),
              ]

def donor_names():
    name_list = []
    for donor in donor_data:
        name_list.append(donor[0])
    return name_list

def menu():
    print("\nPlease choose one of the following options:")
    print("1) Send a Thank You")
    print("2) Create a Report")
    print("3) Quit")
    return int(input("> "))

def send_thank_you():
    d_list = donor_names()
    donor_thanks = ''
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


if __name__ == "__main__":

    while(True):
        choice = menu()
        if choice == 1:
            send_thank_you()
        elif choice == 2:
            print('rpt')
        elif choice == 3:
            quit(0)

