games = ["1. Hollow Knight","2. Minecraft","3. The Witcher 3: Wild Hunt","4. Phasmophobia","5. Resident Evil 4"]
loop = True
print(games)
while loop == True:
    game = str(input("Input a game name from the list: "))
    if game.lower() == "hollow knight":
        gamestatus = input("Played or Favourite?")
        if gamestatus.lower() == "played":
            games.append("1. Hollow Knight (Played)")
            games.remove("1. Hollow Knight")
            games.sort()
            print(games)
        elif gamestatus.lower() == "favourite":
            games.append("1. Hollow Knight (Favourited)")
            games.remove("1. Hollow Knight")
            games.sort()
            print(games)
        else:
            print("No changes made")
            print(games)
    elif game.lower() == "minecraft":
        gamestatus = input("Played or Favourite?")
        if gamestatus.lower() == "played":
            games.append("2. Minecraft (Played)")
            games.remove("2. Minecraft")
            games.sort()
            print(games)
        elif gamestatus.lower() == "favourite":
            games.append("2. Minecraft (Favourited)")
            games.remove("2. Minecraft")
            games.sort()
            print(games)
        else:
            print("No changes made")
            print(games)
    elif game.lower() == "the witcher 3: wild hunt":
        gamestatus = input("Played or Favourite?")
        if gamestatus.lower() == "played":
            games.append("3. The Witcher 3: Wild Hunt (Played)")
            games.remove("3. The Witcher 3: Wild Hunt")
            games.sort()
            print(games)
        elif gamestatus.lower() == "favourite":
            games.append("3. The Witcher 3: Wild Hunt (Favourited)")
            games.remove("3. The Witcher 3: Wild Hunt")
            games.sort()
            print(games)
        else:
            print("No changes made")
            print(games)
    elif game.lower() == "phasmophobia":
        gamestatus = input("Played or Favourite?")
        if gamestatus.lower() == "played":
            games.append("4. Phasmophobia (Played)")
            games.remove("4. Phasmophobia")
            games.sort()
            print(games)
        elif gamestatus.lower() == "favourite":
            games.append("4. Phasmophobia (Favourited)")
            games.remove("4. Phasmophobia")
            games.sort()
            print(games)
        else:
            print("No changes made")
            print(games)
    elif game.lower() == "resident evil 4":
        gamestatus = input("Played or Favourite?")
        if gamestatus.lower() == "played":
            games.append("5. Resident Evil 4 (Played)")
            games.remove("5. Resident Evil 4 ")
            games.sort()
            print(games)
        elif gamestatus.lower() == "favourite":
            games.append("5. Resident Evil 4  (Favourited)")
            games.remove("5. Resident Evil 4 ")
            games.sort()
            print(games)
        else:
            print("No changes made")
            print(games)
    else:
        print("Incorrect value")

