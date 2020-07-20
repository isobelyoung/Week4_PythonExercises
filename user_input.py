# Exercise 1: Accept two numbers from the user and calculate multiplication

a = int(input("Please choose a number: "))
b = int(input("Choose another number! "))

c = a*b

print(f"{a} multiplied by {b} equals {c}!")

# Exercise  2: Display “My Name Is James” as “My**Name**Is**James” using output formatting of a print() function

my_string = "My Name Is James"
new_string = my_string.split()
print('**'.join(new_string))

print('My', 'Name', 'Is', 'James', sep='**')

# Exercise Question 3: Convert decimal number to octal using print() output formatting

num = 8

print('{1} in octal format is {0:o}'.format(num, num))

# Exercise Question 5: Accept list of 5 float numbers as a input from user


float_numbers = []
num = int(input("Enter the number of floats in your list : "))

for i in range(0, num):
    print(f"Enter number at index {i}:")
    user_num = float(input())
    float_numbers.append(user_num)
    
print("Your list of floats is ", float_numbers)

