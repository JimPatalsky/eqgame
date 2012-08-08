import hero
import world
import random
import monster

class EqGame:
    def __init__(self, theHero, theWorld):
        self.valid_cmds = ['w', 'i', 'j', 'c', 'm', 'q', 's']
        self.cmd = 'z'
        self.hero = theHero;
        self.world = theWorld;

    def main_loop(self):
        while self.cmd != 'q':
            self.get_command()
            self.follow_command()

    def print_main(self):
        print "What would you like to do?"
        print "(W)alk to next tile"
        print "Look at your (i)nvintory"
        print "Look at your (j)ournal"
        print "Interact with the (c)urrent tile"
        print "Look at your (s)tats"
        print "(Q)uit"

    def get_command(self):
        print "What would you like to do?"
        print "Press (m) for the main menu options."
        cmd = raw_input('--> ')
        self.cmd = self.parse_command(cmd)

    def parse_command(self, cmd):
        # Returns a lower case command or None if cmd
        # is not part of valid_cmds
        if len(cmd) != 1:
            return 'z'
        else:
            cmd = cmd.lower();
            if cmd in self.valid_cmds:
                return cmd
            else:
                return 'z'

    def follow_command(self):     
        if self.cmd == 'w':
            # Walk
            self.walk()
        elif self.cmd == 'i':
            # Inventory
            self.hero.print_inventory()
        elif self.cmd == 'j':
            # Journal
            print 'Your journal is blank!'
        elif self.cmd == 'c':
            # Current tile actions
            print 'Your on a boring tile and have nothing to do!'
        elif self.cmd == 'm':
            # Print main
            self.print_main();
        elif self.cmd == 's':
            # Stats
            self.hero.print_stats();
        elif self.cmd == 'q':
            # Quit
            print 'Thanks for playing!'
            print 'Goodbye'
        elif self.cmd == 'z':
            # Invalid
            print 'That is not a valid command!'
        else:
            # Something is wrong
            if self.cmd in self.valid_cmds:
                print 'ERROR: Missed a command!'

    def walk(self):
        print 'Do you want to go (u)p, (d)own, (l)eft, or (r)ight?'
        cmd = raw_input('--> ')
        cmd = cmd[0].lower() # Take just the first
        if self.is_valid_dir(cmd):
            # Move the player
            self.hero.move(self.get_dir_value(cmd))
            # Check if in city
            if self.world.is_city(self.hero.loc):
                # In a city, check which one
                print 'You are now in', self.world.get_city_name(self.hero.loc)
            else:
                # Check if you are attacked
                if self.world.is_attacked(self.hero.loc):
                    # Attacked
                    print 'You are being attacked!'
                    self.fight()
                else:
                    # Not attacked
                    print 'You arrive in another boring area'
        else:
            print 'That is not a valid direction!'
        
    def fight(self):
        # Creates a fight and figures out the outcome
        # Uses self.hero and self.world

        # Generate a monster
        rand_int = random.randint(0,1)
        if rand_int == 0:
            # A rat
            enemy = monster.Monster(1);
        elif rand_int == 1:
            # A wolf
            enemy = monster.Monster(2);
        else:
            # Soemthing went wrong
            print 'You are fighting yourself!?...?!'

        while ((not self.hero.is_dead()) and (not enemy.is_dead())):
            # While both are alive we fight
            # Lets give the hero the first hit
            enemy.defend(self.hero.attack());
            if enemy.is_dead():
                break

            # Now it is the enemy's turn
            self.hero.defend(enemy.attack());

        # Out of while loop, so something died
        if enemy.is_dead():
            print 'The hero is victorious!'
        else:
            print 'The hero has suffered a fatal blow and has died!'
            print 'GAME OVER'
            self.quit_loop()

    def quit_loop(self):
        self.cmd = 'q'

    def is_valid_dir(self, cmd):
        valid_dirs = ['u', 'd', 'l', 'r']
        
        if cmd in valid_dirs:
            return True
        else:
            return False

    def get_dir_value(self, cmd):
        if cmd == 'u':
            return [0, 1]
        elif cmd == 'd':
            return [0, -1]
        elif cmd == 'l':
            return [-1, 0]
        elif cmd == 'r':
            return [1, 0]
        else:
            return [0,0]

########### START OF MAIN FUNCTION #############
theHero = hero.Hero()
theWorld = world.World()
theGame = EqGame(theHero, theWorld)

theGame.main_loop()
