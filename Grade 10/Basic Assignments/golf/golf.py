#golf.py
#GOAL: EQUIPPED CLUBS IN ACTION
import random, time

shot = random.randint(1,100)
timer = 6
distanceFromHole = 100
turn = 0

clubs = ["wood", "putter", "iron", "wedge"]
equippedClub = "wood"

print("\nYou are {0}m away from the hole.\n\nIf you need help, type /help.".format(distanceFromHole))

while True:

    #Clubs
    print("\nCurrent club equiped: {0}.".format(equippedClub))
    prompt = input("Press any key to shoot or type a command.")

    if "/changeclubs" in prompt.lower():
        print("Clubs: Driver, Putter, Iron, Wedge")
        chooseClub = input("Choose a club from the list above. ")
        #Choosing a Club
        if "wood" in chooseClub.lower():
            equippedClub = clubs[0]
        elif "putter" in chooseClub.lower():
            equippedClub = clubs[1]
        elif "iron" in chooseClub.lower():
            equippedClub = clubs[2]
        elif "wedge" in chooseClub.lower():
            equippedClub = clubs[3]

        print("You've equipped a {0}!".format(equippedClub.upper()))

    elif "/help" in prompt.lower():
        #Getting help
        print("Commands:\n/help -- If you need to pull out this menu.\n/changeclubs -- Replace your currently equipped club.")

    else:
        

        #Calculations

        turn = turn + 1
        
        if equippedClub == "wood":
            if distanceFromHole >= 1:
                shot = random.randint(round(distanceFromHole / 3), distanceFromHole) #Further range
                distanceFromHole -= shot
            elif distanceFromHole <= -1:
                shot = random.randint(round(distanceFromHole * 3), distanceFromHole)
            
        elif equippedClub == "putter":
            shot = random.randint(1, distanceFromHole)
            distanceFromHole = distanceFromHole - shot
            
        elif equippedClub == "iron":
            
            shot = random.randint(1, distanceFromHole)
            distanceFromHole = distanceFromHole - shot
            
        elif equippedClub == "wedge":
            shot = random.randint(1, distanceFromHole)
            distanceFromHole = distanceFromHole - shot
            
        else:
            print("You don't have a club equipped.")

        print("\nTurn: {0}\nShot: {1}m\n{2}m away from the hole.\n".format(turn, shot, distanceFromHole))

        if shot == 0:
            print("\n\nGame Over\n\n")
        
            for i in range(1,6):
                timer = timer - 1
                print("Shutting down in {0}.".format(timer))
                time.sleep(1)
            exit()
    

