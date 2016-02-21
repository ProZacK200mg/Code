import textwrap
from player import *


class Game:
    def show_start_screen(self):
        #Game splash/start screen
        print ("Welcome to Zombie: The Survival Game!\n\n\n\n\n")
        print ("""Your girl friend wants to go out.
She has always wanted to go out on a picnic.
You planned for weeks to go on this trip.
Your plan was to go to a old farm that you have know about since you where a kid.
Its a beautiful place with a big field you and her can have all to your selfs.
The farm has been abandoned for some time now and the house is just about to fall over.
The old house is just west of this feild.
There is a huge tree that would be a perfect spot for your picnic, and the best place you can think of, to ask your girl friend of 5 year to be your wife!
Best part is it is just over in the next town.

So you load up your truck with everything you think you might need.
You have of course you truck and full tank of gas.
You have all the stuff for the picnic, plus all your camping gear.
Which includes:
    Tent
    Sleeping bags
    Rope
    Axe
    Pocket Knife
    Lighter
    Cash - (just in case you need a hotel)
    Finally you have your cell phone.

You pick her up on at about 12 o'clock, Saturday afternoon.
Y'all drive the hour it takes to get to the next town.
Y'all have an amazing picnic and decide to stay the night.\n\n\n\n""")

        self.new_game()

    def new_game(self):
        self.player = Player()
        self.player.name = input("What is your name?")


        print ("""You awake to your girl friend gone!
There is a Orange haze in the air!
You see your truck parked next to the abandoned house.
All your gear is packed up in your back pack.
Tent is still up.
The house is off to your east
You also hear sirens off in the distance toward town.""")

    def show_go_screen(self):
        #Game over/continue
        pass

g = Game()
g.show_start_screen()
