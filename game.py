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
    SOLID = True

class Character(GameElement):
    IMAGE = "Girl"

    def __init__(self):
        GameElement.__init__(self)
        self.inventory = []

    def next_pos(self, direction):
        if direction == "up":
            return (self.x, self.y-1)
        elif direction == "down":
            return (self.x, self.y+1)
        elif direction == "left":
            return (self.x-1, self.y)
        elif direction == "right":
            return (self.x+1, self.y)
        return None

    def keyboard_handler(self, symbol, modifier):

        #Take key presses from character and move character
        direction = None
        if symbol == key.UP:
            direction = "up"
        elif symbol == key.DOWN:
            direction = "down"
        elif symbol == key.LEFT:
            direction = "left"
        elif symbol == key.RIGHT:
            direction = "right"
        # elif symbol == key.SPACE:
        #     self.board.erase_msg()

        # draw message on screen indicating direction
        self.board.draw_msg("[%s] moves %s" % (self.IMAGE, direction))

        # checks if there is a solid object in the next direction, if there's nothing or
        # it isn't solid, let the character move, if not keep it where it is
        if direction:
            next_location = self.next_pos(direction)

            if next_location:
                next_x = next_location[0]
                next_y = next_location[1]
                
                existing_el = self.board.get_el(next_x, next_y) 

                if existing_el:
                    existing_el.interact(self)

                if existing_el and existing_el.SOLID:
                    self.board.draw_msg("There's something in my way!")
                elif existing_el is None or not existing_el.SOLID:
                    self.board.del_el(self.x, self.y)
                    self.board.set_el(next_x, next_y, self)


        

class Boy(GameElement):
    IMAGE = "Boy"

class Cat(GameElement):
    IMAGE = "Cat"

class Princess(GameElement):
    IMAGE = "Princess"

class Horns(GameElement):
    IMAGE = "Horns"

class Gem(GameElement):
    IMAGE = "BlueGem"
    SOLID = False

    def interact(self, player):
        player.inventory.append(self)
        GAME_BOARD.draw_msg("You just acquired a gem! You have %d items" % (len(player.inventory)))

class Greengem(Gem):
    IMAGE  = "GreenGem"

    def interact(self, player):
        player.inventory.append(self)
        GAME_BOARD.draw_msg("You just acquired a green, organic, local certified gem! You have %d items" % (len(player.inventory)))

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

    rocks[-1].SOLID = False

    for rock in rocks:
        print rock
    
    #register and instantiate PC girl
    player = Character()
    GAME_BOARD.register(player)
    GAME_BOARD.set_el(0, 0, player)
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

    gem = Gem()
    GAME_BOARD.register(gem)
    GAME_BOARD.set_el(3, 1, gem)

    greengem = Greengem()
    GAME_BOARD.register(greengem)
    GAME_BOARD.set_el(3, 3, greengem)

    GAME_BOARD.draw_msg("This game is wicked awesome.")




    # pass


