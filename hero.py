import character
class Hero(character.Character):
    def __init__(self):
        character.Character.__init__(self)
        self.hp = 25
        self.atk_pwr = 5
        self.armor = 3
        self.inv_limit = 10;
        self.loc = [0, 0]

    def receive_item(self, item_str):
        if len(inventory) < self.inv_limit:
            # Okay, can get the item
            self.inventory.append(item_str)
            return True
        else:
            # Too many items
            print 'You are carrying too much!'
            print 'You had to throw away the', item_str
            return False

    def move(self, direction):
        if len(direction) != 2:
            # Do nothing but let calling function know
            return False
        # Right now, direction will be a tuple with 0, 1, or -1
        self.loc[0] += direction[0]
        self.loc[1] += direction[1]
        update_str = self.get_update_str()
        print update_str
        return True

    def get_update_str(self):
        update_str = 'You are currently '
        if self.loc[0] >= 0:
            update_str += str(self.loc[0])
            update_str += ' leauges east and '
        else:
            update_str += str(abs(self.loc[0]))
            update_str += ' leagues west and '

        if self.loc[1] >= 0:
            update_str += str(self.loc[1])
            update_str += ' leagues north of camp.'
        else:
            update_str += str(abs(self.loc[1]))
            update_str += ' leagues east of camp.'
        return update_str

    def print_stats(self):
        print 'HP:', self.hp
        print 'Armor:', self.armor
        print 'Attack power:', self.atk_pwr
        print 'Location:', self.loc
        self.print_inventory()

    def print_inventory(self):
        if len(self.inventory) == 0:
            print 'Your inventory is empty'
        else:
            print 'Inventory:', self.inventory
