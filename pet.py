# Activity 1

class Hero:
    def __init__(self, name, money, inventory):
        self.name = name
        self.money = money
        self.inventory = inventory

    def buy(self, item):
        self.inventory.append(item)
        print(self.inventory)
Khaby_Lame_Mechanism = Hero("Khaby_Lame_Mechanism", 500, ["Hands of Fate"])

print(Khaby_Lame_Mechanism.__dict__)

Khaby_Lame_Mechanism.buy({"item": "Upraded Hands of Time", "attack": 61})
print(Khaby_Lame_Mechanism.__dict__)