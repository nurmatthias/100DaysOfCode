############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

import random
from black_jack_fnc import clear_screen
from black_jack_art import logo

print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

player_hand = []
cpu_hand = []

def deal_card(no_of_cards):
    """Returns a random card from the deck."""
    return random.choices(cards, k=no_of_cards)

def calculate_score(hand):
    """Calculates the score of a given hand."""
    score = 0
    for card in hand:
        score += card
    
    if score > 21 and 11 in hand:
        score -= 10

    return score

def check_bj(hand):
    score = calculate_score(hand)
    
    if score == 21:
        return True
    else:
        return False

def check_score_over21(hand):       
    score = calculate_score(hand)

    if score > 21:
        return True
    else:
        return False

def cpu_open_hand(hand):
    open_hand = ["_"] * len(hand)
    for index in range(0, len(hand)-1):
        open_hand[index] = hand[index]
    
    return open_hand

    

def play():
    round_runs = True
    player_turn = True
    cpu_turn = False

    player_hand = deal_card(2)
    cpu_hand = deal_card(2)

    if check_bj(cpu_hand):
        round_runs = False

    elif check_bj(player_hand):
        round_runs = False


    while round_runs and player_turn:
        print(f"Your hand {player_hand}, CPU hand {cpu_open_hand(cpu_hand)}")

        next_card = input("Draw next card? y/n ").lower()
        if next_card == "y":
            player_hand.extend(deal_card(1))
        else:
            player_turn = False
            cpu_turn = True

        if check_bj(player_hand):
            round_runs = False
            print(f"You win with BlackJack!")
            return

        if check_score_over21(player_hand):
            round_runs = False
            print(f"You lose with {calculate_score(player_hand)}")
            return


    while round_runs and cpu_turn:    
        print(f"Your hand {player_hand}, CPU hand {cpu_open_hand(cpu_hand)}")

        if calculate_score(cpu_hand) < 16:
            cpu_hand.extend(deal_card(1))
        else:
            player_turn = False
            cpu_turn = False

        if check_bj(cpu_hand):
            round_runs = False
            print(f"CPU win's with BlackJack!")
            return

        if check_score_over21(cpu_hand):
            round_runs = False
            print(f"CPU lose with {calculate_score(cpu_hand)}")
            return


    print(f"Your final hand {player_hand}, CPU final hand {cpu_hand}")

    cpu_score = calculate_score(cpu_hand)
    player_score = calculate_score(player_hand)
    if cpu_score >= player_score:
        print(f"You lose with {player_score} to {cpu_score}")
    else:
        print(f"You win with {player_score} to {cpu_score}")

game_run = True
round = 0
while game_run:
    if round == 0:
        play()
        round += 1
    else:
        play_again = input("Another round? y/n ").lower()
        if play_again == "y":
            clear_screen()
            play()
            round += 1
        else:
            game_run = False

    

print(f"Game ends after {round} rounds")