
# learn Python - 12-dec-17


# ===============
# 2.1 strings

first_name = 'John'
last_name = 'Doe'
full_name = first_name + ' ' + last_name
print(full_name)

# ---
# external files
# script.py
# >>> python script.py
# John Doe

# ---
# comments
# this is a comment
# here hash to be called as "pound"

# ---
# typecasting
# convert the "int" to string before concatenating with string values

age = 25
phrase = 'i am ' + str(age) + ' years old.'

# ---
# special characters in strings
# \t for tabs
# \n for new lines

x = '\n\tHellen Goose'
y = 'daddy\'s girl'

print('my prints: ', x, y) # will print indented

# ===============
# 2.2 string behind the scenes

x = 'hello'
# >>> x[0] # 'h'

# what about incorrect index ? try this
# >>> x[10]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# IndexError: string index out of range

# ---
# len - tells the length of the string

x = len('hello')
# >>> x  # 5

# ---
# slicing strings (boundary)

word = 'python'
# >>>word[2:5] # 'tho' - word[ startIndex : beforeEndIndex]

# also
# >>> word[2:] # 'thon' - from 2 to till the end
# >>> word[:3] # 'pyt' - from start till index 3

# no error with incorrect index portion when ":" slicing is used
# >>>> word[100:]

# ---
# integer division

# x = 'evening' # length is 7
# >>> x[ len(x) / 2 ] # error because 3.5 is not an index
# >>> x[ len(x) // 2 ] # index will be 3. because (7 // 2) gives 3. (must for py3)

# ===============
