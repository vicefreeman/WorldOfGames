# The purpose of guess game is to start a new game, cast a random number between 1 to a
# variable called difficulty.The game will get a number input from the Properties
# 1. Difficulty
# 2. Secret number
# Methods
# 1. generate_number - Will generate number between 1 to difficulty and save it to secret_number.
# 2. get_guess_from_user - Will prompt the user for a number between 1 to difficulty and return the number.
# 3. compare_results - Will compare the secret generated number to the one prompted by the get_guess_from_user.
# 4. play - Will call the functions above and play the game. Will return True / False if the user lost or won.

import GameSettings
from Score import add_score
import random


def greeting():
    print(f"{GameSettings.user_name}, LETS BEGIN!!! GOOD LUCK!!\n")


def generate_number(difficulty):
    secret_number = random.randint(1, difficulty)
    return secret_number


def get_guess_from_user(difficulty):
    user_input = ''
    # Verifying the input is a number
    while user_input is not int:
        try:
            user_input = int(input(f'Please guess a number between 1 and {difficulty}:\n'))
            return user_input
        except ValueError:
            print('oops... not a number...\n ')


def play_guess(difficulty):
    greeting()
    gen_num = int(generate_number(difficulty))
    guess_num = int(get_guess_from_user(difficulty))
    if gen_num == guess_num:
        print(f"Nice One {GameSettings.user_name}! You Guessed it right!")
        add_score(difficulty)
        return True
    else:
        print("No luck...")
        return False
