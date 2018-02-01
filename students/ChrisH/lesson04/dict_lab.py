#!/usr/bin/env python3
# -----------------------------------------------------------
# dict_lab.py
#  demonstrates basic Python dictionaries
# -----------------------------------------------------------

def dictionaries():

    # Dictionaries 1
    data = {'name':'Chris', 'city':'Seattle', 'cake':'Chocolate'}
    print("Dictionary:", data)
    print("Deleting cake.")
    del data['cake']
    print("Dictionary:", data)
    print("Adding fruit.")
    data['fruit'] = 'Mango'
    print("Dictionary:", data)
    print("Keys:", ", ".join([x for x in data.keys()]))
    print("Values:", ", ".join([x for x in data.values()]))
    print("Is cake a key?", bool(data.get('cake', 0)))
    print("Is Mango a value?", 'Mango' in data.values())




if __name__ == "__main__":
    dictionaries()