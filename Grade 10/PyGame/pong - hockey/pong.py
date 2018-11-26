#Update: Add a paddle
import sys, pygame, time
pygame.init()
pygame.key.set_repeat(10)

#Version
print(pygame.version.vernum)

# Basic Settings #

paddleSpeed = 8
#Setup
size = width, height = 640, 480  #window sizes
xspeed = 2
yspeed = 3
grey = [ 100, 100, 100]
green = [0, 160, 0]
staminaColor = [246, 255, 100] #yellow
lineColor = [20, 20, 20]
white = [255, 255, 255]
font = pygame.font.SysFont("Arial", 14)

backgroundColour=grey

screen = pygame.display.set_mode(size)

#Line
line = pygame.Rect(640/2,0,10,2000)

#ball

ball = pygame.image.load("ball.png")
ballrect = ball.get_rect()
ballrect.left = width/2

#Paddle + Score
paddle2 = pygame.image.load("player1.png")
paddle2rect = paddle2.get_rect()
paddle2rect.left = 10
paddle2rect.centery = height/2

paddle1 = pygame.image.load("player2.png")
paddle1rect = paddle1.get_rect()
paddle1rect.right = width-10
paddle1rect.centery = height/2
score0 = 0
score1 = 0

#Stamina Bar
staminabar1 = pygame.Rect(640 - 100, 480 - 400, 100, 12)
staminabar2 = pygame.Rect(0 + 100, 480 - 400, 100, 12)

def backgroundChange():
    global backgroundColour
    if backgroundColour == green:
        backgroundColour = grey
    else:
        backgroundColour = green

pause = False
DLAY  = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        #Player 1 Controls

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            paddle1rect.top = paddle1rect.top - paddleSpeed
        if keys[pygame.K_DOWN]:
            paddle1rect.top = paddle1rect.top + paddleSpeed
        if keys[pygame.K_RIGHT]:
            paddle1rect.right = paddle1rect.right + paddleSpeed
        if keys[pygame.K_LEFT]:
            paddle1rect.left = paddle1rect.left - paddleSpeed

        #Player 2 Controls

        if keys[pygame.K_w]:
            paddle2rect.top = paddle2rect.top - paddleSpeed
        if keys[pygame.K_s]:
            paddle2rect.top = paddle2rect.top + paddleSpeed
        if keys[pygame.K_d]:
            paddle2rect.right = paddle2rect.right + paddleSpeed
        if keys[pygame.K_a]:
            paddle2rect.left = paddle2rect.left - paddleSpeed
        if keys[pygame.K_RSHIFT]:
            DLAY = True

    ballrect.left = ballrect.left + xspeed
    ballrect.top = ballrect.top + yspeed

    if ballrect.left < 0:
        ballrect.left=width/2+100
        score1 = score1 + 1
        backgroundChange()
        pause = True

        pygame.time.wait(5)
        xspeed = 2
        yspeed = 2
        
    if ballrect.right > width:
        pygame.time.wait(5)
        xspeed = xspeed * -1.15 # -2 speeds the ball up
    if ballrect.top < 0 or ballrect.bottom > height:
        pygame.time.wait(5)
        yspeed = yspeed * -1.15

        
    if ballrect.left+ballrect.top<100:
        temp = xspeed
        xspeed = -yspeed
        yspeed = -temp
    if width-ballrect.left+ballrect.top<100:
        temp = xspeed
        xspeed = -yspeed
        yspeed = -temp
    if ballrect.left+height-ballrect.top<100:
        temp = xspeed
        xspeed = -yspeed
        yspeed = -temp
    if width-ballrect.left+height-ballrect.top<100:
        temp = xspeed
        xspeed = -yspeed
        yspeed = -temp


    if ballrect.colliderect(paddle1rect) or ballrect.colliderect(paddle2rect): # Colliding
        pygame.time.wait(5)
        score0 = score0 + 1
        xspeed = xspeed * -1.1

    if paddle1rect.colliderect(line):
        paddle1rect.left = paddle1rect.left  + 12

    elif paddle2rect.colliderect(line):
        paddle2rect.left = paddle2rect.left - 12

    screen.fill(backgroundColour)
    pygame.draw.rect(screen, lineColor, line, 0)

    pygame.draw.line(screen, lineColor, (100,0), (0,100), 5)
    pygame.draw.line(screen, lineColor, (640,0), (0,-640), 5)

    #Stamina Bar DRAWING
    pygame.draw.rect(screen, staminaColor, staminabar1)
    pygame.draw.rect(screen, staminaColor, staminabar2)
    
    screen.blit(ball, ballrect)
    screen.blit(paddle1, paddle1rect)
    screen.blit(paddle2, paddle2rect)
    renderedText2 = font.render("Player 1: "+str(score0), 1, white)
    renderedText = font.render("Player 2: "+str(score1), 1, white)
    screen.blit(renderedText, (width/2+150, 10))
    screen.blit(renderedText2, (width/2-150, 10))
    pygame.display.flip()
    pygame.time.wait(10)
    if DLAY:
        pygame.time.wait(50)
        staminabar1.width -= 1
        if staminabar1.width <= 0:
            staminabar1.width = 0
        DLAY = False
    if pause:
        pygame.time.wait(1000)
        pause = False
        backgroundChange()
