import core
import pyglet
from pyglet.window import key
from core import GameElement
import sys

#### DO NOT TOUCH ####
GAME_BOARD = None
DEBUG = False
######################

GAME_WIDTH = 5
GAME_HEIGHT = 5

#### Put class definitions here ####
class Rock(GameElement):            # always has these CLASS attributes in the beginning
    IMAGE = "Rock"
pass
####   End class definitions    ####

def initialize():  # this is where we put the instance attributes aka regular attributes
    """Put game initialization code here"""
    # Initialize and register rock 1
    rock1 = Rock()
    GAME_BOARD.register(rock1)
    GAME_BOARD.set_el(1, 1, rock1)
    # Initialize and register rock 2
    rock2 = Rock()
    GAME_BOARD.register(rock2)      # creates the rock
    GAME_BOARD.set_el(2, 2, rock2)  # puts the rock at a coordinate

    rock3 = Rock()
    GAME_BOARD.register(rock3)
    GAME_BOARD.set_el(3, 3, rock3)


    print "The first rock is at", (rock1.x, rock1.y)
    print "The second rock is at", (rock2.x, rock2.y)
    print "The third rock is at", (rock3.x, rock3.y)
    print "Rock 1 image", rock1.IMAGE
    print "Rock 2 image", rock2.IMAGE
    print "Rock 3 image", rock3.IMAGE
    pass
