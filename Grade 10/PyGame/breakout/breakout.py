#UNFINISHED

import sys, pygame, random

pygame.init()
pygame.key.set_repeat(10)

#pygame version
print("Version: " + str(pygame.version.ver))

#window setup
size = width, height = 640 ,480
window = pygame.display.set_mode(size)

#basic settings
gameStatus = True

ballSpeedX = 8
ballSpeedY = 8

paddleSpeed = 10

backgroundColour = [0,0,0]

arialFont = pygame.font.SysFont("Arial",14)
fontColour = [255,255,255]

#ball setup
ballColour = [255,255,255]
ballRect = pygame.Rect(310, 400, 10, 10)

#paddle setup
paddleColour = [255,255,255]
paddleRect = pygame.Rect(280, 440, 80, 10)

#bricks setup
bricks = []
brickAmount = 20
brickColour = [120, 0, 0]
distanceBetween = 60
bheight = 0
bwidth = 0

for i in range(1, brickAmount):
    bwidth += 1
    bricks.append(pygame.Rect(bwidth * distanceBetween,bheight,40,20))
    if i == 9:
        #creates a second row
        bheight = 40
        bwidth = 0 
    elif i == 18:
        bheight = 80
        bwidth = 0



#Main Game Loop
while True:

    #Controls
    for event in pygame.event.get():

        keys = pygame.key.get_pressed()
        
        if event.type == pygame.QUIT: #quit event
            pygame.quit()
            sys.exit()

        if keys[pygame.K_LEFT]:
            paddleRect.left = paddleRect.left - paddleSpeed

        if keys[pygame.K_RIGHT]:
            paddleRect.right = paddleRect.right + paddleSpeed

    #Ball Movement

    ballRect.left = ballRect.left + ballSpeedX
    ballRect.top = ballRect.top + ballSpeedY

    if ballRect.left < 0:
        ballSpeedX = ballSpeedX * -1
    elif ballRect.right > width:
        ballSpeedX = ballSpeedX * -1 # -2 speeds the ball up
    elif ballRect.top < 0:
        ballSpeedY = ballSpeedY * -1
    elif ballRect.bottom > height:
        ballRect.left = width/2
        ballRect.top = height/2

    #Ball Collision to Paddle:

    if ballRect.colliderect(paddleRect):
        ballSpeedY = -abs(ballSpeedY)

    #Game Over
    if len(bricks) <= 0 and gameStatus == True:
        gameStatus = False
        print("Game Over")
        pygame.quit()
        sys.exit()
    

    #others
    window.fill(backgroundColour)

    for everyBrick in bricks:
        #brick collision
        if ballRect.colliderect(everyBrick):
            ballSpeedY = abs(ballSpeedY)
            bricks.remove(everyBrick)

        

    #drawing
    pygame.draw.rect(window, ballColour, ballRect)

    pygame.draw.rect(window, paddleColour, paddleRect)

    #draw bricks
    for everyBrick in bricks:
        pygame.draw.rect(window, brickColour, everyBrick) #ERROR: define brick

    

    #flip + skip frames
    pygame.display.flip()
    pygame.time.wait(15)







