#!/usr/bin/env python3

#-------------------------------------------------#
# Title: Mailroom Part-3 Assignment
# Dev: Scott Luse
# Date: Feb 18, 2018
#-------------------------------------------------#

from collections import Counter

# -- Data --#
donor_dict = {
    'Peter Parker': [288.09, 9.01, 61288.09],
    'Iron Man': [1238.09, 8199.01, 1468.07],
    'Captain Marvel': [43188.09, 1288.09],
    'Black Widow' : [1272.09],
}

# -- Processing --#
def GetUserChoice():

    print("""
    MailRoom Part2 Menu Options
    1) Send a Thank You
    2) Create a Report
    3) Send Letters To Everyone
    4) Quit Program
    """)
    user_choice = input("Which option would you like to perform? [1 to 4]: ")
    return (user_choice.strip())


def process_menu(menu_item):
    if menu_item == '1':
        send_thanks()
        return
    elif menu_item == '2':
        format_charity_structure()
        return
    elif menu_item == '3':
        create_individual_letters()
        return

def send_thanks():
    while (True):
        thank_you_name = input("Please enter full name, enter 'list' for names, or 'main' for menu: ")
        if thank_you_name.lower() == "list":
            print_donors()
            print(' ')
        elif thank_you_name.lower() == "main":
            return
        else:
            process_input_name(thank_you_name)
            return

def process_input_name (name):
    '''Ask for a donation amount and look for user input name in donor dictionary.
    If you find the name and the amount to the donor ledger and print a letter to the screen.
    If you don't find the name create a new key value pair'''

    gift_amount = int(input("Please enter $$ donation $$ amount for " + name + ":"))
    # add ValueError: try block
    if name in donor_dict.keys():
        #We found the name so update the giving values
        #Is this the best way to manage appending the list?
        original_list = donor_dict.get(name)
        original_list.append(gift_amount)
        donor_dict[name] = original_list
        thank_you_printing(name, gift_amount)
        return
    else:
        #We didn't find the name so create a new key value pair
        donor_dict[name] = [gift_amount]
        thank_you_printing(name, gift_amount)
        return

def thank_you_printing(name, amount):
    line_divider = "*" * 50
    print(f'''
    {line_divider}
    {name}
    Address
    
    Dear {name},
    Thank you for your charitable gift of ${amount}.
    {line_divider}
    ''')

def print_donors():
    # dict comp opportunity! {print(key) for key in DONOR_HISTORY_DICT.keys())}
    # PR comment from Michael, update code
    for key in donor_dict:
        print(key)

def format_charity_structure():
    print('')
    print('{:20}{:>15}{:>10}{:>10}'.format('Donor Name', '| Total Gifts', '| Num Gifts', '| Ave Gift'))
    print('-' * 55)
    for key in donor_dict:
        donor_list = donor_dict.get(key)
        sum_values = "{:.2f}".format(sum(donor_list))
        ave_values = "{:.2f}".format(sum(donor_list) / len(donor_list))
        print('{:20}{:>15}{:>10}{:>10}'.format(key, sum_values, len(donor_list), ave_values))


def create_individual_letters():
    try:
        for key in donor_dict:
            donor_list = donor_dict.get(key)
            sum_values = "{:.2f}".format(sum(donor_list))

            # Update with triple quotes per Pull Request comments

            report_text = f"Dear {key}," + "\n" + "\n" + "Thank you for your charitable gift of $" + sum_values + "."
            report_text = report_text  + "\n" + "\n" + "\tIt will be put to very good use."
            report_text = report_text  + "\n" + "\n" + "\t\tSincerely,"
            report_text = report_text + "\n" + "\t\t\t--The Team"

            key.replace(" ", "_")
            objFileName = key.replace(" ", "_") + ".txt"
            objMyFile = open(objFileName, "w")
            objMyFile.write(report_text)
            objMyFile.close()
            print(objFileName + " file saved.")

    except IOError:
        print("\n" + "File error!")

# -- Presentation (Input/Output) --#
if __name__ == '__main__':
    while (True):
        get_user_action = GetUserChoice()
        if get_user_action == "4":
            print("Goodbye!")
            break
        else:
             process_menu(get_user_action)