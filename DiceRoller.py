import random

class Die(object):
    def __init__(self, sides=6):
        self.sides = sides
def roll(self):
    self.roll_count = random.randint(1, self.sides)

def get(self):
    return self.roll_count           


print('How many dice are you rolling?')
dicenum = input()
print('What sided die are you rolling (ex. d6, d8)')
diceside = input()

print(f'You want to roll a {int(dicenum)}d{int(diceside)}')

#def rolldice(dicenum, diceside):