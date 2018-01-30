#!/usr/bin/env python3

"""Mailroom - Part 1."""

donors = ["Wassily Kandinsky", "Marc Chagall", "Kazimir Malevich",
          "El Lissitzky", "Aristarkh Lentulov"]
donors_sums = [[75.0, 50.5, 60.4], [148.75, 155.0], [15.0, 20.25, 12.25],
               [34.20, 30.0, 35.5], [4.5, 5.0]]


# Sending a Thank You.
def print_send_thank_you_menu():
    """Print the send-thank-you menu on screen."""
    msg = ("\nThis is the Send-Thank-You Menu\n"
           "\nType <list> to see donor names, or\n"
           "Type an existing donor name, or\n"
           "Type a new donor name to add to the list, or\n"
           "Type <quit> to go to the main manu.\n"
           )
    print(msg)


def print_donor_names():
    """Print existing donor names on screen."""
    print()
    for name in donors[:-1]:
        print("{}".format(name), end=', ')
    print(donors[-1])
    print()


def get_last_donation(donor_name):
    """Return the last donation amount for donor_name."""
    donor_index = donors.index(donor_name)
    donation_amount = donors_sums[donor_index][-1]
    return donation_amount


def ask_donation_amount(donor_name):
    """Ask for and add a new donation for the donor named donor_name."""
    prompt_sum = input("Type the donation amount or 0 to abort > ")
    if prompt_sum == "0":
        return False
    donor_index = donors.index(donor_name)
    donors_sums[donor_index].append(float(prompt_sum))
    return True


def add_new_donor(donor_name):
    """Add a new donor to the list and a slot for donation amounts."""
    donors.append(donor_name)
    donors_sums.append([])


def remove_new_donor():
    """Remove last donor from the list if user aborted the add operation."""
    del donors[-1]


def print_email(donor_name):
    """Print a thank-you email addressed to name on screen."""
    print()
    # Get the last donation amount for donor_name.
    don_amount = get_last_donation(donor_name)

    # Compose and print the email text on screen.
    email_text = ("\nDear {},\n"
                  "\nI would like to thank you for your donation of ${:,}.\n"
                  "\nWe appreciate your support.\n"
                  "\nSincerely,\n"
                  "The Organization\n"
                  )
    print(email_text.format(donor_name, don_amount))


def send_thank_you_interaction():
    """Send a thank you letter."""
    while True:
        print_send_thank_you_menu()
        prompt = input("Type your choice > ")
        if prompt == "quit":
            return
        elif prompt == 'list':
            print_donor_names()
            # send_thank_you_interaction()
        elif prompt not in donors:
            add_new_donor(prompt)
            if ask_donation_amount(prompt):
                print_email(prompt)
            else:
                remove_new_donor()
        elif prompt in donors:
            ask_donation_amount(prompt)
            print_email(prompt)


# Creating a Report.
def get_total_given(donor_name):
    """Return total amount of donations for the given donor donor_name."""
    donor_index = donors.index(donor_name)
    return sum(donors_sums[donor_index])


def get_donations(donor_name):
    """Return a list of the specified donor's donations."""
    donor_index = donors.index(donor_name)
    return donors_sums[donor_index]


def sort_donors_by_total():
    """Return a list of donor names sorted by total donations, max to min."""
    # Create a list in the form [['Donor Name', total_donated], []].
    donors_totals = []
    for name in donors:
        donors_totals.append([name, get_total_given(name)])

    # Sort the above list by the total_donated.
    donors_totals.sort(key=lambda x: x[1])
    donors_totals = donors_totals[::-1]

    # Get rid of the total_donated in the list.
    sorted_donor_names = []
    for item in donors_totals:
        sorted_donor_names.append(item[0])

    # Return a list containing the names of donors only.
    return sorted_donor_names


def create_report_main():
    """Create a report."""
    title_line_form = "{:<26}{:^3}{:>13}{:^3}{:>13}{:^3}{:>13}"
    title_line_text = ('Donor Name', '|', 'Total Given', '|',
                       'Num Gifts', '|', 'Average Gift'
                       )
    print()
    print(title_line_form.format(*title_line_text))
    print('- ' * 38)
    form_line = "{:<26}{:>3}{:>13}{:>3}{:>13}{:>3}{:>13}"
    for name in sort_donors_by_total():
        total = get_total_given(name)
        num_gifts = len(get_donations(name))
        mean = round((total / num_gifts), 2)
        print(form_line.format(str(name), '$', str(total), ' ',
                               str(num_gifts), '$', str(mean)
                               )
              )
    print()


# Main menu.
def print_main_menu():
    """Print the menu on screen."""
    main_menu = ("\nThis the Main Menu\n"
                 "\n1 for Send a Thank You\n"
                 "2 for Create a Report\n"
                 "3 for Quit\n"
                 )
    print(main_menu)


def main_menu_interaction():
    """Control the main flow of the user interaction."""
    while True:
        print_main_menu()
        prompt = input("Please choose an option > ")
        if prompt == "1":
            send_thank_you_interaction()
        elif prompt == "2":
            create_report_main()
        elif prompt == "3":
            break


if __name__ == "__main__":
    main_menu_interaction()
