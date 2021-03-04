"""
Snake game : Player maneuvers a snake which grows in lenght as it eats a rat
"""
from random import randrange

#Constants
BOARD_LENGTH = 100
BOARD_HEIGHT = 10

class Snake:
    def __init__(self):
        self.tail_len = 1

class Rat:
    def __init__(self):
        self.x = None
        self.y = None

    def spawn(self):
        'Assign a place for the rat to spawn'
        randrange()

class Game():
    """Class manages game mechanics"""
    def __init__(self):
        # Initialise component objects
        players_snake = Snake
        subjects_rat = Rat
        self.draw_board()

    def draw_board(self):
        print("*"*BOARD_LENGTH)
        print("\n"*BOARD_HEIGHT)
        print("*" * BOARD_LENGTH)

if __name__ == '__main__':
    mygame = Game()
    player_input = None
    while(1):
        if player_input != 'x':
            player_input = str(input())
            print(player_input)
        else :
            print("Game is exiting now")
            break
