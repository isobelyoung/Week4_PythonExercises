# Q1

print("***QUESTION 1***")

foods = ["orange", "apple", "banana", "strawberry", "grape", "blueberry", 
["carrot", "cauliflower", "pumpkin"], "passionfruit", "mango", "kiwifruit"]

print(foods[0])
print(foods[2])
print(foods[-1])
print(foods[0:3])
print(foods[-3:])
print(foods[6][-1])

# Q2

print("***QUESTION 2***")

mailing_list = [
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

names = []

name_1 = input("Hi there! Type your name: ")
names.append(name_1)
name_2 = input("Thanks for that! What's your best friend's name? ")
names.append(name_2)
name_3 = input("Last one - what's your favourite name? ")
names.append(name_3)

print(f"Your list of names is: {names}")

# Q4 

print("***QUESTION 4***")

user_str = input("Hi there! What did the hungry computer eat? ")

split_str = user_str.split()
print(len(split_str), split_str)

all_chars = []
for  x in user_str:
    all_chars.append(x)
print(len(all_chars), all_chars)

if user_str == "Chips, one byte at a time":
    print("Congrats you computer coding comedian!")
else: 
    print("Chips, one byte at a time. Haha!")