#!/usr/bin/env python3

# Week 6
# Mailroom Assignment testing - Part 4
import mailroom4
import pytest
import sys


def test_print_donor_list():
    """Test printing the donor list."""
    donor = mailroom4.print_donor_list()
    assert donor[0] == 'Jimmy Nguyen'
    assert donor[1] == 'Steve Smith'


def test_get_donor():
    """Testing that the name is pulled correctly."""
    mailroom4.donors = { 'Jimmy Nguyen': [100, 1350, 55],
                         'Steve Smith': [213, 550, 435],
                         'Julia Norton': [1500, 1500, 1500],
                         'Ed Johnson': [150],
                         'Elizabeth McBath': [10000, 1200]
                         }

    for k in donors.keys():
        if donor == k.strip().lower():
            return k
        else:
            return None



def test_thank_you():
    """Test Thank you function for sending an email."""
    result = mailroom4.thank_you()

    # Test getting user full name

    while True:
        full_name = input(
            "Please enter a donor's name or type 'list' for list of donors ('menu' to return to menu): ").strip()

        if full_name == 'list':
            print('Below is the current donor list:')
            donor = print_donor_list()
            for i in donor:
                print(i)
            print()
        elif full_name == 'menu':
            return
        else:
            break

    # Enter a donation amount
    while True:
        try:
            donation = int(input("Please enter a donation amount. 'menu' to return to original menu: "))
            if donation == 'menu':
                return
            else:
                break
        except ValueError:
            print('Please enter a valid amount.')
            # continue

    # Enter a new donor
    donor = get_donor(full_name)
    if donor is None:
        donor = full_name
        donors[donor] = []

    donors[donor].append(donation)

    # Write a thank you for the donor
    print(letter(donor))


def test_create_report():
    """Test for creating a report of donors with donation amounts."""
    pass


def test_letter():
    """Test the letter function."""
    letter = """Dear {},\nThank you for your very kind donation of {:.2f}.\n\nIt will be put to very good use.\n\n \t\tSincerely,\n\t\t\t-The Team"""
    donor_list = list(mailroom4.donors.keys())
    donor = donor_list[0]
    result = mailroom4.letter(donor)
    assert result == letter.format(donor, mailroom4.donors[donor][-1])


def test_send_letter_file():
    """Test for writing a letter to a donor."""
    pass


def test_print_header():
    """Prints the menu items to choose from and returns the selection."""
    pass


def test_main():
    """Main mneu of the program."""
    pass
