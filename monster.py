import character
class Monster(character.Character):
    def __init__(self, enemy_flag):
        character.Character.__init__(self)
        if enemy_flag == 1:
            self.make_rat()
        elif enemy_flag == 2:
            self.make_wolf()
        else:
            # Right now there should only be 1 and 2
            # So something went wrong
            print 'Error with enemy_flag'

    def make_rat(self):
        self.name = 'Rat'
        self.hp = 3
        self.atk_pwr = 2
        self.armor = 1
        self.inventory.append('rat fur')

    def make_wolf(self):
        self.name = 'Wolf'
        self.hp = 10
        self.atk_pwr = 5
        self.armor = 2
        self.inventory.append('wolf fur')
