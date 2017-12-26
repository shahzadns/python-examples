# learn Python - 26-dec-17
# 15 - Help me Help me !

# ===============
# 15.1 Using Modules
# definition for beginners
# Modules are code libraries that contain functions we can call from our code.
# They make our lives easier by implementing the hard stuff for us.

# examples
import random
ticket = random.randint(1, 1000)
print(ticket)

# ---
import math
result = math.sqrt(3)
print(result)

# introduction to "pip"
# a 3rd party open source python package manager that helps install modules for us.
# doc website : https://pip.pypa.io/en/stable/
# "pip" comes pre-installed with Python 3.4+ , for earlier try install "python get-pip.py"
# upgrading pip >> sudo -H pip install --upgrade pip

# installing modules using pip
# from terminal try format "pip install package-name"
# >>> pip install requests

# using request module to fetch some data, and parse the json to use as list/dictionary
import requests

request = requests.get('http://jsonplaceholder.typicode.com/users')
users_list = request.json()

print(users_list)

# ===============
# 15.2 Creating Modules

# create a file "users.gy" that contains following code
import requests


def get_users():
    request = requests.get('http://jsonplaceholder.typicode.com/users')
    return request.json()

# now consume our "weather.py" custom module to our mail script "app.py"
import users


def main():
    users_list = users.get_users()
    print('Available users are :', users_list)

main()
# ===============

