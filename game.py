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

    def interact(self, player):
        print 'getting inventory on rock bump %s' % (player.inventory)
        if len(player.inventory) != 0:
            GAME_BOARD.draw_msg("You hit the rock!!! You bent your precious iPhone (6 Plus, Gold).")

class Character(GameElement):
    IMAGE = "Girl"


    def __init__(self):
        GameElement.__init__(self)
        self.inventory = []
        self.popoexists = False

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
        self.board.draw_msg("%s moves %s" % (self.IMAGE, direction))

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
            
            #checking if something in next tile, if so, draw_msg, if not, move player into next position
            else:
                next_x = next_location[0]
                next_y = next_location[1]
                
                if (next_x > 2 or next_y < 7) and self.popoexists == False:
                    popo = Popo()
                    GAME_BOARD.register(popo)
                    GAME_BOARD.set_el(4, 5, popo)
                    self.popoexists = True

                # use coordinates to get object if it's in next location            
                existing_el = self.board.get_el(next_x, next_y) 

                # if there is something in next location, call interact for that object
                if existing_el:
                    existing_el.interact(self)
                
                # this checks if you are allowed to move there, can't if the object is solid
                if existing_el and existing_el.SOLID and not Rock:
                    self.board.draw_msg("There's something in my way!")
                elif existing_el is None or not existing_el.SOLID:
                    self.board.del_el(self.x, self.y)
                    self.board.set_el(next_x, next_y, self)

        def interact(self, GameElement):
            GameElement.playerinteract(self)
            

class Popo(GameElement):
    IMAGE = "Popo"
    VISIBLE = False

    direction = 1


    def update(self, dt):

        next_x = self.x + self.direction

        if next_x < 0 or next_x >= self.board.width:
            self.direction *= -1
            next_x = self.x

        self.board.del_el(self.x, self.y)
        self.board.set_el(next_x, self.y, self)

    def playerinteract(self, player):
        pass


class Sealwhale(GameElement):
    IMAGE = "Sealwhale"

class Alcatraz(GameElement):
    IMAGE = "Alcatraz"
    SOLID = True

class Cage(GameElement):
    IMAGE = "Cage Happy"
    SOLID = True

# Abstract Class Item (Our first abstract WOOO WOOO)

class Item(GameElement):
    SOLID = False

    def interact(self, player, message):
        player.inventory.append(self)
        GAME_BOARD.draw_msg("%s. You have %d items" % (message, len(player.inventory)))

class Iphone(Item):
    IMAGE = "Iphone"
    message = "You just stole a gold iPhone 6 Plus! Oooo, it looks so nice and delicate. This is worth a lot in the clink."
    

    def interact(self, player):
        return super(Iphone, self).interact(player, self.message)



    # def interact(self, player):
    #     player.inventory.append(self)
    #     print "inventory on iphone bump: %s" % player.inventory
    #     GAME_BOARD.draw_msg("You just stole a gold iPhone 6 Plus! Oooo, it looks so nice and delicate. This is worth a lot in the clink.")

class Weed(Item):
    IMAGE = "Weed"

    def interact(self, player):
        player.inventory.append(self)
        print "inventory on weed bump: %s" % player.inventory
        GAME_BOARD.draw_msg("You just got some medicinal weed from your doctor!! This will help your buddy in jail with his 'glaucoma'.")

class Blade(Item):
    IMAGE = "Blade"

    def interact(self, player):
        player.inventory.append(self)
        print "inventory on blade bump: %s" % player.inventory
        GAME_BOARD.draw_msg("You just bought a super sharp blade for your buddy. This will keep him safe, and on top of the prison hiearchy.")

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

    # rocks[-1].SOLID = True
    # rocks[0].SOLID = True

    for rock in rocks:
        print rock
    
    #register and instantiate PC girl
    player = Character()
    GAME_BOARD.register(player)
    GAME_BOARD.set_el(0, 9, player)
    print player

    sealwhale = Sealwhale()
    GAME_BOARD.register(sealwhale)
    GAME_BOARD.set_el(3, 2, sealwhale)

    iphone = Iphone()
    GAME_BOARD.register(iphone)
    GAME_BOARD.set_el(2, 9, iphone)

    alcatraz = Alcatraz()
    GAME_BOARD.register(alcatraz)
    GAME_BOARD.set_el(9, 0, alcatraz)

    cage = Cage()
    GAME_BOARD.register(cage)
    GAME_BOARD.set_el(9, 1, cage)

    weed = Weed()
    GAME_BOARD.register(weed)
    GAME_BOARD.set_el(2, 7, weed)

    blade = Blade()
    GAME_BOARD.register(blade)
    GAME_BOARD.set_el(0, 7, blade)
    
    # item = Item()
    # GAME_BOARD.register(item)
    # GAME_BOARD.set_el(3, 1, item)



    GAME_BOARD.draw_msg("Welcome to Escape to Alcatraz. Begin by gathering contraband to take to your buddy in jail.")




    # pass

