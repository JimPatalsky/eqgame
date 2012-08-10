import random
class World:
    def __init__(self):
        self.cities = {(0,0):'Camp', (2,3):'Town'}

    def convert_loc(self, loc_in):
        return (loc_in[0], loc_in[1]);

    def is_city(self, loc_in):
        loc = self.convert_loc(loc_in)
        if loc in self.cities.keys():
            return True
        else:
            return False

    def get_city_name(self, loc_in):
        loc = self.convert_loc(loc_in)
        return self.cities[loc]
        
    def is_attacked(self, loc_in):
        loc = self.convert_loc(loc_in)
        # Eventually check the chance of being attacked
        # given a particular spot and by what
        if random.randint(0,1) == 1:
            return True
        else:
            return False

    def city_action(self, loc_in):
        loc = self.convert_loc(loc_in)
        # Check which city we are in, prompt the user about
        # the city actions, and carry that action out
        self.print_city_action(loc_in)
        self.execute_city_action(loc_in)

    def print_city_action(self, loc_in):
        # Call the convert_loc function every time even though
        # it has probably already been converted from city_action
        loc = self.convert_loc(loc_in)
        if loc == (0,0):
            # At camp
            print 'What would you like to do in your camp?'
            print '(R)est next to the camp fire.'
            print 'Go to (s)leep.'
            print '(N)othing.'
        elif loc == (2,3):
            # In town
            print 'What would you like to do in town?'
            print 'Go to the (s)tore.'
            print 'Check out the town (f)ountain.'
            print 'Ask around for (r)umors.'
            print '(N)othing.'
        else:
            print 'You are not sure what you can do here.'

    def execute_city_action(self, loc_in):
        loc = self.convert_loc(loc_in)
        cmd = raw_input('--> ')
        cmd = cmd.lower()
        if loc == (0,0):
            if cmd == 'r':
                # Rest
                print 'You take a break.'
                # Add ability to heal 1 HP
            elif cmd == 's':
                # Sleep
                print 'You go to sleep...and snore a lot!'
                # Add ability to heal 100% HP
            elif cmd == 'n':
                # Do nothing
                print 'You do nothing and go on your way.'
            else:
                # Invalid command
                print 'Sorry, that was not an option.'
        elif loc == (2,3):
            if cmd == 's':
                # Store
                print 'Seems like the store is closed today.'
                # Add ability to sell items and buy items
            elif cmd == 'f':
                # Fountain - to progress story line
                print 'You take a walk down to the fountain.'
                print 'The townspeople all seem to enjoy this area.'
            elif cmd == 'r':
                # Rumors - to get quests for exp and items
                print 'You do not know anyone here to talk with yet.'
            elif cmd == 'n':
                print 'You do nothing and go on your way.'
            else:
                print 'Sorry, that was not an option.'
        else:
            # Something went wrong
            print 'You are not able to do anything in this location.'
