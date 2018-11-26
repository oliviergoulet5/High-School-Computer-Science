import random, time

level = 1
keys = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "[", ";"]
words = []

def loadString():
    global words, level, keys
    for i in range(1,level + 5):
        randomNumber = random.randint(0, len(keys))
        randomKey = keys[randomNumber]
        words.append(randomKey)
        
        

startgame = input("Enter any key to play the game. ")

time.sleep(2)

print("Memorize the following string of letters...")

loadString()

print(words)

answer = input("Letters: ")

time.sleep(25 - level)

if answer





    
    
