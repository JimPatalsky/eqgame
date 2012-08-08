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
