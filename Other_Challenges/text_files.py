# Reading a file
file_path = "/Users/isobel/Desktop/SheCodes/Week4_Python/days_of_the_week.txt"

days_file = open(file_path, 'r')
my_days = days_file.read()


# Writing  a file
title = "Days of the Week, Take 2"

new_path = '/Users/isobel/Desktop/SheCodes/Week4_Python/new_week.txt'
new_days = open(new_path,'w')

new_days.write(title)
print(title)

all_days = "Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday."

new_days.write(all_days)
print(all_days)

# Closing a file

days_file.close()
new_days.close()



