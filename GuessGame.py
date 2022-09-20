# The purpose of guess game is to start a new game, cast a random number between 1 to a
# variable called difficulty.The game will compare the user's input with the generated sequence.


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
