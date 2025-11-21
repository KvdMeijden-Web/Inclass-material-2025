import random

GOBLIN_NAMES = ["Grok", "Zug", "Blarg", "Mog", "Thok", "Ruk", "Snag", "Grim", "Vex", "Dreg"]

class player:
    def __init__(self, name, level, health):
        self.name = name
        self.level = level
        self.health = health

    def attack(self, target, damage):
        print(f"{self.name} attacks {target} at level {self.level}")
        return self.level * damage

    def take_damage(self, amount):
        self.health = max(self.health - amount, 0)
        print(f"{self.name} takes {amount} damage. Health = {self.health}")


class Goblin:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, target):
        print(f"{self.name} attacks {target} with power {self.attack_power}")
        return self.attack_power

    def take_damage(self, amount):
        self.health = max(self.health - amount, 0)
        print(f"{self.name} takes {amount} damage. Health = {self.health}")


# make goblin list
def goblin_list():
    amount_of_goblins = random.randint(2, 5)
    print(f"You are attacked by {amount_of_goblins} goblins!")
    goblin_list = []
    for i in range(amount_of_goblins):
        goblin_name = random.choice(GOBLIN_NAMES)
        goblin_health = random.randint(30, 70)
        goblin_attack_power = random.randint(5, 15)
        goblin_list.append(Goblin(goblin_name, goblin_health, goblin_attack_power))
    print(f"Their names are: {', '.join([goblin.name for goblin in goblin_list])}")
    return goblin_list


goblins = goblin_list()
player1 = player("Hero", 1, 150)

while len(goblins) > 0 and player1.health > 0:
    print("\nCurrent goblins:")
    for g in goblins:
        print(f"- {g.name}: {g.health} HP, {g.attack_power} ATK")

    target_name = input("Who will you attack? ")

    # find target goblin by name
    target_goblin = None
    for goblin in goblins:
        if goblin.name.lower() == target_name.lower():
            target_goblin = goblin
            break

    if target_goblin is None:
        print("No goblin with that name. Try again.")
        continue

    # player attacks chosen goblin
    player_damage = player1.attack(target_goblin.name, 10)
    target_goblin.take_damage(player_damage)

    # remove goblin if dead
    if target_goblin.health <= 0:
        print(f"{target_goblin.name} has been defeated!")
        goblins.remove(target_goblin)

    # if all goblins are dead, end battle
    if len(goblins) == 0:
        print("You have defeated all the goblins!")
        break

    # goblins' turn to attack
    print("\nThe goblins strike back!")
    for goblin in goblins:
        goblin_damage = goblin.attack("Hero")
        player1.take_damage(goblin_damage)
        if player1.health <= 0:
            print("You have been defeated!")
            break

if player1.health > 0 and len(goblins) == 0:
    print("Victory!")
elif player1.health <= 0:
    print("Game over.")






# -------------------------
# Base class (blueprint)
# -------------------------
# class Goblin:
#     def __init__(self, name, health):
#         self.name = name
#         self._health = health         

#     def take_damage(self, amount):
#         self._health = max(self._health - amount, 0)
#         print(f"{self.name} takes {amount} damage. Health = {self._health}")

#     def attack(self, target):
#         # generic goblin attack
#         print(f"{self.name} hits {target} with a club!")


# # -------------------------
# # Inheritance: different goblin types
# # -------------------------
# class FireGoblin(Goblin):
#     def __init__(self, name, health, fire_power):
#         super().__init__(name, health)
#         self.fire_power = fire_power

# #     # Polymorphism: same method name, different behavior
# #     def attack(self, target):
# #         print(f"{self.name} throws fire at {target}! "
# #               f"Fire damage = {self.fire_power}")


# # class HealerGoblin(Goblin):
# #     def __init__(self, name, health, heal_power):
# #         super().__init__(name, health)
# #         self.heal_power = heal_power

# #     def heal(self, ally):
# #         print(f"{self.name} heals {ally} for {self.heal_power} HP!")


# # -------------------------
# # Using the classes (objects)
# # -------------------------
# g1 = Goblin("Gruk", 50)
# # g2 = FireGoblin("Blaz", 40, fire_power=15)
# # g3 = HealerGoblin("Mendik", 35, heal_power=10)

# g1.attack("hero")      # base behavior
# # g2.attack("hero")      # polymorphic behavior
# # g3.heal("Gruk")        # extra behavior
# g1.take_damage(20)
# # g2.take_damage(10)
