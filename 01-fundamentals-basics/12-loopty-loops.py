# learn Python - 14-dec-17
# 12 - Loopty Loops

# ===============
# 12.1 Loops and range

# with lists - pattern: for tempVar in list
prices = [0.23, 0.56, 0.33]
for price in prices:
    print('Price is :', price)

# using with some calculations
total = 0
prices = [0.23, 0.56, 0.33]

for price in prices:
    print('Price is :', price)
    total = total + price

print('Total Price is :', total)

# find the average, using already familiar len function
avg = total / len(prices)
print('Average is :', avg)

# generating random numbers with module "random"
import random

r1 = random.random()
# 0.80945 - number between 0.0 to 1.0

r2 = random.choice([1, 3, 5, 7, 9])
# 3 - random choice from the given list

r3 = random.randint(1, 1000)
# 902 - random number between 1 to 1000

# range() function - auto generates a list of numbers
range(5)
# [1, 2, 3, 4, 5]

for i in range(5):
    print('num is :', i)

# range(start, stop, step) - # range advance usage
range(2005, 2012, 2)
# [2005, 2007, 2009, 2011]

for year in range(2005, 2012, 2):
    print('year is :', year)

# ===============
# 12.2 Spam Van menu

# loop with dictionaries
menu_prices = {'foo': 12, 'bar': 13, 'baz': 50}

# if to only use keys
for item in menu_prices:
    print('item name is :', item)

# if to use both keys and their values (need .items() too)
for key, value in menu_prices.items():
    print('price for ', key, 'is ', value)

# .items() trimmed last zero of the "value" floats, we need them back
# using format() function - to use 2 decimal places
for key, value in menu_prices.items():
    print('price for ', key, 'is ', format(value, '.2f'))

# dictionaries - get list of keys
menu_prices.keys()
# ['baz', 'foo', 'bar'] - why baz as first ? 0_0

# dictionaries - get list of values
menu_prices.values()
# [50, 12, 13] - - why 50 as first ? 0_0

# dictionaries - want to see .items() ? (not sure where else we can use)
menu_prices.items()
# [('baz', 50), ('foo', 12), ('bar', 13)]

# ===============
# 12.3 while loops

x = 1
while x <= 5:
    print('count: ', x)
    x += 1  # x++ does not work in python

# ---
# unlimited orders example
menu = {'product x': '$55', 'product y': '$66'}
orders = []

while True:

    # ask for the order
    order = input('Can I take your order? (Q to Quit)')

    # check if user wants to quit
    if order.upper() != 'Q':
        break

    found = menu.get(order)
    if found:
        orders.append(order)
    else:
        print('Sorry, product does not exist.')

print('your orders are:', orders)

# ---
# the "break" and "continue" keywords inside loop

# game - guess the number
import random

num = random.randint(1, 10)

guess = int(input('Guess a number between 1 and 10'))
times = 1

while guess != num:
    guess = int(input('Guess again'))
    times = times + 1

    if times == 3:
        break
if guess == num:
    print('You win!')
else:
    print('You lose! The number was ', num)

# ===============
