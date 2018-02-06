#!/usr/bin/env python

donors = [["Walter White", "Ray Donovan", "John Snow", "Walter White", "Ray Donovan", "John Snow"],
          [10000, 2500, 10, 15000, 6500, 5]]

# define a function to prompt the user for their desired action
def prompt_user():
    print("What would you like to do? Your options are: 1) Send a Thank You, 2) Create a Report, 3) quit")
    response = input("Please type your selection > ")
    while(response not in ("Send a Thank You", "Create a Report", "quit")):
        print("Please enter one of 'Send a Thank You', 'Create a Report', or 'quit' > ")
        response = input("Please type your selection > ")
    return response

# define a function to send a thank you card
def send_a_thank_you():
    unique_donors = list(set(donors[0]))
    print("You selected Send a Thank You.")
    donor = input("To whom would you like to send a thank you? > ")
    # list the possible candidates within the donors list    
    if donor == "list":
        # cycle through unique names in donor list with set() function
        for names in unique_donors:
            print(names)
        donor = input("To whom would you like to send a thank you? > ")
    # prompt the user for a donation amount
    donation_amount = int(input("How much would you like to donate? > "))
    # add the donor and the donation amount to the donors list
    donors[0].append(donor)
    donors[1].append(donation_amount)
    
    print("Dear {:s}, Thank you for your generous donation of ${:.2f}. Best, The Donation Foundation. ".format(donors[0][-1], donors[1][-1]))
    
    prompt_user()
   

# define a function to create a donation report
def create_a_report():
    print("You selected create a report.")

# define a function to quit the program
def quit_program():
    print("You selected quit.")

def handle_response(user_input):
    if user_input == "Send a Thank You":
        send_a_thank_you()
    elif user_input == "Create a Report":
        create_a_report()
    elif user_input == "quit":
        quit_program()
    else:
        print("Something went wrong, the program is quitting.")
        quit_program()
    
if __name__ == '__main__':
    handle_response(prompt_user())