import pygame  # this is of course needed to access the PyGame framework.
pygame.init()  # This kicks things off. It initializes all the modules required for PyGame.

RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (0, 0, 255)
WHITE = (255, 255, 255)

# Initialization
screen = pygame.display.set_mode((500, 500))  # This will launch a window of the desired size. The return value is a Surface object which is the object you will perform graphical operations on.
pygame.display.set_caption("My Snake Game")   # optional to set caption
clock = pygame.time.Clock()                   # The clock will be used to control how fast the screen updates

positionX = 50
positionY = 50
direction = 3                # UP = 0, DOWN = 1, LEFT = 2, RIGHT = 3
eggPNG = pygame.image.load("Easter_Egg.png")
eggPNG = pygame.transform.scale(eggPNG, (50, 60))

carryOn = True
while carryOn:
    for event in pygame.event.get():   # This empties the event queue. If you do not call this, the windows messages will start to pile up and your game will become unresponsive in the opinion of the operating system.
        #print(event)
        if event.type == pygame.QUIT:  # This is the event type that is fired when you click on the close button in the corner of the window
            carryOn = False
        keys = pygame.key.get_pressed()   # Check keyboard input
        if keys[pygame.K_LEFT]:
            direction = 2
            # positionX -= 10
        if keys[pygame.K_RIGHT]:
            direction = 3
            # positionX += 10
        if keys[pygame.K_UP]:
            direction = 0
            # positionY -= 10
        if keys[pygame.K_DOWN]:
            direction = 1
            # positionY += 10

    # Your code here
    screen.fill(WHITE)                 # Set background color to white and clear the screen
    if direction == 0:   # UP
        positionY -= 5
    elif direction == 1:  # DOWN
        positionY += 5
    elif direction == 2:  # LEFT
        positionX -= 5
    elif direction == 3:   # RIGHT
        positionX += 5

    pygame.draw.rect(screen, BLUE, [positionX, positionY, 10, 10], 0)
    screen.blit(eggPNG, (positionX, positionY))

    pygame.display.flip()              # PyGame is double-buffered. This swaps the buffers. All you need to know is that this call is required in order for any updates that you make to the game screen to become visible.
    #pygame.display.update()
    clock.tick(30)                     # Limit to 30 frames per second

pygame.quit()