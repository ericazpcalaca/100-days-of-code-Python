#Day 04 - Student: Erica CalaÃ§a

#You are going to write a program which will mark a spot with an X.
#First your program must take the user input and convert it to a usable format.
#Next, you need to use it to update your nested list with an "x".

# ð¨ Don't change the code below ð
row1 = ["â¬ï¸","â¬ï¸","â¬ï¸"]
row2 = ["â¬ï¸","â¬ï¸","â¬ï¸"]
row3 = ["â¬ï¸","â¬ï¸","â¬ï¸"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# ð¨ Don't change the code above ð

#Write your code below this row ð
x = [int(a) for a in str(position)]
column_user = int(x[0])
row_user = int(x[1])

treasure = map[row_user-1]
treasure[column_user-1] = "X"

#Write your code above this row ð
# ð¨ Don't change the code below ð
print(f"{row1}\n{row2}\n{row3}")