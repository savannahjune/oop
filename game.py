import core
import pyglet
from pyglet.window import key
from core import GameElement
import sys

#### DO NOT TOUCH ####
GAME_BOARD = None
DEBUG = False
######################

GAME_WIDTH = 10
GAME_HEIGHT = 10

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

        

            # GAME_BOARD.set_el(4, 5, popo)
        # checks if there is a solid object in the next direction, if there's nothing or
        # it isn't solid, let the character move, if not keep it where it is

        if direction:
            #set next_location to detect next position
            next_location = self.next_pos(direction)

            # checking if player within boundaries and setting to original position if not
            if next_location[0] > 9 or next_location[0] < 0 or next_location[1] > 9 or next_location[1] < 0:
                self.board.draw_msg("You fucked up! Go back to the beginning.")
                self.board.del_el(self.x, self.y)
                self.board.set_el(0, 9, self)

            # if Popo.VISIBLE == False and next_location[0] > 2 or next_location[1] < 7:
            #     # GAME_BOARD.set_el(4, 5, Popo)
            #     print "Hello"
            
            if next_location[0] > 2 or next_location[1] < 7:
                GAME_BOARD.set_el(4, 5, Popo)
                print "Hello"
            #checking if something in next tile, if so, draw_msg, if not, move player into next position
            else:
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

class Iphone(Gem):
    IMAGE = "Iphone"

    def interact(self, player):
        # player.inventory.append(self)
        GAME_BOARD.draw_msg("You just a gold iPhone 6 Plus! Oooo it looks so nice and delicate. This is worth a lot in the clink.")

class Popo(GameElement):
    IMAGE = "Popo"
    VISIBLE = False

    direction = 1

    # def interact(self, player):
    #     if player is 


    def update(self, dt):

        next_x = self.x + self.direction

        if next_x < 0 or next_x >= self.board.width:
            self.direction *= -1
            next_x = self.x

        self.board.del_el(self.x, self.y)
        self.board.set_el(next_x, self.y, self)

    # def interact(self, player):
class Sealwhale(GameElement):
    IMAGE = "Sealwhale"
        


####   End class definitions    ####

def initialize():  # this is where we put the instance attributes aka regular attributes
    """Put game initialization code here"""
    rock_positions = [
            (2, 1),
            # (1, 2),
            # (3, 2),
            # (2, 3),
            # (1, 1),
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
    GAME_BOARD.set_el(0, 9, player)
    print player

    popo = Popo()
    GAME_BOARD.register(popo)
 

    sealwhale = Sealwhale()
    GAME_BOARD.register(sealwhale)
    GAME_BOARD.set_el(3, 2, sealwhale)

    iphone = Iphone()
    GAME_BOARD.register(iphone)
    GAME_BOARD.set_el(2, 9, iphone)
    
    # gem = Gem()
    # GAME_BOARD.register(gem)
    # GAME_BOARD.set_el(3, 1, gem)

    # greengem = Greengem()
    # GAME_BOARD.register(greengem)
    # GAME_BOARD.set_el(3, 3, greengem)

    GAME_BOARD.draw_msg("Welcome to Escape to Alcatraz. Begin by gathering contraband to take to your buddy in jail.")




    # pass


