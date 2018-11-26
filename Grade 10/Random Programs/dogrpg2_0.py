#tomorrow: Add store take money stuf
import random, time 

dog_health = 100
dog_xp = 0
dog_level = 1
coins = 0

dog_moves = ["bite", "barfk", "wag tail"]

def showCommands():
    print("showCommands() -- Show the game's commands \ncheckCoins() - Check how many coins you have. \nbattle() - Battle an enemy \nnewGame() - Create a new game\n")
def clearTerminal():
    print("\n" * 100)

def shop():
    global dog_moves
    print("\nYou entered the store...\n")
    wantToBuy = input("\nHere's what I'm selling: \nMove: Vomit(damage: 45)\n")
    
    if "vomit" in wantToBuy.lower():
        answer = input("That'll be 100 coins.\n(Type Cancel to exit the transaction.)")
        if "cancel" in answer:
            print("Goodbye then...")
        else: #agree
            dog_moves.append("vomit")
            
        
def checkCoins():
    global coins
    print("You have {0} coins.".format(coins))
def checkLevel():
    global dog_xp, dog_level
    if dog_xp >= 100:
        dog_xp = 0
        dog_level = dog_level + 1
        print("Level Up! Your current level is {0}.".format(dog_level))

currentEnemy = None
enemy_health = 100
enemy_maxHealth = 100

def newGame():
    global dog_health, dog_moves
    incorrect_breed = True
    name = input("What's the name of your mutt?\n(Enter your dog's name)")
    name_opinion_number = random.randint(1,2)
    if name_opinion_number == 1:
        print("A name suitable for such a malnourished mutt.")
    else:
        print("I would've expected a stronger mutt with a name of yours.")

    while incorrect_breed == True:
        breed = input("What's the breed of your mutt?\n(Bearded Collie, Whippet, Rat Terrier)")
        if "whip" in breed.lower() or "beard" in breed.lower() or "rat" in breed.lower():
               
            incorrect_breed == False
            break
        else:
            print("Choose a valid breed of mutt.\n\n")

    if name == "Steve Buscemi":
        dog_health = 100000
        dog_moves.append("lick a roach")
        dog_moves.append("scoop eyeballs")


def enemy_eatMcDouble():
    global enemy_health, currentEnemy
    print("{0} begins to eat a McDouble.".format(currentEnemy))
    time.sleep(6)
    for i in range(1,20):
        print("OM NOM NOM NOM" * 5)
    print("\n" * 5)
    print("{0} finished his McDouble. He has diabetes and loses 75 HP.".format(currentEnemy))
    enemy_health -= 75

def enemy_thatsGravity():
    global dog_health
    print("\nYou fall off your chair...\n")
    print("Stan: THATS GRAVITY!")
    print("\nYou can't take his insult. He tips his fedora.You begin to have a seizure over the cringe.\n")
    time.sleep(8)
    for i in range(1,1000):
        print("AFRARYARAYRYARAGRHRGHRGAHRHRGAHGRAHRGAHRGAHGRAHGRHAGHGRAHGRHARGAHRGAHAHAHHAHAAAAAHAHAHAHAHHA BAR ARARR RARRRR")
        print("BAR BAR YAR BREERRR BAARR ARRRRR OH NAA RBAAR BAAAR")
        print("AFARKARKRKARKARBRBABRRBABRBABRBARBABRABRA")
        print("ARF ARGF ARRGY")
        print("HELP ARHRHAHRHRHAHRHRAHR ARGY FRYYH AAARHHH ARRAALLAALALALAP AALALALAALALALLAP")
        print("cringe!")
        
    dog_health = dog_health - 60
    print("\n" * int(100) + "Ron Perlman gives you CPR.\nYou are relieved to still be alive but you still hate your life.")

def enemy_showMeme():
    global dog_health
    print("\nStan the Man: Do you want to see something funny?")
    youranswer = input("Do you? ")
    print("\nStan the Man shows you a meme on his phone.")
    print("\nYou hate your life. You off yourself.")
    dog_health = 0

def enemy_deathByScooter():
    global dog_health, currentEnemy
    print("\n{0} chucks a scooter. The scooter hits you in the face.".format(currentEnemy))
    print("\nYou take 10 damage")
    dog_health = dog_health - 10

def enemy_fedora():
    global dog_health
    print("\nStan the Man does a fedora trick.")
    print("\nYou vomit your guts out.")
    print("\nYou take 40 damage")
    dog_health = dog_health - 40
def enemy_vomit():
    global dog_health
    print("I have an urge to..")
    print("\nThe unhealthy beast vomits on your foot")

def enemy_yell():
    while True:
        print("Enemy yells")
        time.sleep(3)
        for i in range(1,25):
            print("AAAAAAAAAAHHHHHH")
        stopit = input("Tell him to stop: ")
        if "stop" in stopit.lower():
            break

def enemy_humpLeg():
    global dog_health
    print("The dog begins to hump your leg.")
    stopit = input("Tell him to stop humping your leg: ")
    while True:
        if "stop" in stopit.lower():
            break
        
def enemy_needle():
    global dog_health
    print("Get pricked by my needle you stupid pooch.")
    dog_health = dog_health - 25

def neuter():
    global dog_health
    dog_health = dog_health - 50
    print("I'm going to neuter you! Get chopped, hound.")

def enemy_headbutt():
    global dog_health, enemy_health
    dog_health = dog_health - 30
    enemy_health = enemy_health - 25
    print("I'm goner hedburt yar facenuts")


