#Day 03 - Student: Erica Calaça
#You are going to write a program that tests the compatibility between two people.

#To work out the love score between two people:
##Take both people's names and check for the number of times the letters in the word TRUE occurs. Then check for the number of times the letters in the word LOVE occurs. Then combine these numbers to make a 2 digit number.

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
lower_case_name1 = name1.lower()
lower_case_name2 = name2.lower()

# TRUE test
sum1 = 0

if lower_case_name1.count("t") != 0 or lower_case_name2.count("t") !=0:
  sum1 = lower_case_name1.count("t")
  sum1 = sum1 + lower_case_name2.count("t")

if lower_case_name1.count("r") != 0 or lower_case_name2.count("r") !=0:
  sum1 = sum1 + lower_case_name1.count("r")
  sum1 = sum1 + lower_case_name2.count("r")

if lower_case_name1.count("u") != 0 or lower_case_name2.count("u") !=0:
  sum1 = sum1 + lower_case_name1.count("u")
  sum1 = sum1 + lower_case_name2.count("u")

if lower_case_name1.count("e") != 0 or lower_case_name2.count("e") !=0:
  sum1 = sum1 + lower_case_name1.count("e")
  sum1 = sum1 + lower_case_name2.count("e")

sum1 = sum1*10

#LOVE TEST

if lower_case_name1.count("l") != 0 or lower_case_name2.count("l") !=0:
  sum1 = sum1 + lower_case_name1.count("l")
  sum1 = sum1 + lower_case_name2.count("l")

if lower_case_name1.count("o") != 0 or lower_case_name2.count("o") !=0:
  sum1 = sum1 + lower_case_name1.count("o")
  sum1 = sum1 + lower_case_name2.count("o")

if lower_case_name1.count("v") != 0 or lower_case_name2.count("v") !=0:
  sum1 = sum1 + lower_case_name1.count("v")
  sum1 = sum1 + lower_case_name2.count("v")

if lower_case_name1.count("e") != 0 or lower_case_name2.count("e") !=0:
  sum1 = sum1 + lower_case_name1.count("e")
  sum1 = sum1 + lower_case_name2.count("e")

if sum1 > 10 or sum1 < 90:
  print(f"Your score is {sum1}, you go together like coke and mentos.")
elif sum1 > 40 and sum1 < 50:
  print(f"Your score is {sum1}, you are alright together.")
else:
  print(f"Your score is {sum1}.")