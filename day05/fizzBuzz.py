#Write your code below this row 👇

# Erster Versuch
for number in range(1, 101):
    output = ""

    if number % 3 == 0:
        output += "Fizz"
    if number % 5 == 0:
        output += "Buzz"
    if output == "":
        output = number

    print(output)


print("--------------------------------------")

# Zweiter Versuch
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
