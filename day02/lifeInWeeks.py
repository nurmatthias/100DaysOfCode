# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
yearsRemain = 90 - int(age)
monthRemain = yearsRemain * 12
weeksRemain = yearsRemain * 52
daysRemain = yearsRemain * 365


print(f"You have {daysRemain} days, {weeksRemain} weeks, and {monthRemain} months left. ")