# Day 05 - Student: Erica CalaΓ§a

# You are going to write a program that calculates the highest score from a List of scores.

# π¨ Don't change the code below π
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# π¨ Don't change the code above π

#Write your code below this row π
max = 0

for score in student_scores:
  if score > max:
    max = score

print(f"The highest score in the class is: {max}")
  



