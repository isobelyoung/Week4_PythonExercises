# Q1 

print("***QUESTION 1***")

# all_nums = []

# while True:
#     try:
#         if len(all_nums) == 0:
#             num = int(input("Enter a number! "))
#             all_nums.append(num)     
#         else:
#             num = int(input("Enter a number, or press enter: "))
#             all_nums.append(num)
#     except ValueError:
#         break


# sum_nums = sum(all_nums)

# print(f"The total sum of your numbers is {sum_nums}!")

# Q2

print("***QUESTION 2***")

mailing_list  =  [
    ["Roary", "roary@moth.catchers"],
    ["Remus", "remus@kapers.dog"],
    ["Prince Thomas of Whitepaw", "hrh.thomas@royalty.wp"], 
    ["Biscuit", "biscuit@whippies.park"],
    ["Rory", "rory@whippies.park"]
]


for i in range(len(mailing_list)):
    print(mailing_list[i][0] + ": " + mailing_list[i][1])

# Q3

print("***QUESTION 3***")

# names = []

# name_1 = input("Hi there! Type your name: ")
# names.append(name_1)
# name_2 = input("Thanks for that! What's your mum's name? ")
# names.append(name_2)
# name_3 = input("Last one - what's your dad's name? ")
# names.append(name_3)

# for x in names:
#     print(x)

# Q4

print("***QUESTION 4***")

groceries = [
    ["Baby Spinach", 2.78], 
    ["Hot Chocolate", 3.70], 
    ["Crackers", 2.10], 
    ["Bacon", 9.00], 
    ["Carrots", 0.56], 
    ["Oranges", 3.08]
]

customer_name = input("Hi there! Thanks for visiting our store. What's your name? ")

ind = 0
for x in groceries:
    n = int(input(f"How many units of {groceries[ind][0]} did you buy? "))
    groceries[ind].append(n)
    ind += 1

receipt_width = 28


print()
print("Your receipt is as  follows: ")
print()

header = "Izzy's Food Emporium"

print(header.center(receipt_width, '='))

total_cost = []


for i in range(len(groceries)):
    cost = groceries[i][1] * groceries[i][2]
    total_cost.append(cost)
    space_width = receipt_width - len(groceries[i][0]) - 6
    print("{}".format(groceries[i][0]) + " " * space_width + "${:.2f}".format(cost))

print("=" * receipt_width)

receipt_sum = sum(total_cost)
sum_str = "${:.2f}".format(receipt_sum)

print(sum_str.rjust(receipt_width, ' '))
