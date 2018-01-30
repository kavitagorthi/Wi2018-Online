#!/usr/local/bin/python3

fruit = ['Apples', 'Pears', 'Oranges', 'Peaches']


def display_list():
    print(fruit)


def series_1():
    display_list()
    fruit.append(input("enter a new fruit >"))
    display_list()
    while True:
        number = input("Enter a number between 1 and {:d} ".format(len(fruit)))
        if int(number) in range(1, len(fruit) + 1):
            print('Fruit number {:d} is a {:s}'.format(
                int(number), fruit[int(number) - 1]))
            break
    fruit[0] = 'strawberry'
    fruit.insert(0, 'fig')
    display_list()

    for item in fruit:
        if item[0] == 'P':
            print(item)


def series_2():
    display_list()
    fruit.pop(-1)  # remove last element
    fruit.extend(fruit)  # multiple by 2
    display_list()

    while True:
        fruit_to_remove = input('enter a fruit to delete ')
        if fruit_to_remove in fruit:
            while fruit_to_remove in fruit:
                fruit.remove(fruit_to_remove)
            display_list()
            break


# series_1()
series_2()
