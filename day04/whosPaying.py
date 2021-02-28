# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random

selectedIndex = random.randint(0, len(names) - 1)
choice = names[selectedIndex]

print(f"{choice} is going to buy the meal today!")

choice = random.choice(names)
print(f"{choice} is going to buy the meal today!")
