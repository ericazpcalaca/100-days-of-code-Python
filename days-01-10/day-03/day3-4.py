#Day 03 - Student: Erica CalaΓ§a
#Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program.
#Based on a user's order, work out their final bill.

# π¨ Don't change the code below π
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# π¨ Don't change the code above π

#Write your code below this line π

bill = 0
size = size.upper()
add_pepperoni = add_pepperoni.upper()
extra_cheese = extra_cheese.upper()

if size == "S":
  bill +=15
elif size == "M":
  bill +=20
elif size == "L":
  bill +=25
else:
  print("Please put a valid letter.")

if add_pepperoni == "Y":
  if size == "S":
    bill += 2
  else:
    bill +=3

if extra_cheese == "Y":
  bill +=1

print(f"Your final bill is: ${bill}")






