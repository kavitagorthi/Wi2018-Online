#!/usr/local/python3

#Initial Donors List
donors = [['Aron', [100, 200, 300]], ['Joan', [200]], ['Jean', [200, 300, 1000, 50]], ['Scott', [150]]]

#Thank You Functionality
##If the user types ‘list’, show them a list of the donor names and re-prompt
##If the user types a name not in the list, add that name to the data structure and use it.
##If the user types a name in the list, use it.
##Once a name has been selected, prompt for a donation amount.
##Turn the amount into a number – it is OK at this point for the program to crash if someone types a bogus amount.
##Once an amount has been given, add that amount to the donation history of the selected user.
##Compost an email thanking the donor for their generous donation. Print the email to the terminal and return to the original prompt.

#
def donor_sum():
    summary=[]
    for donor in donors:
        summary.append([donor[0],
        len(donor[1]),
        sum(donor[1]) / len(donor[1])])
    return summary

#list of donor names
names=[]
def donor_names():
    for i in donors:
        names.append(i[0])

def list_check(x):
    while True:
        x=input("Check user name: ")
        if x in names:
            print("We have a match")
        else:
        y = input("No match, adding to list. Please enter donation amount ")
        donors.append([x,[y]])

def send_thank_you():
    donor_names = names()  # create a list of names only
    while True:
        response = input("Enter the name of a donor "
                         "('list' -> list of donors | 'main' -> "
                         "main menu)\n")
        if response == 'list':
            print("Existing donors - " + " - ".join(donor_names))
        elif response == 'main':
            init()
        elif response in donor_names:  # i.e. existing donor
            add_donation(response, exsting_donor=True)
            break
        elif response.isalpha():  # new donor
            add_donation(response, exsting_donor=False)
            break
    init()

def init():
    while True:
        heading = "Main Menu"
        print(heading)
        choice = input("1 - See list of donors ")
        if choice == '1':
            send_thank_you()
            break
        elif choice == '2':
            create_report()
            break
        elif choice == '3':
            print ('Exit')
            quit()
            break
