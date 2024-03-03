import pygame  # this is of course needed to access the PyGame framework.
pygame.init()  # This kicks things off. It initializes all the modules required for PyGame.

RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (0, 0, 255)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((500, 500))  # This will launch a window of the desired size. The return value is a Surface object which is the object you will perform graphical operations on.
pygame.display.set_caption("My Snake Game")   # optional to set caption
screen.fill(WHITE)                            # Set background color to white

carryOn = True
while carryOn:
    for event in pygame.event.get():   # This empties the event queue. If you do not call this, the windows messages will start to pile up and your game will become unresponsive in the opinion of the operating system.
        #print(event)
        if event.type == pygame.QUIT:  # This is the event type that is fired when you click on the close button in the corner of the window
            carryOn = False

    # Your code here

    pygame.draw.line(screen, BLUE, (200, 250), (100, 200), 3)
    pygame.draw.rect(screen, BLUE, [200, 250, 100, 200], 2)
    pygame.draw.polygon(screen, BLUE, [(10, 10), (40, 40), (40, 10)], 2)
    pygame.draw.lines(screen, BLUE, False, [(110, 10), (140, 40), (140, 10)], 2)
    pygame.draw.circle(screen, BLUE, (100, 100), 50, 8)
    pygame.draw.ellipse(screen, BLUE, [200, 250, 100, 200], 5)


    pygame.display.flip()              # PyGame is double-buffered. This swaps the buffers. All you need to know is that this call is required in order for any updates that you make to the game screen to become visible.
    #pygame.display.update()

pygame.quit()