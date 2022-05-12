#Day 03 - Student: Erica Calaça
#Write a program that works out whether if a given year is a leap year. 

# # 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# on every year that is evenly divisible by 4 
  # **except** every year that is evenly divisible by 100 
    #**unless** the year is also evenly divisible by 400

if year%4 == 0:
  if year%100 == 0:
    if year % 400 == 0:
      print("Leap year")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else: 
  print("Not leap year.")