# Day 05 - Student: Erica Calaça

#Write your code below this row 👇

for i in range(1,101):
  if i%3 != 0:
    if i% 5 != 0:
      print(i)
    elif i%5 == 0:
      print("Buzz")
  elif i%3 == 0 and i%5 ==0:
    print("Fizz Buzz")
  elif i%3 == 0:
    print("Fizz")
  