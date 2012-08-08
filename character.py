class Character:
    def __init__(self):
        # The basic init for all characters should
        # be called from each child class, but will
        # be over written by new values
        self.name = 'character'
        self.hp = 1
        self.armor = 1
        self.atk_pwr = 1
        self.inventory = []; # holds loot
        self.inv_limit = 1;

    def is_dead(self):
        if self.hp <= 0:
            return True
        else:
            return False

    def attack(self):
        # Used to attack other characters
        # Returns the atkpwr of this character
        return self.atk_pwr

    def defend(self, atk_pwr):
        # Used to defend against other attacks
        # Calculates damage based on atkpwr of
        # attacker and armor of self
        damage = atk_pwr - self.armor
        if damage > 0:
            self.hp -= damage
            print self.name, 'was hit for', damage, 'damage!'
        else:
            print self.name, 'blocked the attack completely!'
