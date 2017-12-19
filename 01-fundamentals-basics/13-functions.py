# learn Python - 18-dec-17
# 13 - Functions

# ===============
# 13.1 introduction to functions

# common imports for examples
import math
import random


# defining a custom function
def hello_world():
    print('hello world !')


# calling the function
hello_world()


# one more example of an average
def average(numbers):
    total = 0

    for price in numbers:
        total += price

    avg = total / len(numbers)
    return avg


prices = [12, 20, 3.4, 4, 5.60]
result = average(prices)
print('the average price is :', result)

daily_users = [56, 20, 34, 40, 12]
result = average(prices)
print('the average daily users are :', math.floor(result))


# ===============
# 13.2  main function and calling main()

# intro to best practice of keeping "main" function
# to keep the initialization execution code

def main():
    daily_users = [56, 20, 34, 40, 12]
    result = average(prices)
    print('the average daily users are :', math.floor(result))


main()


# local and global scope
# similar to JS

# ===============
# 13.3  Spam Van functions
# playing more with functions

# print the menu
# take the order
# calculate the total bill


def print_menu(menu):
    for name, price in menu.items():
        print(name, ' : $', format(price, '.2f'))


def get_order(menu):
    orders = []
    order = input('What would you like to order? (Q to Quit)')

    while order.upper() != 'Q':
        found = menu.get(order)
        if found:
            orders.append(order)
        else:
            print('Sorry, product does not exist.')

        print('Anything else ? (Q to Quit)')

    return orders


def bill_total(orders, menu):
    total = 0

    for order in orders:
        total += menu[order]

    return total


def main():
    menu = {'product x': 0.50, 'product y': 1.99}
    print_menu(menu)
    orders = get_order(menu)
    total = bill_total(orders, menu)
    print('You ordered', orders)
    print('Your total is: $', format(total, '.2f' ))


main()

# ===============