def vomit():
    global enemy_health
    damage = 45 #damage
    print("\nYou begin to vomit...\n\nBWAHARARARARARARARARGGGGGGGBLEEEURGGGGGGG\n")
    enemy_health = enemy_health - damage
def eatGrass():
    global dog_health
    seizure_chances = random.randint(1,4)
    if seizure_chances == 1:
        print("You begin to have a seizure.\n\nByarararararafk BAYAAYAFAFRAFRAK BOARLARLALRARLRARLA FARARARARARARALLRARARARARARLARLARLARARAR\n\nYou lose 75 hp.")
        dog_health = dog_health - 75 # damage
    else:
        print("OMONOMNOMNOMNOM\n You restore 10 hp")
        dog_health = dog_health + 10
        
def bite():
    global enemy_health
    damage = 25
    print("Crrrkrk, meueehehe\n{0} loses {1} HP.".format(currentEnemy, damage))
    enemy_health = enemy_health - damage
    
def barfk():
    global enemy_health
    damage = 15
    enemy_health = enemy_health - damage
    print("BARFK BARFK BUERUEK BARFEKEK BURF BARF\n{0} loses {1} HP.".format(currentEnemy, damage))

def scoopEyeBalls():
    global enemy_health
    damage = 50
    print("Scloop Scloop Scloop, i got ur i balls")
    enemy_health -= damage
    
def lickRoaches():
    global enemy_health
    damage = 50
    print("Lik lik de roach")
    enemy_health -= damage
    
    
def battle():
    #finding an opponent
    global currentEnemy, enemy_health, dog_health, dog_xp, enemy_maxHealth, coins
    enemy_health = enemy_maxHealth
    enemies = ["Stray Cat", "Bruno the Squirrel", "shadow", "Bart the Bear", "Eugene the Rat Terrier", "The Euthanizer", "Stan the Man", "Dominic the McDonald Warrior", "Gordon the Golden Retriever"]
    enemy = random.randint(1,len(enemies))
    currentEnemy = enemies[enemy]
    turn = True
    randomCoins = random.randint(1,250)
    
    xpGain = 50
    coinsGain = randomCoins

    
    #ENEMY STATISTICS
    if currentEnemy == "The Euthanizer":
        enemy_health = 250
        print("The Euthanizer: I'm going to put you down, you domesticated rat!\n")
    elif currentEnemy == "Stan the Man":
        enemy_health = 80


    print("You've encountered {0}!".format(currentEnemy.upper()))
    #fighting moves
    
    while enemy_health >= 1:
        print("\nEnemy:\nhealth = {0}\n\nYou:\nhealth = {1}\n".format(enemy_health, dog_health))

        print("\n\nWait for your turn.\n\n")
        time.sleep(3)
        #Enemy Turn/Your Turn
        
        if turn == True:
            move = input(str(dog_moves))
    
            if "bite" in move.lower():
                bite()
                turn = False
            elif "barfk" in move.lower():
                barfk()
                turn = False
            elif "grass" in move.lower():
                eatGrass()
                turn = False
            elif "tail" in move.lower():
                wagTail()
                turn = False

            elif "vomit" in move.lower():
                for i in range(1, len(dog_moves)):
                    if dog_moves[i] == "vomit":
                        vomit()
            elif "scoop" in move.lower():
                for i in range(1, len(dog_moves)):
                    if dog_moves[i] == "scoop eyeballs":
                        scoopEyeBalls()

            elif "lick" in move.lower():
                for i in range(1, len(dog_moves)):
                    if dog_moves[i] == "lick a roach":
                        lickRoaches()
            elif "dead" in move.lower():
                print("You play dead.\nThe enemy drops a tear and walks away with regrets.")
                print("You lose {0} coins".format(coinsGain))
                coins = coins - coinsGain # Opposite Operation
                break
        elif turn == False:

            if currentEnemy == "The Euthanizer":
                randomMove = random.randint(1,2)
                if randomMove == 1:
                    enemy_needle()
                    turn = True

                else:
                    neuter()
                    turn = True

            elif currentEnemy == "Stray Cat" or currentEnemy == "Bart the Bear" or currentEnemy == "Eugene the Rat Terrier":
                randomMove = random.randint(1,2)
                if randomMove == 1:
                    enemy_vomit()
                    turn = True
                elif randomMove == 2:
                    enemy_yell()
                    turn = True

            elif currentEnemy == "Dominic the McDonald Warrior":
                randomMove == random.randint(1,2)
                if randomMove == 1:
                    enemy_eatMcDouble()
                    turn = True
                elif randomMove == 2:
                    enemy_deathByScooter()
                    turn = True

            elif currentEnemy == "Stan the Man":
                randomMove = random.randint(1,3)
                if randomMove == 1:
                    enemy_showMeme()
                    turn = True
                elif randomMove == 2:
                    enemy_thatsGravity()
                    turn = True
                elif randomMove == 3:
                    turn = True
                    enemy_fedora()

            elif currentEnemy == "Gordon the Golden Retriever":
                randomMove = random.randint(1,3)]
                if randomMove == 1:
                    enemy_headbutt()
                elif randomMove == 2:
                    enemy_humpLeg()
                elif randomMove == 3:
                    enemy_dragBodyAroundCarpet()

            else:
                turn = True
                    
    if enemy_health <= 0:
        print("You've earned {0} XP".format(xpGain))
        dog_xp = dog_xp + xpGain
        coins = coins + coinsGain
        print("You gain {0} coins!".format(coinsGain))
        checkLevel()
    

newGame()

