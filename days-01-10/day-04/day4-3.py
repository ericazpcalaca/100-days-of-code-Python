#Day 04 - Student: Erica Calaça

#You are going to write a program which will mark a spot with an X.
#First your program must take the user input and convert it to a usable format.
#Next, you need to use it to update your nested list with an "x".

# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
x = [int(a) for a in str(position)]
column_user = int(x[0])
row_user = int(x[1])

treasure = map[row_user-1]
treasure[column_user-1] = "X"

#Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")