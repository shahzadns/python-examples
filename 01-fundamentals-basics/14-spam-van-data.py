# learn Python - 19-dec-17
# 14 - Spam Van Data

# ===============
# 14.1 writing files

# function to read, write, and append is
# open(path, mode) # modes are 'w', 'r', 'a'

# write an example hello world file
my_file = open('14-example-file-write.txt', 'w')

my_file.write('Hello\n')
my_file.write('World !\n')

my_file.close()

# another example

performances = {
    'Ventriloquism': '9:00am',
    'Snake Charmer': '12:00pm',
    'Amazing Acrobatics': '2:00pm',
    'Enchanted Elephants': '5:00pm'
}

schedule_file = open('schedule.txt', 'w')

for key, val in performances.items():
    schedule_file.write(key + ' - ' + val + '\n')

schedule_file.close()

# ===============
# 14.2 Reading files

# write an example hello world file
my_file = open('14-example-file-write.txt', 'r')

# read and print the entire content of the file
content = my_file.read()
print(content)

# read the each line (which looks for \n) - helpful with loops
print(my_file.readline())
print(my_file.readline())

# can directly be use with loop
dolar_menu = []
for line in my_file:
    dolar_menu.append(line.strip())  # strip exclude the \n

my_file.close()

# ===============
# 14.3 Try, Except
# using exceptions

# reading a file which does not exist, raise an exception
my_file = open('invalid-file.txt', 'r')
# Exception / Error Thrown
# FileNotFoundError: No such file or directory 'name.txt'
# this error will cause our program to crash.

# handle the exception
try:
    my_file = open('invalid-file.txt', 'r')
    print('file read success !', file.read())
except KeyError:
    print('File read error - file does not exist.')

# Python has over 60+ types of exceptions. a few examples.
# FileNotFoundError - File does not exist
# IndexError - Index out of bounds
# KeyError - Key does not exist
# NameError - Variable name does not exist in local or global
# ValueError - Value is the wrong type

# example of type casting error i.e. ValueError
price = input('Enter the price: ')  # 'yo'
try:
    price = float(price)
    print('Price = ', price)
except ValueError:
    print('Not a number !')

# extended version
price = input('Enter the price: ')  # 'yo'
try:
    price = float(price)
    print('Price = ', price)
except ValueError as err:
    print(err)  # could not convert the string to float: 'yo'

# multiple exceptions
# format taken from https://stackoverflow.com/questions/6470428/catch-multiple-exceptions-in-one-line-except-block
product = 'Product x'  # 'Product y'
price = 'yo'

try:
    if product == 'Product x':
        print('it will be released on : ', release_date) # will raise NameError
    else:
        print('Price = ', float(price))  # will raise ValueError
except (NameError, ValueError) as err:
    print(err)  # could not convert the string to float: 'yo'


# ===============
