# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
names = name1.lower() + name2.lower()
score = 0

score += names.count("t")
score += names.count("r")
score += names.count("u")
score += names.count("e")
score *= 10

score += names.count("l")
score += names.count("o")
score += names.count("v")
score += names.count("e")

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")