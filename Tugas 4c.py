# ================================
# MINI TEXT ADVENTURE GAME
# ================================

# Variabel awal
current_room = "library"
inventory = []

print("\n--- Welcome to the Mini Adventure! ---")
print("Find the key and unlock the door to escape.\n")

# Game loop utama
while True:

    # =========================
    # RUANGAN: LIBRARY
    # =========================
    if current_room == "library":
        print("You are in a dusty library. There is a door to the north.")

        # Jika kunci belum diambil
        if "key" not in inventory:
            print("You see a shiny key on a table.")

        command = input("What do you do? > ").lower()

        if command == "get key":
            if "key" not in inventory:
                inventory.append("key")
                print("You picked up the key.")
            else:
                print("You already have the key.")

        elif command == "go north":
            current_room = "hallway"

        else:
            print("Invalid command.")


    # =========================
    # RUANGAN: HALLWAY
    # =========================
    elif current_room == "hallway":
        print("\nYou are in a long hallway. There is a large, locked door at the end.")
        print("The only way back is south.")

        command = input("What do you do? > ").lower()

        if command == "unlock door":
            if "key" in inventory:
                print("\nYou used the key and unlocked the door. You escaped! YOU WIN!")
                break
            else:
                print("The door is locked. You need a key.")

        elif command == "go south":
            current_room = "library"

        else:
            print("Invalid command.")
