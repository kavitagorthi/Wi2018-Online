#!/usr/bin/env python3

"""Mailroom 1."""

DONORS = ['Wassily Kandinsky', 'Marc Chagall', 'Kazimir Malevich',
          'El Lissitzky', 'Aristarkh Lentulov']
DONORS_SUMS = [[75.0, 50.5, 60.4], [148.75, 155.0], [15.0, 20.25, 12.25],
               [34.20, 30.0, 35.5], [4.5, 5.0]]


# Sending a Thank You.
def print_send_thank_you_menu():
    """Print the send-thank-you menu on screen."""
    msg = ("Type <list> to see donor names, " +
           "type an existing donor name, or " +
           "type a new donor name to add to the list, or " +
           "type <quit> to go to the main manu.")
    print()
    print(msg)
    print()


def print_donor_names():
    """Print existing donor names on screen."""
    print()
    for name in DONORS[:-1]:
        print("{}".format(name), end=', ')
    print(DONORS[-1])
    print()


def get_last_donation(donor_name):
    """Return the last donation amount for donor_name."""
    donor_index = DONORS.index(donor_name)
    donation_amount = DONORS_SUMS[donor_index][-1]
    return donation_amount


def ask_donation_amount(donor_name):
    """Ask for and add a new donation for the donor named donor_name."""
    prompt_sum = float(input('Type the donation amount or 0 to abort > '))
    if int(prompt_sum) == 0:
        return False
    donor_index = DONORS.index(donor_name)
    DONORS_SUMS[donor_index].append(prompt_sum)
    return True


def add_new_donor(donor_name):
    """Add a new donor to the list and a slot for donation amounts."""
    DONORS.append(donor_name)
    DONORS_SUMS.append([])


def remove_new_donor():
    """Remove last donor from the list if user aborted the add operation."""
    del DONORS[-1]


def print_email(donor_name):
    """Print a thank-you email addressed to name on screen."""
    print()
    # Get the last donation amount for donor_name.
    don_amount = get_last_donation(donor_name)

    # Compose and print the email text on screen.
    email_text = '''Dear {},

    Thank you for your kind contribution of ${}.

    It will be put to good use.

    Sincerely,
    The team'''
    print(email_text.format(donor_name, don_amount))
    print()


def send_thank_you_main():
    """Send a thank you letter."""
    print_send_thank_you_menu()
    prompt = input('Please type here > ')
    if prompt == "quit":
        return
    elif prompt == 'list':
        print_donor_names()
        send_thank_you_main()
    elif prompt not in DONORS:
        add_new_donor(prompt)
        if ask_donation_amount(prompt):
            # print('-ask-don-am returned True')
            print_email(prompt)
        else:
            remove_new_donor()
    elif prompt in DONORS:
        ask_donation_amount(prompt)
        print_email(prompt)


# Creating a Report.
def get_total_given(donor_name):
    """Return total amount of donations for the given donor donor_name."""
    donor_index = DONORS.index(donor_name)
    return sum(DONORS_SUMS[donor_index])


def get_donations(donor_name):
    """Return a list of the specified donor's donations."""
    donor_index = DONORS.index(donor_name)
    return DONORS_SUMS[donor_index]


def sort_donors_by_total():
    """Return a list of donor names sorted by total donations, max to min."""
    # Create a list in the form [['Donor Name', total_donated], []].
    donors_totals = []
    for name in DONORS:
        donors_totals.append([name, get_total_given(name)])
    # print(donors_totals)

    # Sort the above list by the total_donated.
    donors_totals.sort(key=lambda x: x[1])
    donors_totals = donors_totals[::-1]
    # print(DONORS)
    # print(DONORS_SUMS)
    # print(donors_totals)

    # Get rid of the total_donated in the list.
    sorted_donor_names = []
    for item in donors_totals:
        sorted_donor_names.append(item[0])
    # print(sorted_donor_names)

    # Return a list containing the names of donors only.
    return sorted_donor_names


def create_report_main():
    """Create a report."""
    title_line_form = "{:26}{:^3}{:>13}{:^3}{:>13}{:^3}{:>13}"
    title_line_text = ('Donor Name', '|', 'Total Given', '|',
                       'Num Gifts', '|', 'Average Gift')
    print()
    print(title_line_form.format(*title_line_text))
    print('- ' * 38)
    form_line = "{:26}{:>3}{:>13}{:>3}{:>13}{:>3}{:>13}"
    for name in sort_donors_by_total():
        total = get_total_given(name)
        num_gifts = len(get_donations(name))
        mean = round((total / num_gifts), 2)
        print(form_line.format(str(name), '$', str(total), ' ',
                               str(num_gifts), '$', str(mean)))
    print()


# Main menu.
def print_main_menu():
    """Print the menu on screen."""
    item1 = '1 for Send a Thank You'
    item2 = '2 for Create a Report'
    item3 = '3 for Quit'
    print()
    print('Main menu')
    for item in (item1, item2, item3):
        print(item)
    print()


if __name__ == '__main__':
    while True:
        print_main_menu()
        prompt = int(input('Please choose an option > '))
        while not (prompt == 1 or prompt == 2 or prompt == 3):
            print_main_menu()
            prompt = int(input('Please choose an option > '))
        if prompt == 1:
            send_thank_you_main()
        elif prompt == 2:
            create_report_main()
        else:
            break
