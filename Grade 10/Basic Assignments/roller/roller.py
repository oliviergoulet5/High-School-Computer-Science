import random

total = 0

while True:
    
    prompt = input("\nPress enter to continue or 'q' to quit\n")
    if prompt == "":
        roll = random.randint(1,6)
        total = total + roll
        print("\nRoll: {0} Total: {1}\n".format(roll, total))
    elif prompt == "q":
        break
    else:
        print("\nInvalid Key\n")
        




