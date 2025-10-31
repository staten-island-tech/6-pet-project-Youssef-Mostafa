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
    def __init__ (self, name, happiness, hunger, thirst, hygiene, sleep, age):
        self.name = name
        self.happiness = happiness
        self.hunger = hunger
        self.thirst = thirst
        self.hygiene = hygiene
        self.sleep = sleep
        self.age = age

    def play(self, happiness):
        self.happiness += random.randint(1,6)
        self.hunger -= random.randint(1,6)
        self.thirst -= random.randint(1,6)
        self.hygiene -= random.randint(1,6)
        self.sleep -= random.randint(1,6)
        print (f"Khaby Lame Mechanism turns his hands with excitement. Happiness increased by {self.happiness - 50}. Hygiene, thirst, hunger, and sleep also decreased.")

    def feed(self, hunger):
        self.hunger += random.randint(1,6)
        self.hygiene -= random.randint(1,6)
        self.happiness += random.randint(1,2)
        print (f"Khaby Lame Mechanism speeds up his hands with to shovel food in his mouth. Hunger increased by {self.hunger - 50}. Hygiene decreased and happiness increased slightly.")

    def drink(self, thirst):
        self.thirst += random.randint(1,6)
        self.hunger -= random.randint(1,2)
        self.happiness += random.randint(1,2)
        print (f"Khaby Lame Mechanism uses his hands to quickly scoop and drink up the water in his bowl. Thirst increased by {self.thirst - 50}. Hunger decreased and ")

    def bathe(self, hygiene):
        self.hygiene += random.randint(1,6)
        self.happiness -= random.randint(1,3)
        print (f"Khaby Lame Mechanism jumps into the bath, turning his hands to stay above water. Hygiene increased by {self.hygiene - 50}.")

    def rest(self, sleep):
        self.sleep += random.randint(1,6)
        self.happiness += random.randint(1,2)
        self.hunger -= random.randint(1,3)
        self.thirst -= random.randint(1,3)
        print (f"Khaby Lame Mechanism rests his weary hands and heads to sleep. Sleep increased by {self.sleep - 50}.")




Khaby_Lame_Mechanism = Pet("Khaby_Lame_Mechanism", 50, 50, 50, 50, 50, 0)

choice = input("What would you like to do with your mechanism? 1) Play. 2) Feed. 3) Drink. 4) Bathe. 5) Rest.")
if choice == "play" or choice == "1":
    Khaby_Lame_Mechanism.play(1)
if choice == "feed" or choice == "2":
    Khaby_Lame_Mechanism.feed(1)
if choice == "drink" or choice == "3":
    Khaby_Lame_Mechanism.drink(1)
if choice == "bathe" or choice == "4":
    Khaby_Lame_Mechanism.bathe(1)
if choice == "rest" or choice == "5":
    Khaby_Lame_Mechanism.rest(1)
else:
    print("Please pick a valid choice, or else.")

print(Khaby_Lame_Mechanism.__dict__)