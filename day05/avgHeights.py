# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
allHeights = 0
entryCounter = 0
for height in student_heights:
    allHeights += height
    entryCounter += 1

print(f"avg. height is {allHeights/entryCounter}")