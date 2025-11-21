import random

GOBLINS=["Glok", "Brak", "Sniv", "Grim", "Zog", "Mug", "Ruk", "Thok"]

# Class player:

# Class goblin:

class goblin:
    def __init__(self, name, health):
        self.name = name
        self.health = health
    
    def attack(self, target):
        print(f"{self.name} attacks {target}!")
    
    def take_damage(self, amount):
        self.health =- amount
        print(f"{self.name} takes {amount} damage. Health = {self.health}")

class fire_goblin(goblin):
    def __init__(self, name, health, fire_power):
        super().__init__(name, health)
        self.fire_power = fire_power
    
    def attack(self, target):
        print(f"{self.name} attacks {target} with fire power {self.fire_power}!")


# Class goblin_shaman:
random_name = random.choice(GOBLINS)
goblin_1 = fire_goblin(random_name, random.randint(20, 50))

print("A wild goblin appears!")
print("Goblin Name:", goblin_1.name)
print("Goblin Health:", goblin_1.health)

goblin_1.take_damage(10)
