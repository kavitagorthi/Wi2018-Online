#!/usr/bin/env python3

"""Mailroom exercise."""

DONORS = ['Wassily Kandinsky', 'Marc Chagall', 'Kazimir Malevich',
          'El Lissitzky', 'Aristarkh Lentulov']
DONORS_SUMS = [[75.0, 50.5, 60.4], [148.75, 155.0], [15.0, 20.25, 12.25],
               [34.20, 30.0, 35.5], [4.5, 5.0]]


def print_email():
    """Print an email on screen."""
    # build a big string in part
    print()
    print('Example thank you email')


def send_thank_you():
    """Send a thank you letter."""
    print_email()


def create_report():
    """Create a report."""
    print()
    print('Example report')


def print_menu():
    """Print the menu on screen."""
    item1 = '1 - Send a Thank You'
    item2 = '2 - Create a Report'
    item3 = '3 - Quit'
    print()
    print('Menu')
    for item in (item1, item2, item3):
        print(item)


if __name__ == '__main__':
    while True:
        print_menu()
        prompt = int(input('Please choose an option > '))
        while not (prompt == 1 or prompt == 2 or prompt == 3):
            print_menu()
            prompt = int(input('Please choose an option > '))
        if prompt == 1:
            send_thank_you()
        elif prompt == 2:
            create_report()
        else:
            break
