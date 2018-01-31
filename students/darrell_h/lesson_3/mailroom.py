#!/usr/local/bin/python3

donors = [['jack', [100, 200, 300, 400]],
          ['mary', [3000, 5000]],
          ['frank', [29.50, 31]],
          ['jane', [3000, 5000]],
          ['scrouge', [1, 2, 3]],
          ['bob', [6000000, 7000000, 8000000]]]


def send_thank_you():
    donor_names = get_names()  # create a list of names only
    while True:
        response = input("\nEnter a name of a donor ('list' for list )\n")
        if response == 'list':
            print("\nExisting donors\n", "\n".join(donor_names))
        elif response in donor_names or response.isalpha():  # existing donor
            add_donation(response)
            break
        # elif response.isalpha():  # checks the string contains numerical vals
        #     add_donation(response)
        #     break


def create_report():
    data = []
    print('\ncreating a report\n')
    data = get_summary()
    heading = "Donor Name | Total Given | Num Gifts | Average Gift\n"
    seperator = "-----------------------------------------------------\n"
    print(heading, seperator)
    for item in data:
        print("{:10} ${:10} {:10} {:15}".format(item[0], item[1], item[2], item[3]))
    # print(heading , "\n".split(data))


def add_donation(donor_name):
    while True:
        donation = input(
            f"\nEnter a donation amount for {donor_name.capitalize()}: ")
        if donation.isnumeric():
            print(f'addiing {donation} donation to {donor_name}')
            for index, donor in enumerate(donors):
                if donor[0] == donor_name:  # existing donor
                    donors[index][1].append(int(donation))
                else:
                    pass
            print('added donation successfully')
            print(donors)
            break
    return True

def get_summary():
    summary = []
    for donor in donors:
        # add name , total donation , # of donations, average donation
        summary.append([donor[0], sum(donor[1]), len(donor[1]), sum(donor[1]) / len(donor[1])])
    return summary



def get_names():
    names = []
    for donor in donors:
        names.append(donor[0])
    return names


if __name__ == "__main__":
    while True:
        choice = input("\nenter a number from this list\n"
                       "1 - Send a Thank You\n"
                       "2 - Create a Report\n"
                       "3 - Quit\n")
        if choice == '1':
            send_thank_you()
            break
        elif choice == '2':
            create_report()
            break
        elif choice == '3':
            print('Exiting...')
            quit()
            break
