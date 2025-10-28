#Examples

""" class Hero:
    def __init__(self, name, money, inventory):
        self.name = name
        self.money = money
        self.inventory = inventory

    def buy(self, item):
        self.inventory.append(item)
Khaby_Lame_Mechanism = Hero("Khaby_Lame_Mechanism", 500, ["Hands of Fate"])

print(Khaby_Lame_Mechanism.__dict__)

Khaby_Lame_Mechanism.buy({"item": "Upraded Hands of Time", "attack": 61})   
print(Khaby_Lame_Mechanism.__dict__)
 """
#Personal Pet Project

import random


class Pet:
    def __init__ (self, name, happiness):
        self.name = name
        self.happiness = happiness

    def play(self, happiness):
        self.happiness += random.randint(1,6)
        print (f"Khaby Lame Mechanism turns his hands with excitement. Happiness increased by {self.happiness}.")
Khaby_Lame_Mechanism = Pet("Khaby_Lame_Mechanism", 0)
Khaby_Lame_Mechanism.play(1)
print(Khaby_Lame_Mechanism.__dict__)