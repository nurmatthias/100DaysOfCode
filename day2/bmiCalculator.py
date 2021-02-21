# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

height = float(height.replace(',', '.'))
weight = float(weight.replace(',', '.'))

bmi = weight / height**2

print(int(round(bmi)))
