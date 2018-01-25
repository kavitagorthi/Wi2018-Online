#!/usr/bin/env python3

"""Lesson03 - Assignment 2 - Operations on lists."""

# Series 1
fruit1 = ['Apples', 'Pears', 'Oranges', 'Peaches']
print(fruit1)
response_fruit = input("Type the name of a fruit > ")
fruit1.append(response_fruit)
print(fruit1)
prompt_number = 'Type a number in range {} > '.format(len(fruit1))
response_number = int(input(prompt_number))
print(response_number, fruit1[response_number - 1])
fruit1 = ['Melons'] + fruit1
print(fruit1)
fruit1.insert(0, 'Lemons')
print(fruit1)
for name in fruit1:
    if name.lower().startswith('p'):
        print(name, end=' ')
print()

# Series 2
##print(fruit1)
##fruit2 = fruit1[:-1] # any better way to remove the last item? pop() w/out print?
##print(fruit2)
##print()

def find_del_fruit(seq):
    print(seq)
    chosen_fruit_to_del = input("Type the name of a fruit to delete > ")
    if chosen_fruit_to_del not in seq:
        print('Not found. Try again.', end=' ')
        find_del_fruit(seq)
    new_fruit = []
    for item in seq[:]:
        if item != chosen_fruit_to_del:
            new_fruit.append(item)
    return new_fruit

##print(find_del_fruit(fruit2))
##print(find_del_fruit(fruit2*2))

# Series 3

def do_you_like(seq):
    new_seq = []
    for item in seq:
        prompt = 'Do you like {}? yes/no > '.format(item.lower())
        response = input(prompt)
        while not (response == 'yes' or response == 'no'):
            response = input(prompt)
        if response == 'yes':
            new_seq.append(item)
    return new_seq

##print(do_you_like(fruit1))


# Series 4

def reverse_each_fruit(seq):
    # Make a copy of the list
    reversed_seq = seq[:] 
    # and reverse the letters in each fruit in the copy.
    for index, fruit in enumerate(seq):
        reversed_seq[index] = fruit[::-1]
    # Delete the last item of the original list.
    seq = seq[:-1]
    # Display the original list and the copy.
    print(seq)
    print(reversed_seq)

reverse_each_fruit(fruit1)


def reverse_each_fruit2(seq):
    reversed_seq = [] 
    for fruit in seq:
        reverted_fruit = fruit[::-1]
        reversed_seq.append(reverted_fruit)
    # Delete the last item of the original list.
    seq = seq[:-1]
    # Display the original list and the copy.
    print(seq)
    print(reversed_seq)
