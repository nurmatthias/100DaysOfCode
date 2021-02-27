#Write your code below this line 👇
def prime_checker(number):
    prime = True

    if number % 2 == 1:
        for check in range(3, int(number/2), 2):
            if number % check == 0:
                prime = False
    else:
        prime = False


    if prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")




#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)