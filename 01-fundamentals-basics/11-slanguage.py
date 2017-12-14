# learn Python - 14-dec-17
# 11 - SLanguage

# ===============
# 11.1 lists

empty = []
nums = [10, 20]
anything = ['lorem', True, 10, 123.456]
multi_dimensional = [20, 30, 30, [1, 2, 3]]

# slicing - similar to strings
greetings = ['hi', 'hello', 'good morning', 'good day']
greetings[0]
greetings[1:3]
greetings[3:]
greetings[:7]

# .append()
# adds a new item to the end of the list, returns nothing (or None ?)

slang = ['cheerio']
slang.append('cheeky')
slang.append('yonks')

# .remove()
# removes the item by-index or by-value, returns nothing (or None ?)

slang.remove('cheeky')

# del operator (note - the index should be valid - otherwise error raised)
# can use with dictionaries too, but not with strings
del slang[1]

# del with slice
del slang[3:]

# ===============
# 11.2 Dictionaries (objects in JavaScript)

# legacy with lists
slang = ['apple', 'banana']
translations = ['soof', 'kelo']

del slang[0]
del translations[0]
print(slang)

# the dictionary
slang = {
    'cheerio': 'goodbye',
    'foo': True,
    'lorem ipsum': 15.4,
    15: 'int as key',
    16.345: 'float as key'
}

# dynamic keys addition or updates

slang['new-key'] = 'the value'
slang[16] = False
# slang.16 = False # invalid syntax - error on dot "."

# delete the key (note - the index should be valid - otherwise error)
del slang['cheerio']

# .get() - get value by key (or to check if value so that to delete it)
slang.get('cheerio')  # returned value is 'goodbye'

# None - (like undefined in JavaScript)
result = slang.get('unknown-key')  # returned is None

if result:
    print('do something') # None evaluated as False in a conditional
else:
    print('key does\'nt exist')

# reading values from dictionaries
# slang['cheero'] # (can used with string, list too) - avoid, error raised if not available.
# slang.get('cheero') # recommended. no errors

translation = 'Sorry, my ' + slang.get('mate') + ' is a bit cheeky !'
print(translation)

# ===============
# 11.3 comparing and combining lists and dictionaries

# comparing lists
my_list = [1, 2, 3, 4]
his_list = [2, 3, 3, 4]
your_list = [1, 2, 3, 4]

# should have the same values and same order
print(my_list == his_list)  # False
print(my_list == your_list)  # True

# comparing dictionaries
my_dict = {1: 15, 'foo': 'bar'}
his_dict = {1: 15, 'baz': 'bar'}
your_dict = {'foo': 'bar', 1: 15}

# should have the same values only (no same order required)
print(my_dict == his_dict)  # False - values are diff
print(my_dict == your_dict)  # True - values are same, order not matter

# ---
# combining list and dictionaries, and reading 2 dimensional L & D

menus = {
    'lunch': ['SLT', 'ABC'],
    'dinner': {'FOO': 'xoxo'}
}

menus['lunch']
menus['lunch'][0]
menus['dinner']
menus['dinner']['FOO']

# ===============
