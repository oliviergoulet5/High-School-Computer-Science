import random

score = 0

print("This is a two player game that requires teamwork to win. If you answer a point correctly then your team will get a point, if you get an answer incorrectly then you'll lose one.")

player1 = input("What's the name of PLAYER 1? ")
player2 = input("What's the name of PLAYER 2? ")

def scoreUp():
    global score
    score = score + 1

def scoreDown():
    global score
    score = score - 1

while True:
    
    randomNum = random.randint(0,3)

    randomPlayer = random.randint(0,1)

    randomSelection = [1,2,3,4]

    question = randomSelection[randomNum] # TO ADD: player name in prints

    if randomPlayer == 0:
        currentPlayer = player1
    else:
        currentPlayer = player2

    if question == 1:
        trivia = input("Question for " + player1 + ": Who was the first prime minister of Canada?")
        if "john" in trivia.lower():
            scoreUp()
            print("Correct! You now have a score of " + str(score) + "!")
            

        else:
            scoreDown()
            print("False, you now lose a point! Your score is now " + str(score))

    elif question == 2:
        trivia = input("Question for " + player2 + ": What's the 4th planet closest to the Sun? ")
        if "mars" in trivia.lower():
            scoreUp()
            print("Correct! You now have a score of " + str(score) + "!")

        else:
            scoreDown()
            print("False, you now lose a point! Your score is now " + str(score))

    elif question == 3:
        trivia = input("Question for " + player1 + ": What's the biggest city in Canada? ")
        if "tor" in trivia.lower():
            scoreUp()
            print("Correct! You now have a score of " + str(score) + "!")

        else:
            scoreDown()
            print("False, you now lose a point! Your score is now " + str(score))

    elif question == 4:
        trivia = input("Question for " + player2 + ": How many countries are there in the world? ")
        if "196" in trivia.lower():
            scoreUp()
            print("Correct! You now have a score of " + str(score) + "!")
        else:
            scoreDown()
            print("False, you now lose a point! Your score is now " + str(score))
                  


