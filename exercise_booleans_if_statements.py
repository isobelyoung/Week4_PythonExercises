# Q1

import random 

print("***QUESTION 1***")

random_bit = random.getrandbits(1)

# moths_in_house = False

if random_bit == 0:
    moths_in_house = False;
else: 
    moths_in_house = True;

if moths_in_house == True:
    print("Get  the moths!")
else: 
    print("No threats detected.")

# Q2

hooman_home = random.getrandbits(1)

# mitch_is_home = False

if hooman_home == 0:
    mitch_is_home = False;
else: 
    mitch_is_home = True;

print("***QUESTION 2***")

if mitch_is_home == True:
    if moths_in_house == True:
        print("Hooman! Help me get the moths!")
    else: 
        print("Climb on Mitch.")
else:
    if moths_in_house == True:
        print("Meooooooooow! Hissssss!")
    else: 
        print("No threats detected.")

# Q3 

print("***QUESTION 3***")


traffic_lights = ["Red", "Green", "Amber"]
light_colour = random.choice(traffic_lights)


is_car = random.getrandbits(1)

if is_car == 0:
    car_detected = False
else: 
    car_detected = True

if light_colour == "Red":
    if car_detected == False:
        print("Do nothing.")
    else:
        print("Flash!")
elif light_colour == "Green":
    if car_detected == False:
        print("Do nothing.")
    else:
        print("Do nothing.")
else:
    if car_detected == False:
        print("Do nothing.")
    else:
        print("Do nothing.")

# Q4

print("***QUESTION 4***")

user_height = int(input("Hi there! How tall are you in centimetres? Please only enter the number "))

print(f"Your height is {user_height}cm.")

if user_height >= 120:
    print("Hop on!")
elif 120 > user_height >= 50:
    print("Sorry, not today :(")
else: 
    print("Thanks for choosing to have fun with us today!")