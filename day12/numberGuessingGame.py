#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random

print('''
 _____                                                     _               
|  __ \                                                   | |              
| |  \/_   _  ___  ___ ___    __ _   _ __  _   _ _ __ ___ | |__   ___ _ __ 
| | __| | | |/ _ \/ __/ __|  / _` | | '_ \| | | | '_ ` _ \| '_ \ / _ \ '__|
| |_\ \ |_| |  __/\__ \__ \ | (_| | | | | | |_| | | | | | | |_) |  __/ |   
 \____/\__,_|\___||___/___/  \__,_| |_| |_|\__,_|_| |_| |_|_.__/ \___|_|   
                                                                           
''')

MODE = {
    "e": 10,
    "h": 5,
}

RUNNING = True

def play():
    mode_selected = input("Chose your difficulty level: (e)asy or (h)ard ")
    number_to_guess = random.randint(1, 100)

    guess = 0
    round = 1
    while guess != number_to_guess:

        print(f"{MODE[mode_selected] - round + 1} guesses left")
        guess = int(input("What do you think is the number? "))

        if guess > number_to_guess:
            print(f"Your guess {guess} is to high, try again")
            round += 1
        elif guess < number_to_guess:
            print(f"Your guess {guess} is to low, try again")
            round += 1
        else:
            print(f"You got it after {round} rounds")
        
        if round >= MODE[mode_selected]:
            print(f"You don't find the number {number_to_guess}, of corse next time")
            return


while RUNNING:
    play()
    play_again = input("Whant to play again? y/n ")

    if play_again == "n":
        RUNNING = False
        print("Thanks for playing!")



