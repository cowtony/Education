import pygame  # this is of course needed to access the PyGame framework.
import random

# Screen size constant
HEIGHT = 400
WIDTH = 400

# Facing
UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

# Color definition
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

class Snake(object):
    def __init__(self):
        self.snakePos = [(50, 50), (60, 50)]
        self.direction = RIGHT

    def setDirection(self, dir):
        if self.direction == RIGHT and dir != LEFT:
            self.direction = dir
        if self.direction == LEFT and dir != RIGHT:
            self.direction = dir
        if self.direction == UP and dir != DOWN:
            self.direction = dir
        if self.direction == DOWN and dir != UP:
            self.direction = dir

    def move(self):
        positionX = self.snakePos[0][0]
        positionY = self.snakePos[0][1]

        if self.direction == UP:
            positionY -= 10
        elif self.direction == DOWN:
            positionY += 10
        elif self.direction == LEFT:
            positionX -= 10
        elif self.direction == RIGHT:
            positionX += 10

        self.snakePos.insert(0, (positionX, positionY))  # Add new head
        self.snakePos.pop()  # remove tail

    def isCollision(self):
        head = self.snakePos[0]  # head = (x, y)
        # 1. See if your snake touching the wall
        if head[0] < 0 or head[0] >= WIDTH:   # head[0] = x value
            return True
        if head[1] < 0 or head[1] >= HEIGHT:  # head[1] = y value
            return True
        # 2. See if your snake is touching yourself
        if head in self.snakePos[1: ]:
            return True
        return False

    def draw(self):    # This definition may not be completed.
        # Your code goes here
        # just cut and paste the two lines from main() function
        # and don't forget to call this function in the same place instead
        print('Please remove this line after you finish your code')

def getRandApplePos():
    appleX = random.randint(0, WIDTH / 10 - 1) * 10
    appleY = random.randint(0, HEIGHT / 10 - 1) * 10
    return (appleX, appleY)


def main():
    pygame.init()  # This kicks things off. It initializes all the modules required for PyGame.

    screen = pygame.display.set_mode((WIDTH, HEIGHT))  # This will launch a window of the desired size. The return value is a Surface object which is the object you will perform graphical operations on.
    pygame.display.set_caption("My Snake Game")   # optional to set caption
    clock = pygame.time.Clock()                   # The clock will be used to control how fast the screen updates

    snake_Eddie = Snake()   # Create a Snake object
    applePos = getRandApplePos()   # Get first random apple

    carryOn = True
    while carryOn:
        for event in pygame.event.get():   # This empties the event queue. If you do not call this, the windows messages will start to pile up and your game will become unresponsive in the opinion of the operating system.
            #print(event)
            if event.type == pygame.QUIT:  # This is the event type that is fired when you click on the close button in the corner of the window
                carryOn = False
            elif event.type == pygame.KEYDOWN:   # keys = pygame.key.get_pressed()   # Check keyboard input
                if event.key == pygame.K_LEFT:
                    snake_Eddie.setDirection(LEFT)
                    break
                elif event.key == pygame.K_RIGHT:
                    snake_Eddie.setDirection(RIGHT)
                    break
                elif event.key == pygame.K_UP:
                    snake_Eddie.setDirection(UP)
                    break
                elif event.key == pygame.K_DOWN:
                    snake_Eddie.setDirection(DOWN)
                    break

        snake_Eddie.move()           # Move your snake to next position

        if snake_Eddie.isCollision():
            print("Game Over!")
            clock.tick(0.5)
            carryOn = False

        # eat apple
        if snake_Eddie.snakePos[0] == applePos:
            applePos = getRandApplePos()
            # Grow
            snake_Eddie.snakePos.append(snake_Eddie.snakePos[-1])

        # Drawing section
        screen.fill(WHITE)                 # Set background color to white and clear the screen
        for point in snake_Eddie.snakePos:
            pygame.draw.rect(screen, BLUE, [point, (10, 10)], 0)
        pygame.draw.circle(screen, RED, (applePos[0] + 5, applePos[1] + 5), 5, 0)

        pygame.display.flip()              # PyGame is double-buffered. This swaps the buffers. All you need to know is that this call is required in order for any updates that you make to the game screen to become visible.
        #pygame.display.update()
        clock.tick(15)                     # unit in Hz, can be used for speed control

    pygame.quit()


main()