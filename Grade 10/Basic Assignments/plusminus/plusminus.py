import random

score = 10

while True:
    prompt = input("\n\nPress ENTER to ROLL. \n\n")
    roll = random.randint(1,6)

    if roll <= 4:
        score = score - roll
    else:
        score = score + roll
        
    print("Your roll is: {0}\nYour score is:{1}".format(roll, score))

    if score <= 0:
        print("\n\nYou LOSE\n\nSetting up a new game.")
        score = 10
        
    elif score >= 21:
        print("\n\nYou LOSE\n\nSetting up a new game.")
        score = 10


    exitResponse = input("Press ENTER to KEEP PLAYING.")
    if "\n" not in exitResponse:
        exit()
