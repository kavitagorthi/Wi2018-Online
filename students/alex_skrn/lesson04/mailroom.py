#!/usr/bin/env python3

"""Mailroom - Part 2 - Dicts, Files."""

donors = {'Aristarkh Lentulov': [4.5, 5.0],
          'El Lissitzky': [34.2, 30.0, 35.5],
          'Kazimir Malevich': [15.0, 20.25, 12.25],
          'Marc Chagall': [148.75, 155.0],
          'Wassily Kandinsky': [75.0, 50.5, 60.4]
          }


# Sending a Thank You.
def existing_donor_interaction():
    """Ask for old donor name, donation amount, print a thank-you email."""
    prompt_name = "Type full name of the old donor or 0 to abort > "
    old_donor_name = input(prompt_name)
    if old_donor_name == "0":
        return
    while old_donor_name not in donors:
        old_donor_name = input(prompt_name)
        if old_donor_name == "0":
            return

    prompt_amount = "Enter the donation amount or 0 to abort > "
    donation_amount = input(prompt_amount)
    if donation_amount == "0":
        return

    # Add the donation amount to the dict.
    donors[old_donor_name].append(float(donation_amount))
    print_email(old_donor_name, float(donation_amount))


def new_donor_interaction():
    """Ask for new donor name, donation amount, print a thank-you email."""
    prompt_name = "Type full name of the new donor or 0 to abort > "
    new_donor_name = input(prompt_name)
    if new_donor_name == "0":
        return

    prompt_amount = "Enter the donation amount or 0 to abort > "
    donation_amount = input(prompt_amount)
    if donation_amount == "0":
        return

    # Add the donor and the donation amount to the dict.
    donors[new_donor_name] = [float(donation_amount)]

    print_email(new_donor_name, float(donation_amount))


def print_donor_names():
    """Print existing donor names on screen."""
    print()
    donors_L = list(donors.keys())
    for name in donors_L[:-1]:
        print(name, end=', ')
    print(donors_L[-1])
    print()


def print_email(name, amount):
    """Print a thank-you email on screen."""
    email_text = ("\nDear {},\n"
                  "\nI would like to thank you for your donation of ${:,}.\n"
                  "\nWe appreciate your support.\n"
                  "\nSincerely,\n"
                  "The Organization\n"
                  )
    print(email_text.format(name, amount))


def send_thank_you_interaction():
    """."""
    menu_selection(send_thanks_prompt, send_thanks_dispatch)


# Creating a Report.
def get_total_given(donor_name):
    """Return total amount of donations for the given donor."""
    return sum(donors[donor_name])


def get_donations(donor_name):
    """Return a list of the specified donor's donations."""
    return donors[donor_name]


def sort_donors_by_total():
    """Return a list of donor names sorted by total donations, max to min."""
    # Create a list in the form [['Donor Name', total_donated], etc.].
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


def quit():
    """."""
    return "exit menu"


def menu_selection(prompt, dispatch_dict):
    """."""
    while True:
        response = input(prompt)
        try:
            if dispatch_dict[response]() == "exit menu":
                break
        except KeyError:
            print("\nInvalid choice. Try again")
            pass


if __name__ == "__main__":
    # main_menu_interaction()
    send_thanks_dispatch = {"1": print_donor_names,
                            "2": new_donor_interaction,
                            "3": existing_donor_interaction,
                            "4": quit
                            }
    send_thanks_prompt = ("\nSend-Thank-You Sub-Menu\n"
                          "\n1 - See the list of donors\n"
                          "2 - Add a new donor and a donation amount\n"
                          "3 - Choose an existing donor\n"
                          "4 - Quit\n"
                          ">> "
                          )
    main_dispatch = {"1": send_thank_you_interaction,
                     "2": create_report_main,
                     "3": quit
                     }
    main_prompt = ("\nMain Menu\n"
                   "\n1 - Send a Thank You\n"
                   "2 - Create a Report\n"
                   "3 - Quit\n"
                   ">> "
                   )
    menu_selection(main_prompt, main_dispatch)
