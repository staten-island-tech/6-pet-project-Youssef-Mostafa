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
        self.age += 0.25
        print (f"{Khaby_Lame_Mechanism.name} turns his hands with excitement. You throw him a ball and he runs to get it, getting himself a little dirty.")

    def feed(self, hunger):
        self.hunger += random.randint(1,6)
        self.hygiene -= random.randint(1,6)
        self.happiness += random.randint(1,2)
        self.age += 0.25
        print (f"{Khaby_Lame_Mechanism.name} speeds up his hands with to shovel food in his mouth. Your mechanism is enjoying the food, but he is a very messy eater.")

    def drink(self, thirst):
        self.thirst += random.randint(1,6)
        self.hunger -= random.randint(1,2)
        self.happiness += random.randint(1,2)
        self.age += 0.25
        print (f"{Khaby_Lame_Mechanism.name} uses his hands to quickly scoop and drink up the water in his bowl. He must have been really parched. He enjoyed the water you gave him.")

    def bathe(self, hygiene):
        self.hygiene += random.randint(1,6)
        self.happiness -= random.randint(1,3)
        self.age += 0.25
        print (f"{Khaby_Lame_Mechanism.name} jumps into the bath, turning his hands to stay above water. However, your mechanism hates baths and isn't very happy with you.")

    def rest(self, sleep):
        self.sleep += random.randint(1,6)
        self.happiness += random.randint(1,2)
        self.hunger -= random.randint(1,3)
        self.thirst -= random.randint(1,3)
        self.age += 0.25
        print (f"{Khaby_Lame_Mechanism.name} rests his weary hands and heads to sleep. He snores through the night, happily dreaming of food.")

Khaby_Lame_Mechanism = Pet("Khaby_Lame_Mechanism", 50, 50, 50, 50, 50, 0)
Khaby_Lame_Mechanism.name = input("You found a mechanism is a cardboard box and decide to take it home with you. What would you like to name your beautiful mechanism?")

options = [{
    "Play"},
    {"Feed"},
    {"Drink"},
    {"Bathe"},
    {"Rest"}]
pet_state = "Not Dead"
while pet_state == "Not Dead":
    for index, item in enumerate(options, start = 1):
        print(index, ":", item)
    print(f"{len(options) + 1 } : View Mechanism Stats")
    choice = input(f"What would you like to do with {Khaby_Lame_Mechanism.name}? Or would you like to view {Khaby_Lame_Mechanism.name}'s stats?")
    if not choice.isdigit():
        print("Please choose a valid choice with numbers that are displayed, or else!")
    else:
        choice = int(choice)
        if choice == 1:
            Khaby_Lame_Mechanism.play(1)
        elif choice == 2:
            Khaby_Lame_Mechanism.feed(1)
        elif choice == 3:
            Khaby_Lame_Mechanism.drink(1)
        elif choice == 4:
            Khaby_Lame_Mechanism.bathe(1)
        elif choice == 5:
            Khaby_Lame_Mechanism.rest(1)
        elif choice == len(options) + 1:
            choice = int(choice)
            print(Khaby_Lame_Mechanism.__dict__)
        else:
            print("Please choose a valid choice with numbers that are displayed, or else!")
    
    end_day_options = [{
    "Quit"},
    {"Rest"}]

    for index, item in enumerate(options, start = 1):
        print(index, ":", item)
    print(f"{len(options) + 1 } : View Mechanism Stats")
    choice = input(f"What would you like to do right now? Do you want to quit, rest to continue to the next day, or check {Khaby_Lame_Mechanism.name}'s stats?")
    if not choice.isdigit():
        print("Please choose a valid choice with numbers that are displayed, or else!")
    

    
    if Khaby_Lame_Mechanism.age == 1:
        print("The day is over and you are very tired now. Head to bed to start the next day.")
    else:
        choice = int(choice)
        if choice == 1:
            quit()
        elif choice == 2:
            print("It is now the next day.")
        elif choice == len(options) + 1:
            choice = int(choice)
            print(Khaby_Lame_Mechanism.__dict__)
        else:
            print("Please choose a valid choice with numbers that are displayed, or else!")

    if Khaby_Lame_Mechanism.happiness <= 0:
        print(f"{Khaby_Lame_Mechanism.name} died of boredom and loneliness because you didn't feel like playing with it. GAME OVER")
        quit()
    elif Khaby_Lame_Mechanism.hunger <= 0:
        print(f"{Khaby_Lame_Mechanism.name} died of hunger because you didn't want to hop off the game and feed your pet. GAME OVER")
        quit()
    elif Khaby_Lame_Mechanism.thirst <= 0:
        print(f"{Khaby_Lame_Mechanism.name} died of thirst because you were too lazy scrolling on TikTok to do a simple task. GAME OVER")
        quit()
    elif Khaby_Lame_Mechanism.hygiene <= 0:
        print(f"{Khaby_Lame_Mechanism.name} died of diseases because you lack basic hygiene and didn't feel like bathing your mechanism. GAME OVER")
        quit()
    elif Khaby_Lame_Mechanism.sleep <= 0:
        print(f"{Khaby_Lame_Mechanism.name} died of insomnia and sleep deprivation because you would tuck it in at bedtime. Your mechanism couldn't sleep because you weren't there! GAME OVER")
        quit()

