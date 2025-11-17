# Examples

""" class Hero:
    def __init__(self, name, money, inventory):
        self.name = name
        self.money = money
        self.inventory = inventory

    def buy(self, item):
        self.inventory.append(item)
Khaby_Lame_Mechanism = Hero("Khaby_Lame_Mechanism", 500, ["Hands of Fate"])

print(Khaby_Lame_Mechanism.__dict__)

Khaby_Lame_Mechanism.buy({"item": "Upgraded Hands of Time", "attack": 61})   
print(Khaby_Lame_Mechanism.__dict__)
 """


# Personal Pet Project

import random



class Pet:
    def __init__ (self, name, happiness, hunger, thirst, hygiene, sleep, age, money):
        self.name = name
        self.happiness = happiness
        self.hunger = hunger
        self.thirst = thirst
        self.hygiene = hygiene
        self.sleep = sleep
        self.age = age
        self.money = money

    def play(self):
        self.happiness += random.randint(1,10)
        self.hunger -= random.randint(1,6)
        self.thirst -= random.randint(1,6)
        self.hygiene -= random.randint(1,6)
        self.sleep -= random.randint(1,6)
        self.age += 0.25
        print (f"{Khaby_Lame_Mechanism.name} turns his hands with excitement. You throw him a ball and he runs to get it, getting himself a little dirty. Age advanced by 1/4 of a day.")

    def feed(self):
        self.hunger += random.randint(1,10)
        self.hygiene -= random.randint(1,6)
        self.happiness += random.randint(1,2)
        self.age += 0.25
        print (f"{Khaby_Lame_Mechanism.name} speeds up his hands with to shovel food in his mouth. Your mechanism is enjoying the food, but he is a very messy eater. Age advanced by 1/4 of a day.")

    def drink(self):
        self.thirst += random.randint(1,10)
        self.hunger -= random.randint(1,2)
        self.happiness += random.randint(1,2)
        self.age += 0.25
        print (f"{Khaby_Lame_Mechanism.name} uses his hands to quickly scoop and drink up the water in his bowl. He must have been really parched. He enjoyed the water you gave him. Age advanced by 1/4 of a day.")

    def bathe(self):
        self.hygiene += random.randint(1,10)
        self.happiness -= random.randint(1,5)
        self.age += 0.25
        print (f"{Khaby_Lame_Mechanism.name} jumps into the bath, turning his hands to stay above water. However, your mechanism hates baths and isn't very happy with you. Age advanced by 1/4 of a day.")

    def rest(self):
        self.sleep += random.randint(1,10)
        self.happiness += random.randint(1,2)
        self.hunger -= random.randint(1,3)
        self.thirst -= random.randint(1,3)
        self.age += 0.25
        print (f"{Khaby_Lame_Mechanism.name} rests his weary hands and heads to sleep. He snores through the night, happily dreaming of food. Age advanced by 1/4 of a day.")
    
    def skipday(self):
        self.sleep -= random.randint(1,15)
        self.happiness -= random.randint(1,15)
        self.hunger -= random.randint(1,15)
        self.thirst -= random.randint(1,15)
        self.hygiene -= random.randint(1,15)
        self.age += 1
        print (f"You don't do anything today and decide to let {Khaby_Lame_Mechanism.name} do whatever he wants. You skip to the next day, advancing age by 1 day.")
    
    def gotowork(self):
        self.sleep -= random.randint(1,15)
        self.happiness -= random.randint(1,15)
        self.hunger -= random.randint(1,15)
        self.thirst -= random.randint(1,15)
        self.hygiene -= random.randint(1,15)
        self.money += 100
        self.age += 1
        print (f"You head out to your miserable minimum wage job, leaving {Khaby_Lame_Mechanism.name} at home by himself. You gain $100 and advance age by 1 day.")
    
    def murder(self):
        print (f"You killed {Khaby_Lame_Mechanism.name}! How dare you! I hope you are proud of yourself you monster! GAME OVER you crazy idiot!!!")
        quit()

Khaby_Lame_Mechanism = Pet("Player_Name_Choice", 50, 50, 50, 50, 50, 0, 100)
Khaby_Lame_Mechanism.name = input("You found a mechanism in a cardboard box and decide to take it home with you. What would you like to name your beautiful mechanism?")
options = [
    "Play ($50)",
    "Feed ($25)",
    "Drink ($10)",
    "Bathe ($25)",
    "Rest ($10)",
    "Skip Day ($0)",
    "Go to Work ($0)",
    "Murder ($100/QUIT GAME)"]
