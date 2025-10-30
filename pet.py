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
    def __init__ (self, name, happiness, hunger, thirst, hygiene, sleep):
        self.name = name
        self.happiness = happiness
        self.hunger = hunger
        self.thirst = thirst
        self.hygiene = hygiene
        self.sleep = sleep

    def play(self, happiness):
        self.happiness += random.randint(1,6)
        self.hunger -= random.randint(1,6)
        self.thirst -= random.randint(1,6)
        self.hygiene -= random.randint(1,6)
        self.sleep -= random.randint(1,6)
        print (f"Khaby Lame Mechanism turns his hands with excitement. Happiness increased by {self.happiness - 15}. Hygiene, thirst, hunger, and sleep also decreased.")

    def feed(self, hunger):
        self.hunger += random.randint(1,6)
        self.hygiene -= random.randint(1,6)
        self.happiness += random.randint(1,2)
        print (f"Khaby Lame Mechanism speeds up his hands with to shovel food in his mouth. Hunger increased by {self.hunger - 15}. Hygiene decreased and happiness increased slightly.")

    def drink(self, thirst):
        self.thirst += random.randint(1,6)
        self.hunger -= random.randint(1,2)
        self.happiness += random.randint(1,2)
        print (f"Khaby Lame Mechanism uses his hands to quickly scoop and drink up the water in his bowl. Thirst increased by {self.thirst - 15}. Hunger decreased and ")


Khaby_Lame_Mechanism = Pet("Khaby_Lame_Mechanism", 15, 15, 15, 15, 15)
Khaby_Lame_Mechanism.play(1)
print(Khaby_Lame_Mechanism.__dict__)