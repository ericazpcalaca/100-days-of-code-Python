#Day 03 - Student: Erica CalaΓ§a
#Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.

# π¨ Don't change the code below π
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# π¨ Don't change the code above π

#Write your code below this line π

bmi = weight/(height**2)

if bmi < 18.5:
  print(f"Your BMI is {bmi:.2f}, you are underweight.")
elif bmi < 25:
  print(f"Your BMI is {bmi:.2f}, you have a normal weight.")
elif bmi < 30:
  print(f"Your BMI is {bmi:.2f}, you are slightly overweight")
elif bmi <35:
  print(f"Your BMI is {bmi:.2f}, you are obese.")
else:
  print(f"Your BMI is {bmi:.2f}, you are clinically obese.")