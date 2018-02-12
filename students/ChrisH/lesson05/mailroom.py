#!/usr/bin/env python3
# -----------------------------------------------------------
# mailroom.py
#  Part 3. Script to automate writing thank you emails to donors.
#  Add exceptions and use comprehensions.
# -----------------------------------------------------------

import time

from collections import namedtuple

# Giving namedtuples a shot
Donor = namedtuple('Donor', 'first,last')


# Global data structure
donor_data = \
    {Donor('Al','Donor1'): [10.00, 20.00, 30.00, 40.00, 50.00],
     Donor('Bert', 'Donor2'): [10.00],
     Donor('Connie', 'Donor3'): [10.00, 10.00, 10.01],
     Donor('Dennis', 'Donor4'): [10.00, 20.00, 20.00],
     Donor('Egbert', 'Donor5'): [10.39, 20.21, 10.59, 4000.40],
     }


def get_donor_fullname(donor):
    """
    Given a donor namedtuple, assembles and returns the donor's full name.
    :param donor: namedtuple type: Donor
    :return: string with donor's full name
    """
    return (donor.first + ' ' + donor.last).strip()   # Strip, in case first name is blank


def menu(menu_data):
    """
    Prints the main user menu & retrieves user selection.
    :param: a menu dictionary, key as numbered list.
            Dict key 0 should be a null function (or text for bad choice)
            Dict value is a list with the following entries:
                [0] = Text for user prompt
                [1] = Function that should be run for that choice
    :return: the function corresponding to the user's selection
    """
    print("\nPlease choose one of the following options:")
    for n in range(1, len(menu_data)):                     # Start at item 1, item 0 should be null function
        print(f"{n}) {menu_data[n][0]}")                   # Prints the menu user text
    menu_entry = menu_data.get(int(input("> ")), menu_data[0])   # if bad option, returns item 0
    return menu_entry[1]                                         # Returns the function from that menu choice's list


def generate_letter(donor):
    """
    Generates a Thank You letter to send to a donor. Uses the last value in their donations list to
    mention their last donation amount.
    :param donor: a donor dictionary entry
    :return: string containing the text of the Thank You letter.
    """
    format_string = """
Dear {first_name} {last_name},

   Thank you for your donation of ${last_donation:.2f}.

            Warmest Regards,
                Local Charity
"""
    amount = donor_data[donor][-1]
    return format_string.format(last_donation=float(amount), first_name=donor.first, last_name=donor.last)

#    return "{first_name} {last_name} {donations[2]}".format(**(donor_data[donor]))  # This requires static index!!


def send_letters_all():
    """
        Runs through donor data structure, generates a thank you letter for each and saves it to
        the current working directory with in a date+donorname.txt file
        :return: None
        """
    for donor in donor_data:
        print(f'Generating letter for {get_donor_fullname(donor)}')
        now = time.localtime()
        f_name = f"{now.tm_year}{now.tm_mon:02}{now.tm_mday:02}_"
        f_name += get_donor_fullname(donor).replace(" ", "_") + ".txt"
        file_out = open(f_name, 'w')
        file_out.write(generate_letter(donor))
        file_out.close()
    return None


def send_thank_you():
    """
    Prompts for donor name, if not present, adds user to data. Prompts for donation
    and adds it to donor's data. Prints a 'Thank You' email populated with the donor's data.
    :return: None
    """

    while True:
        name = input("Enter a Full Name ('list' to show list of donors, 'q' to quit): ")
        if name == 'q':
            return
        elif name == 'list':
            print(("{}\n" * len(donor_data)).format(*([get_donor_fullname(d) for d in donor_data])))
            continue
        else:
            name_sp = name.split()
            if len(name_sp) == 0:
                print("Name cannot be empty.")
                continue
            elif len(name_sp) > 1:
                donor = Donor(name_sp[0], ' '.join(name_sp[1:]))  # Defines first name up to the first space given
            else:
                donor = Donor(first='', last=name)
            break

    if donor not in donor_data:
        donor_data[donor] = []

    while True:
        try:
            amount = input("Enter a donation amount for {} : ".format(get_donor_fullname(donor)))
            if float(amount) <= 0:
                print('Amount donated must be a positive number.')
            else:
                break
        except ValueError:
            print('Please enter a numerical value.')

    donor_data[donor].append(float(amount))
    print(generate_letter(donor))


def print_report():
    """
    Prints a formatted report on the donors with name, amount given, number of gifts, and average gift.
    :return: None
    """
    # Adjust first column width to accommodate the length of the longest name
    name_max = 26
    for donor in donor_data.keys():
        if len(get_donor_fullname(donor)) > name_max:
            name_max = len(get_donor_fullname(donor)) + 1

    rpt_title = "Donor Name" + ' ' * (name_max - 10) + "| Total Given | Num Gifts | Average Gift"
    print(rpt_title)
    print("-" * len(rpt_title))
    for donor in donor_data.keys():
        dons = donor_data[donor]
        print(f"{get_donor_fullname(donor):{name_max}} ", end='')
        print(f"$ {sum(dons):>10.2f}   {len(dons):>9}  ${sum(dons)/len(dons):>12.2f}")


def nul():
    pass


if __name__ == "__main__":
    menu_functions = {0: ['nul', nul],                      # could also use 'lambda: None' instead of nul
                      1: ['Send a Thank You', send_thank_you],
                      2: ['Print a report', print_report],
                      3: ['Send letters to everyone', send_letters_all],
                      4: ['Quit', quit],
                      }
    while True:
        menu(menu_functions)()
