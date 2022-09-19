# MemoryGame.py
# The purpose of memory game is to display an amount of random numbers to the users for 0.7 seconds
# and then prompt them from the user for the numbers that he remember.
# If he was right with all the numbers the user will win otherwise he will lose.
# Properties
# 1. Difficulty
# Methods
# 1. generate_sequence - Will generate a list of random numbers between 1 and 101.
# The list length will be difficulty.
# 2. get_list_from_user - Will return a list of numbers prompted from the user.
# The list length will be in the size of difficulty.
# 3. is_list_equal - A function to compare two lists if they are equal. The function will return True / False.
# 4. play - Will call the functions above and play the game. Will return True / False if the user lost or won.

import random
import time

import GameSettings
from Score import add_score


def play_memory(difficulty):
    is_list_equal(difficulty)


def generate_sequence(difficulty):
    # Generating secret sequence
    random_list = []
    for i in range(difficulty):
        random_list.append(random.randint(1, 101))
    # Printing automated dialog with the user
    print(f"OK {GameSettings.user_name} , let's check your memory.....\n")
    time.sleep(2)
    print("TRY TO REMEMBER...\n")
    time.sleep(1)
    print(f"Are you ready {GameSettings.user_name}?\n")
    time.sleep(1)
    print("3...\n")
    time.sleep(1)
    print("2..\n")
    time.sleep(1)
    print("1.\n")
    time.sleep(1)
    print("GO!\n")
    time.sleep(1)
    for num in random_list:
        print(f"{num}\n")
        time.sleep(0.7)
    # Clearing console for hiding the numbers
    print("\n\n\n\n\n\n")
    return random_list


def get_list_from_user(difficulty):
    input_list = []
    print("Let's see if you got it right...\n")
    for i in range(difficulty):
        input_list.append(int(input("What's the next number?\n")))
    print(input_list)
    return input_list


def is_list_equal(difficulty):
    if generate_sequence(difficulty) == get_list_from_user(difficulty):
        print("WOW! You did it! What a Memory!")
        add_score(difficulty)
        return True
    else:
        print("Oops...You need to work on your memory")
        return False
