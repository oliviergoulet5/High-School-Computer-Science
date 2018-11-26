import random

def game(x):
    randomInteger = random.randint(1,15)
    question = input("Ask a question to the magic 8 ball: ")
    if randomInteger == 1:
        print("Yes.")
    elif randomInteger == 2:
        print("No.")
    elif randomInteger == 3:
        print("Stop.")
    elif randomInteger == 4:
        print("Go away.")
    elif randomInteger == 5:
        print("Maybe.")
    elif randomInteger == 6:
        print("Stop using my keyboard.")
    elif randomInteger == 7:
        print("Sure, whatever.")
    elif randomInteger == 8:
        print("I'm not rigged")
    elif randomInteger == 9:
        print("You have a messed up mind.")
    elif randomInteger == 10:
        print("LOL")
    elif randomInteger == 11:
        print("Right on!")
    elif randomInteger == 12:
        print("Possibly")
    elif randomInteger == 13:
        print("Don't ask those kinds of questions.")
    elif randomInteger == 14:
        print("That's personal")
    elif randomInteger == 15:
        print("Shutup you pig")
while True:
    game(1) 
