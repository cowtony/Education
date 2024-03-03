import pygame  # this is of course needed to access the PyGame framework.
import random

# Initialization pygame
HEIGHT = 400
WIDTH = 400

# Constant & enum
UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

class Snake(object):
    def __init__(self):
        self.snakePos = [(50, 50), (60, 50)]
        self.direction = RIGHT

def getRandApplePos():
    appleX = random.randint(0, WIDTH / 10 - 1) * 10
    appleY = random.randint(0, HEIGHT / 10 - 1) * 10
    return (appleX, appleY)

def main():
    pygame.init()  # This kicks things off. It initializes all the modules required for PyGame.

    # Color definition
    RED   = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE  = (0, 0, 255)
    WHITE = (255, 255, 255)


    screen = pygame.display.set_mode((WIDTH, HEIGHT))  # This will launch a window of the desired size. The return value is a Surface object which is the object you will perform graphical operations on.
    pygame.display.set_caption("My Snake Game")   # optional to set caption
    clock = pygame.time.Clock()                   # The clock will be used to control how fast the screen updates



    # Initial Snake description
    snake = Snake()

    # Initial Apple
    applePos = getRandApplePos()


    carryOn = True
    while carryOn:
        for event in pygame.event.get():   # This empties the event queue. If you do not call this, the windows messages will start to pile up and your game will become unresponsive in the opinion of the operating system.
            #print(event)
            if event.type == pygame.QUIT:  # This is the event type that is fired when you click on the close button in the corner of the window
                carryOn = False
            elif event.type == pygame.KEYDOWN:   # keys = pygame.key.get_pressed()   # Check keyboard input
                if event.key == pygame.K_LEFT and snake.direction != RIGHT:
                    snake.direction = LEFT
                elif event.key == pygame.K_RIGHT and snake.direction != LEFT:
                    snake.direction = RIGHT
                elif event.key == pygame.K_UP and snake.direction != DOWN:
                    snake.direction = UP
                elif event.key == pygame.K_DOWN and snake.direction != UP:
                    snake.direction = DOWN

        # Calculate Next
        positionX = snake.snakePos[0][0]
        positionY = snake.snakePos[0][1]

        if snake.direction == UP and positionY >= 10:
            positionY -= 10
        elif snake.direction == DOWN and positionY < HEIGHT - 10:
            positionY += 10
        elif snake.direction == LEFT and positionX >= 10:
            positionX -= 10
        elif snake.direction == RIGHT and positionX < WIDTH - 10:
            positionX += 10

        # move
        snake.snakePos.insert(0, (positionX, positionY))   # Add new head
        snake.snakePos.pop()                               # remove tail

        # eat apple
        if snake.snakePos[0] == applePos:
            applePos = getRandApplePos()
            # Grow
            snake.snakePos.append(snake.snakePos[-1])

        # Drawing section
        screen.fill(WHITE)                 # Set background color to white and clear the screen
        for point in snake.snakePos:
            pygame.draw.rect(screen, BLUE, [point, (10, 10)], 0)
        pygame.draw.circle(screen, RED, (applePos[0] + 5, applePos[1] + 5), 5, 0)

        pygame.display.flip()              # PyGame is double-buffered. This swaps the buffers. All you need to know is that this call is required in order for any updates that you make to the game screen to become visible.
        #pygame.display.update()
        clock.tick(15)                     # unit in Hz, can be used for speed control

    pygame.quit()

main()