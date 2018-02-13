# Write some functions that take a sequence as an argument, and return a copy of that sequence:
#
#     with the first and last items exchanged.
#     with every other item removed.
#     with the first and last 4 items removed, and every other item in between.
#     with the elements reversed (just with slicing).
#     with the middle third, then last third, then the first third in the new order.
#

seq = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
# seq = 'this is a string'


print("Original Sequence")
print(seq)


def exchange_first_last(seq):
    return seq[-1:] + seq[1:-1] + seq[:1]


print(" ")
print("Exchange First Last")
print(exchange_first_last(seq))


def every_other(seq):
    return seq[0:-1:2]


print(" ")
print("Every Other")
print(every_other(seq))

#     with the first and last 4 items removed, and every other item in between.


def first4_and_last4_removed_every_other(seq):
    return seq[4:-4:2]


print(" ")
print("The First 4 and Last 4 Removed, with Every Other in Between")
print(first4_and_last4_removed_every_other(seq))


def elements_reversed_with_slicing(seq):
    return seq[::-1]


print(" ")
print("Elements Reversed with Slicing")
print(elements_reversed_with_slicing(seq))


#     with the middle third, then last third, then the first third in the new order.


third = round(len(seq)/3)
print('third')
print(third)

first = seq[:third]
mid = seq[third:-third]
last = seq[-third:]

new = mid + last + first

print(" ")
print("new")
print(new)

