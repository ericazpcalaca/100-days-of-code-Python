#Day 04 - Student: Erica Calaça

#You are going to write a program which will select a random name from a list of names. The person selected will have to pay for everybody's food bill.

import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆
#Write your code below this line 👇
count = len(names)
random_integer = random.randint(1,count - 1)

print(f"{names[random_integer]} is going to buy the meal today!")