pet_state = "Not Dead"
while pet_state == "Not Dead":
    for index, item in enumerate(options, start = 1):
        print(index, ":", item)
    print(f"{len(options) + 1 } : View Mechanism Stats")
    choice = input(f"What would you like to do with {Khaby_Lame_Mechanism.name}? Or would you like to view {Khaby_Lame_Mechanism.name}'s stats? You have ${Khaby_Lame_Mechanism.money} to spend.")
    if not choice.isdigit():
        print("Please choose a valid choice with numbers that are displayed, or else!")
    else:
        choice = int(choice)
        if choice == 1:
            if Khaby_Lame_Mechanism.money >= 50:
                Khaby_Lame_Mechanism.play()
                Khaby_Lame_Mechanism.money -= 50
            else:
                print(f"You are missing ${50 - Khaby_Lame_Mechanism.money} to buy toys for {Khaby_Lame_Mechanism.name}. Go to work to get more money.")
        elif choice == 2:
            if Khaby_Lame_Mechanism.money >= 25:
                Khaby_Lame_Mechanism.feed()
                Khaby_Lame_Mechanism.money -= 25
            else:
                print(f"You are missing ${25 - Khaby_Lame_Mechanism.money} to buy food for {Khaby_Lame_Mechanism.name}. Go to work to get more money.")
        elif choice == 3:
            if Khaby_Lame_Mechanism.money >= 10:
                Khaby_Lame_Mechanism.drink()
                Khaby_Lame_Mechanism.money -= 10
            else:
                print(f"You are missing ${10 - Khaby_Lame_Mechanism.money} to buy water for {Khaby_Lame_Mechanism.name}. Go to work to get more money.")
        elif choice == 4:
            if Khaby_Lame_Mechanism.money >= 25:
                Khaby_Lame_Mechanism.bathe()
                Khaby_Lame_Mechanism.money -= 25
            else:
                print(f"You are missing ${25 - Khaby_Lame_Mechanism.money} to pay for the water bill to bathe {Khaby_Lame_Mechanism.name}. Go to work to get more money.")
        elif choice == 5:
            if Khaby_Lame_Mechanism.money >= 10:
                Khaby_Lame_Mechanism.rest()
                Khaby_Lame_Mechanism.money -= 10
            else:
                print(f"You are missing ${10 - Khaby_Lame_Mechanism.money} to buy sleeping pills for {Khaby_Lame_Mechanism.name}. Go to work to get more money.")
        elif choice == 6:
            Khaby_Lame_Mechanism.skipday()
        elif choice == 7:
            Khaby_Lame_Mechanism.gotowork()
        elif choice == 8:
            if Khaby_Lame_Mechanism.money >= 100:
                Khaby_Lame_Mechanism.murder()
                Khaby_Lame_Mechanism.money -= 100
            else:
                print(f"You are missing ${100 - Khaby_Lame_Mechanism.money} to buy items to murder {Khaby_Lame_Mechanism.name}. Please consider other options instead of killing your pet, brokey.")
        elif choice == len(options) + 1:
            choice = int(choice)
            print(Khaby_Lame_Mechanism.__dict__)
        else:
            print("Please choose a valid choice with numbers that are displayed, or else!")
    
   

    if Khaby_Lame_Mechanism.happiness <= 0:
        print(f"{Khaby_Lame_Mechanism.name} died of boredom and loneliness because you didn't feel like playing with it. GAME OVER")
        print(f"Final Mechanism Stats: {Khaby_Lame_Mechanism.__dict__}.")
        quit()
    elif Khaby_Lame_Mechanism.hunger <= 0:
        print(f"{Khaby_Lame_Mechanism.name} died of hunger because you didn't want to hop off the game and feed your pet. GAME OVER")
        print(f"Final Mechanism Stats: {Khaby_Lame_Mechanism.__dict__}.")
        quit()
    elif Khaby_Lame_Mechanism.thirst <= 0:
        print(f"{Khaby_Lame_Mechanism.name} died of thirst because you were too lazy scrolling on TikTok to do a simple task. GAME OVER")
        print(f"Final Mechanism Stats: {Khaby_Lame_Mechanism.__dict__}.")
        quit()
    elif Khaby_Lame_Mechanism.hygiene <= 0:
        print(f"{Khaby_Lame_Mechanism.name} died of diseases because you lack basic hygiene and didn't feel like bathing your mechanism. GAME OVER")
        print(f"Final Mechanism Stats: {Khaby_Lame_Mechanism.__dict__}.")
        quit()
    elif Khaby_Lame_Mechanism.sleep <= 0:
        print(f"{Khaby_Lame_Mechanism.name} died of insomnia and sleep deprivation because you wouldn't tuck it in at bedtime. Your mechanism couldn't sleep because you weren't there! GAME OVER")
        print(f"Final Mechanism Stats: {Khaby_Lame_Mechanism.__dict__}.")
        quit()