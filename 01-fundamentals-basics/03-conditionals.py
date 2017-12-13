
# learn Python - 12-dec-17


# ===============
# 3.1 conditionals

# ---
# comparators (comparison operators)
# there are 6 of them
# <, <=, ==, >=, >, and !=

# >>> 5 == 5 # True - notice the capital "T" unlike JS
# >>> 5 != 5 # False

# ---
# - booleans.. True or False
is_raining = True

# ---
# - if else

num_knights = 2

if num_knights < 3:
  print('Retreat !') # this is called code block - indented with 4 spaces
  print('Another nested statement')
else:
  print('March on yayy !')
print('this always runs as norm, not an else block')

# ---
# another example with if, else if, and else
rain_speed = 6

if rain_speed < 5:
    print('Just a Scotch mist')
elif rain_speed < 7:
    print('achi barish hy')
elif rain_speed <= 10:
    print('solid barish hy')
else:
    print('It\'s a real Cow-quaker out there')

# ---
# combining conditionals (and, or)

day = 'Wednesday'

if rain_speed < 5 or day == 'Monday':
  print('do something')

elif rain_speed and day == 'Wednesday':
  print('do something')

else:
    print('do something else')

# -----
# taking input from the user
x = input('please enter the age')
# >>>print(x) # '25' - we have to typecast it as int(x) to a number.


# ===============
# topic:
# Dictionaries

slang = ['apple', 'banana']
translations = ['soof', 'kelo']

del slang[0]
print(slang)

# ===============
