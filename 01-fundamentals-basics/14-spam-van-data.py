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
# 14.2


# ===============
