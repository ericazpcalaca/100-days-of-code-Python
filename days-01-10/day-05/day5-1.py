# Day 05 - Student: Erica CalaΓ§a
# You are going to write a program that calculates the average student height from a List of heights.

# π¨ Don't change the code below π
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# π¨ Don't change the code above π
#Write your code below this row π
heights = 0
count = 0
for student in student_heights:
  heights += student
  count += 1

average_height = heights/count

print(round(average_height))
  



