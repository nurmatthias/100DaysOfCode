print("Welcome to the rollercoaster!")

height = int(input("What is your height in cm? "))

if height >= 120:
    bill = 0
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7")
    else:
        bill = 12
        print("Adult tickets are $12")

    wantsPhoto = input("Do you want a photo taken Y or N. ")
    if wantsPhoto == "Y":
        bill += 3

    print(f"Your final bill is {bill}")


else:
    print("Soryy, you have to grow taller before you can ride!")