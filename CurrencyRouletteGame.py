# This game will use the free currency api to get the current exchange rate from USD to ILS,
# will generate a new random number between 1-100 a will ask the user what he thinks is the value
# of the generated number from USD to ILS,
# depending on the user’s difficulty his answer will be correct if the guessed value is between
# the interval surrounding the correct answer
# Properties
# 1. Difficulty
# Methods
# 1. get_money_interval -Will get the current currency rate from USD to ILS and will generate an interval as follows:
# a. for given difficulty d, and total value of money t the interval will be: (t - (5 - d), t + (5 - d))
# 2. get_guess_from_user - A method to prompt a guess from the user to enter a guess of value to a given amount of USD
# 3. play - Will call the functions above and play the game. Will return True / False if the user lost or won.


from GameSettings import user_name, game_difficulty

import requests
import random


def play_roulette():
    # Printing massage while fetching exchange rates from API
    print("Let me check the current exchange rate...\n")
    random_number, min_range, max_range = get_money_interval()
    print("Done! Let's play!\n")
    guessed_num = get_guess_from_user(random_number)
    # Comparing the results
    if min_range <= guessed_num <= max_range:
        print(f"Amazing {user_name}! You know your stuff!!")
        return True
    else:
        print("No luck...seems that you have some homework to do :)")
        return False


def get_money_interval():
    # Getting conversion data from Openexchangerates API
    exchange = requests.get('https://openexchangerates.org/api/latest.json?app_id=d9245db001f94ce48e765311836ce0fa'
                            '&symbols=ILS')
    rate = {}
    rate.update(exchange.json()['rates'])
    ils_rate = rate.get('ILS')

    # Generating interval based on difficulty
    random_num = random.randint(1, 100)
    total_amount = float("{:.2f}".format(random_num * ils_rate))
    min_range = total_amount - (5 - game_difficulty)
    max_range = total_amount + (5 - game_difficulty)

    return random_num, min_range, max_range


# Getting guess from user
def get_guess_from_user(usd_amount):
    user_guess = float(input(f"{user_name}, guess: How much IL Shekels, {usd_amount} Dollars worth?\n"))
    return user_guess
