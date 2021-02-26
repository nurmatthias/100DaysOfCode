import random

from hangman_art import logo, stages 
from hangman_words import word_list
from hangman_fnc import clear_screen

clear_screen()
print(f"{logo}\n")

chosen_word = random.choice(word_list)
word_len = len(chosen_word)

lives = 6
display = ["_"] * word_len

end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    clear_screen()

    if guess.upper() in display:
        print("You guessed that already, try again...")
        continue

    for pos in range(word_len):
        if chosen_word[pos] == guess:
            display[pos] = guess.upper()

    if guess not in chosen_word:
        print(f"Your guess {guess.upper()} is not in that word, oh no... You loose a live")
        lives -= 1

    print(f"{stages[lives]} {' '.join(display)} \n")    

    if "_" not in display:
        end_of_game = True
        print("You won!")
    
    elif lives == 0:
        end_of_game = True
        print("You loose!")

    

