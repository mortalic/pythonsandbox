# game.py
# import the draw module
from draw import draw_game
# also valid, imports all objects from a module.
#from draw import *

def play_game():
    ...

def main():
    result = play_game()
    draw_game(result)

# this means that if this script is executed, then 
# main() will be executed
if __name__ == '__main__':
    main()