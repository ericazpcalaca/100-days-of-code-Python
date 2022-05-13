#Day 04 - Student: Erica Calaça

#Make a rock, paper, scissors game.

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

game_draw = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice > 2 or user_choice < 0:
  print("Invalid code. You lost")
else:
  print(game_draw[user_choice])
  print("Computer:")
  computer_choice = random.randint(0,2)
  print(game_draw[computer_choice])

  if user_choice == computer_choice:
    print("Its a tie :O")
  
  if user_choice == 0 and computer_choice == 1:
    print("You lost!")
  elif user_choice == 0 and computer_choice == 2:
    print("You won!")

  if user_choice == 1 and computer_choice == 0:
    print("You won!!")
  elif user_choice == 1 and computer_choice == 2:
    print("You lost!")

  if user_choice == 2 and computer_choice == 0:
    print("You lost ;;")
  elif user_choice == 2 and computer_choice == 1:
    print("You wooonnnn")

