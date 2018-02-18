#!/usr/bin/env python3

# Activity 1
print("{:-^70s}".format("Activity One"), end='\n')

tst_dict = {'name': 'Chris', 'city':'Seattle', 'cake':'Chocolate'}
print(f'Here are the Keys & Values in the dictonary: \n{tst_dict}\n')
# remove cake entry
tst_dict.pop("cake")

print(f'Here are the values after removing the "cake" key: \n{tst_dict}\n')
tst_dict["fruit"] = "Mango"
print(f'Here are the values after adding "fruit":"Mango "\n {tst_dict}\n')
print(f'Here are the dictionary "keys": \n{tst_dict.keys()}\n')

print("{:-^70s}".format("Activity Two"), end='\n')