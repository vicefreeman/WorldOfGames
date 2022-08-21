# The purpose of guess game is to start a new game, cast a random number between 1 to a
# variable called difficulty.The game will get a number input from the Properties
# 1. Difficulty
# 2. Secret number
# Methods
# 1. generate_number - Will generate number between 1 to difficulty and save it to secret_number.
# 2. get_guess_from_user - Will prompt the user for a number between 1 to difficulty and return the number.
# 3. compare_results - Will compare the secret generated number to the one prompted by the get_guess_from_user.
# 4. play - Will call the functions above and play the game. Will return True / False if the user lost or won.
import Score
from GameSettings import user_name, game_difficulty
from Score import add_score
import random


def greeting():
    print(f"{user_name}, LETS BEGIN!!! GOOD LUCK!!\n")


def generate_number():
    secret_number = random.randint(1, game_difficulty)
    return secret_number


def get_guess_from_user():
    user_input = ''
    # Verifying the input is a number
    while user_input is not int:
        try:
            user_input = int(input(f'Please guess a number between 1 and {game_difficulty}:\n'))
            return user_input
        except ValueError:
            print('oops... not a number...\n ')


def play_guess():
    greeting()
    gen_num = int(generate_number())
    guess_num = int(get_guess_from_user())
    if gen_num == guess_num:
        print(f"Nice One {user_name}! You Guessed it right!")
        add_score(game_difficulty)
        return True
    else:
        print("No luck...")
        return False
