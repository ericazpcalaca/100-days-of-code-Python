#Day 03 - Student: Erica CalaΓ§a
#Write a program that works out whether if a given year is a leap year. 

# # π¨ Don't change the code below π
year = int(input("Which year do you want to check? "))
# π¨ Don't change the code above π

#Write your code below this line π
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