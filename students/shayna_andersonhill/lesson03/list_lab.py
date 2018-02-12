#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
#Shayna Anderson-Hill
#Goal: Learn the basic ins and outs of Python lists.
#02-10-2018

fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']
print(fruits)

response = input("Please user, give me a fruit > ")
fruits.append(response)
print(fruits)

response = input("Please user, give me a number > ")
print(response, fruits[(int(response)-1)])

fruits = ['Bananas'] + fruits
print(fruits)

#Displays fruits beginning with 'P'
for fruit in fruits:
    if fruit[0]=='P':
        print(fruit)


