import GameSettings

game_is_on = True


# Greetings message and getting name from the user
def welcome(name=input("To get started, please enter your name: ")):
    print(f"\nHello {name} and welcome to the World of Games (WoG)!\nHere you can find many cool games to play.\n")
    GameSettings.user_name = name

    print(GameSettings.user_name)


# Importing Play functions
from GuessGame import play_guess
from MemoryGame import play_memory
from CurrencyRouletteGame import play_roulette


# Getting input from user and verifying requirements
def check_input(input_range):
    while game_is_on:
        try:
            user_input = int(input(f"Please enter your choice between 1 and {input_range}: \n"))
        except ValueError:
            print("Not a number")
            continue
        if user_input >= 0 and int(user_input) <= input_range:
            return user_input
            break
        else:
            print("Not in range")
            continue


# Loading choices of game and difficulty
def load_game():
    choose_game = ("Please choose a game to play:\n "
                   "1. Memory Game - a sequence of numbers will appear for 1 second and you "
                   "have to guess it back.\n "
                   "2. Guess Game - guess a number and see if you chose like the computer.\n "
                   "3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n")
    choose_dif = "Now let's chose a difficulty. "
    game = ""
    print(choose_game)
    game_choice = check_input(3)
    print(choose_dif)
    difficulty = check_input(5)
    GameSettings.game_difficulty = difficulty
    if game_choice == 1:
        game = "Memory Game"
    elif game_choice == 2:
        game = "Guess Game"
    else:
        game = "Currency Roulette"
    print(f"The difficulty level you chose for {game} is: {difficulty}\n")

    if game == "Memory Game":
        play_memory(difficulty)
    elif game == "Guess Game":
        play_guess(difficulty)
    elif game == "Currency Roulette":
        play_roulette(difficulty)
