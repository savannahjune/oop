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

class Character(GameElement):
    IMAGE = "Girl"

class Boy(GameElement):
    IMAGE = "Boy"

class Cat(GameElement):
    IMAGE = "Cat"

class Princess(GameElement):
    IMAGE = "Princess"

class Horns(GameElement):
    IMAGE = "Horns"
####   End class definitions    ####

def initialize():  # this is where we put the instance attributes aka regular attributes
    """Put game initialization code here"""
    rock_positions = [
            (2, 1),
            (1, 2),
            (3, 2),
            (2, 3),
            (1, 1),
        ]

    rocks = []

    for pos in rock_positions:
        rock = Rock()
        GAME_BOARD.register(rock)
        GAME_BOARD.set_el(pos[0], pos[1], rock)
        rocks.append(rock)

    for rock in rocks:
        print rock
    
    #register and instantiate PC girl
    player = Character()
    GAME_BOARD.register(player)
    GAME_BOARD.set_el(2, 0, player)
    print player

    boy = Boy()
    GAME_BOARD.register(boy)
    GAME_BOARD.set_el(3, 0, boy)
    print boy

    cat = Cat()
    GAME_BOARD.register(cat)
    GAME_BOARD.set_el(1, 0, cat)
    print cat

    princess = Princess()
    GAME_BOARD.register(princess)
    GAME_BOARD.set_el(1, 3, princess)
    print princess

    horns = Horns()
    GAME_BOARD.register(horns)
    GAME_BOARD.set_el(3, 1, horns)
    print horns


    pass


