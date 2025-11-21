import random

# --- Step 1: Setup your monsters ---
monster_names = ["Drako", "Blobbit", "Zapcat"]
monster_health = [100, 80, 60]
monster_attack = [20, 15, 25]

enemy_names = ["Goblin", "Ogre", "Slime"]
enemy_health = [90, 110, 70]
enemy_attack = [18, 22, 12]

# --- Step 2: Display team info ---
def show_teams():
    print("\n=== Your Team ===")
    for i in range(len(monster_names)):
        print(f"{i+1}. {monster_names[i]} (HP: {monster_health[i]}, ATK: {monster_attack[i]})")

    print("\n=== Enemy Team ===")
    for i in range(len(enemy_names)):
        print(f"{i+1}. {enemy_names[i]} (HP: {enemy_health[i]}, ATK: {enemy_attack[i]})")
    print()

# --- Step 3: Main battle loop ---
print("⚔️ Welcome to Monster Arena! ⚔️")

while len(monster_names) > 0 and len(enemy_names) > 0:
    show_teams()

    # Player chooses a monster
    try:
        choice = int(input("Choose your monster (1–3): ")) - 1
        if choice < 0 or choice >= len(monster_names):
            print("Invalid choice, try again!")
            continue
    except ValueError:
        print("Please enter a number!")
        continue
2
    # Randomly choose an enemy
    enemy_choice = random.randint(0, len(enemy_names) - 1)

    # --- Player's Attack ---
    print(f"\n{monster_names[choice]} attacks {enemy_names[enemy_choice]}!")
    damage = monster_attack[choice]
    enemy_health[enemy_choice] -= damage
    print(f"💥 {enemy_names[enemy_choice]} took {damage} damage! Remaining HP: {max(enemy_health[enemy_choice], 0)}")

    # Check if enemy fainted
    if enemy_health[enemy_choice] <= 0:
        print(f"💀 {enemy_names[enemy_choice]} fainted!")
        del enemy_names[enemy_choice]
        del enemy_health[enemy_choice]
        del enemy_attack[enemy_choice]
        if len(enemy_names) == 0:
            break
        continue  # Skip enemy turn if it fainted

    # --- Enemy Counterattack ---
    attacker = random.randint(0, len(enemy_names) - 1)
    defender = random.randint(0, len(monster_names) - 1)
    print(f"\n{enemy_names[attacker]} counterattacks {monster_names[defender]}!")
    damage = enemy_attack[attacker]
    monster_health[defender] -= damage
    print(f"🔥 {monster_names[defender]} took {damage} damage! Remaining HP: {max(monster_health[defender], 0)}")

    # Check if player's monster fainted
    if monster_health[defender] <= 0:
        print(f"💀 {monster_names[defender]} fainted!")
        del monster_names[defender]
        del monster_health[defender]
        del monster_attack[defender]

# --- Step 4: End game message ---
if len(enemy_names) == 0:
    print("\n🎉 You win! All enemies defeated!")
else:
    print("\n💀 You lose! All your monsters fainted!")
