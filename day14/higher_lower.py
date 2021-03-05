import random

from higher_lower_art import logo, vs
from higher_lower_data import data
from higher_lower_fnc import clear_screen


def get_random_account():
  return random.choice(data)


def format_data(account):
  name = account["name"]
  description = account["description"]
  country = account["country"]
  return f"{name}, a {description}, from {country}"


def check_answer(guess, follower_a, follower_b):

    if follower_a > follower_b:
        return guess == "a"
    else:
        return guess == "b"


def play():
    print(logo)

    game_runs = True

    score = 0
    account_a = get_random_account()
    account_b = get_random_account()


    while game_runs:
        account_a = account_b
        account_b = get_random_account()
        while account_a == account_b:
            account_b = get_random_account()


        print(f"Score: {score}")
        print("")
        print(f"Compare A: {format_data(account_a)}")
        print(vs)
        print(f"Against B: {format_data(account_b)}")

        guess = input("How has more follower? Type 'a' or 'b' ").lower()

        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]

        aswer_correct = check_answer(guess, a_follower_count, b_follower_count)

        clear_screen()
        if aswer_correct:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            game_runs = False
            print(f"Sorry, that's wrong. Final score: {score}")

play()