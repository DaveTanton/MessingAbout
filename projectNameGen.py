import random

print("Operational Name Generator")

namesList = ("King", "Queen", "Grim", "Joint", "Olive", "Wing", "Archers", "Talon", "Shield",
    "Praire", "Mustang", "Swift", "Response", "Crimson", "Sahara", "Alpha", "Eagle", "Black", "Typhoon",
    "Goodwood", "Distant", "Cougar", "Desert", "Tempest", "Heart", "Arcade", "Fusion", "Strike", "Warrior",
    "Blade", "Grove", "Leopard", "Reach", "Evade", "Eagle", "Storm", "Raid", "Trial", "Bayonet",
    "Ace", "Alligator", "Revival", "Spider", "Blade", "Valour", "Magic", "Carpet", "Lancer", "Chameleon",
    "Griffin", "Sword", "Crusader", "Merlin", "Spear", "Point", "Lion", "Blizzard", "Hammer", "Anvil",
    "Atlantic", "Serpent", "High", "Diamond", "Highlander", "Centurion", "Scholar", "Red", "White", "Green",
    "Grey", "Guardian", "Vortex", "Clockwork", "Lynx", "Jaguar", "Tiger", "Buccaneer", "Dagger", "Iron",
    "Steel", "Gold", "Silver", "Forge", "Evening", "Light", "Nimble", "Grand", "Slam", "Claw",
    "Prime", "Mantis", "Cactus", "Hawk", "Falcon", "Trident", "Urgent", "Fury", "Dragon", "Blue",
    "Winged", "wiskey", "vodaka", "Gin")

tryAgain = "y"

while tryAgain == "y":
    prefixlist = ("Operation: ", "Project: ", "Exercise: ", "mission: ")
    prefixoption = int(input("\nenter your prefix\n\t1. Operation\n\t2. Project\n\t3. Exercise\n\t4. mission\n\t\tenter option: "))
    prefixname = prefixlist[prefixoption-1]

    namelength = input("\ndo you want\n\t1. one name.\n\t2. two names.\n\t\tenter option: ")
    namelength = int(namelength)

    numnames = input("\nhow many names do you want generated: ")
    numnames = int(numnames)
    print("")

    count = 0
    for x in range(numnames):
        count += 1
        if namelength == 1:
            randOne = random.randint(0, len(namesList))
            firstName = namesList[randOne]
            print(count,prefixname,firstName)

        if namelength == 2:
            randOne = random.randint(0, len(namesList))
            firstName = namesList[randOne]
            randTwo = randOne  
            secondName = namesList[randTwo]
           
            while firstName == secondName:
                secondName = namesList[random.randint(0, len(namesList))]
            print(count,prefixname,firstName, secondName)

    tryAgain = input("\nTry again ? Y/N : ")
    tryAgain = tryAgain.lower()
© 2021 GitHub, Inc.
