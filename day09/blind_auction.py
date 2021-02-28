from blind_auction_fnc import clear_screen
from blind_auction_art import logo
#HINT: You can call clear() to clear the output in the console.

print(logo)

bids = {}

bidding_finished = False

while bidding_finished:
    name = input("What is your name?\n")
    price = input("How many do you want to bid? $")

    bids[name] = int(price)

    should_continue = input("Are there any other users? y/n ")
    if should_continue == "n":
        bidding_finished = True
    else:
        clear_screen()

# find highest bidder
highest_bid = 0
winner = ""
for bidder in bids:
    if bids[bidder] > highest_bid:
        winner = bidder
        highest_bid = bids[bidder]

print(f"{winner} won with ${highest_bid}")