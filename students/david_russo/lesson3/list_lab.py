#!/usr/bin/env python

# Series 1

# Initial list of fruits
fruits = ["Apples", "Pears", "Oranges", "Peaches"]

# print list of fruits
print(fruits)

# prompt user for new fruit and append it to the fruits list
fruits.append(input("Enter a new fruit > "))

# print the modified fruits list
print(fruits)

# print the index and the corresponding fruit at the user supplied index
fruit_index = int(input("Enter a number between 1 and 5 > ")) - 1
print(fruit_index, fruits[fruit_index])

# Add another fruit to the beginning of the list and print it
fruits = ["Cherry"] + fruits
print(fruits)

# Add another fruit to the beginning of the list with .insert() and print it
fruits.insert(0, "Pineapple")
print(fruits)

for fruit in fruits:	
	if fruit[0] == 'P':
		print(fruit)

# Series 2



