#!/usr/bin/env python3
#
# Assignment: Mailroom, Part 2
# Chay Casso
# 2/11/2018

# Initial donor table with the donation values.
donor_table = [["William Gates, III", 401321.52], ["William Gates, III", 201342.71], ["Mark Zuckerberg", 123.45],
               ["Mark Zuckerberg", 5123.21], ["Mark Zuckerberg", 8213.11], ["Jeff Bezos", 877.33],
               ["Paul Allen", 152.42], ["Paul Allen", 30.54], ["Paul Allen", 825.21], ["Steve Ballmer", 5198.96],
               ["Steve Ballmer", 654.98]]
answer = ""


def thank_you(donor_table):
    full_name = ""
    while full_name.lower() != "quit":
        full_name = input("Please enter a full name. >")
        if full_name.lower() == "quit": return(donor_table)
        if full_name.lower() == "list":
            donor_table.sort()
            current_name = ""
            print("Donor list:")
            for row in donor_table:
                if current_name != row[0]:
                    current_name = row[0]
                    print(current_name)
        else:
            donation_value_str = input("Please enter a donation amount. >")
            if donation_value_str.lower() == "quit": return(donor_table)
            donor_table.append([full_name, float(donation_value_str)])
            print()
            print("Dear {}:".format(full_name))
            print()
            print("Thank you for your generous donation to Save the Kids. We hope to hear from you soon.")
            print("-------------")
            print("Save the Kids")
            print("save@kids.org")
            print()
            return(donor_table)


def create_report(donor_table):
    donor_table.sort()
    print("{:<20} | {:<10} | {:<10} | {:<10}".format("Donor Name", "Total Given", "Num Gifts", "Average Gift"))
    print("----------------------------------------------------------------------------")
    current_name = donor_table[0][0]
    donor_total = 0
    num_donor = 0
    for row in donor_table:
        if current_name != row[0]:
            print("{:<20}   ${:>10.2f}   {:>10d}   ${:>10.2f}".format(current_name, donor_total, num_donor,
                                                             donor_total / num_donor))
            current_name = row[0]
            donor_total = row[1]
            num_donor = 1
        else:
            donor_total += row[1]
            num_donor += 1
    else:
        print("{:<20}   ${:>10.2f}   {:>10d}   ${:>10.2f}".format(current_name, donor_total, num_donor,
                                                                  donor_total / num_donor))
        print()


def send_letters(donor_table):
    pass


# Main menu
if __name__ == "__main__":
    while True:
        print("1. Send a Thank You\n2. Create a Report\n3. Send Letters to All\n4. Quit")
        answer_dict = {1: thank_you,
                       2: create_report,
                       3: send_letters,
                       4: "quit"}
        answer = input("Please select an option. >")
        if answer == "4":
            print("Have a nice day.")
            break
        else:
            answer_dict[answer](donor_table)