# Day 05 - Student: Erica Calaça
# You are going to write a program that calculates the average student height from a List of heights.

# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
#Write your code below this row 👇
heights = 0
count = 0
for student in student_heights:
  heights += student
  count += 1

average_height = heights/count

print(round(average_height))
  



