from Live import welcome
from Live import load_game

welcome()
game = load_game()

from GuessGame import play_guess
from MemoryGame import play_memory
from CurrencyRouletteGame import play_roulette


if game == 1:
    play_memory()
elif game == 2:
    play_guess()
elif game == 3:
    play_roulette()

#
