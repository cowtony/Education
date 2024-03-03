import pygame  # this is of course needed to access the PyGame framework.
import random

# Screen size constant
HEIGHT = 400
WIDTH = 400

# Facing
UP = 0
DOWN = 3
LEFT = 2
RIGHT = 1

# Color definition
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

########### BEGINNING OF CLASS DEFINITION #########################
class Snake(object):
    def __init__(self, startingPos, rgb = BLUE):
        self.snakePos = [startingPos]
        self.direction = RIGHT
        self.color = rgb

    def setDirection(self, dir):
        if self.direction + dir != 3:
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

    def isCollision(self, anotherSnakePos):
        head = self.snakePos[0]  # head = (x, y)
        # 1. See if your snake touching the wall
        if head[0] < 0 or head[0] >= WIDTH:   # head[0] = x value
            return True
        if head[1] < 0 or head[1] >= HEIGHT:  # head[1] = y value
            return True
        # 2. See if your snake is touching yourself
        if head in self.snakePos[1:]:
            return True
        # 3. See if you are touching others
        if head in anotherSnakePos:
            return True
        # Else:
        return False


    def draw(self, screen):
        for point in self.snakePos:
            pygame.draw.rect(screen, self.color, [point, (10, 10)], 0)

    def grow(self, applePos):
        if self.snakePos[0] == applePos:
            self.snakePos.append(self.snakePos[-1])
            return True
        else:
            return False

################ END OF CLASS DEFINITION #########################


def getRandApplePos():
    appleX = random.randint(0, WIDTH / 10 - 1) * 10
    appleY = random.randint(0, HEIGHT / 10 - 1) * 10
    return (appleX, appleY)


def main():
    pygame.init()  # This kicks things off. It initializes all the modules required for PyGame.

    screen = pygame.display.set_mode((WIDTH, HEIGHT))  # This will launch a window of the desired size. The return value is a Surface object which is the object you will perform graphical operations on.
    pygame.display.set_caption("My Snake Game")        # optional to set caption
    clock = pygame.time.Clock()                        # The clock will be used to control how fast the screen updates

    applePos = getRandApplePos()  # Get first random apple
    snake_Eddie = Snake((50, 50), BLUE)    # Create a Snake object
    snake_Jason = Snake((50, 70), GREEN)

    carryOn = True
    while carryOn:
        for event in pygame.event.get():   # This empties the event queue. If you do not call this, the windows messages will start to pile up and your game will become unresponsive in the opinion of the operating system.
            #print(event)
            if event.type == pygame.QUIT:  # This is the event type that is fired when you click on the close button in the corner of the window
                carryOn = False
            elif event.type == pygame.KEYDOWN:   # keys = pygame.key.get_pressed()   # Check keyboard input
                if event.key == pygame.K_LEFT:
                    snake_Eddie.setDirection(LEFT)
                elif event.key == pygame.K_RIGHT:
                    snake_Eddie.setDirection(RIGHT)
                elif event.key == pygame.K_UP:
                    snake_Eddie.setDirection(UP)
                elif event.key == pygame.K_DOWN:
                    snake_Eddie.setDirection(DOWN)
                elif event.key == pygame.K_w:
                    snake_Jason.setDirection(UP)
                elif event.key == pygame.K_s:
                    snake_Jason.setDirection(DOWN)
                elif event.key == pygame.K_a:
                    snake_Jason.setDirection(LEFT)
                elif event.key == pygame.K_d:
                    snake_Jason.setDirection(RIGHT)

        snake_Eddie.move()           # Move your snake to next position
        snake_Jason.move()

        if snake_Eddie.isCollision(snake_Jason.snakePos) or snake_Jason.isCollision(snake_Eddie.snakePos):
            font = pygame.font.SysFont("comicsansms", 72)
            text = font.render("Game Over", True, (0, 128, 0))
            screen.blit(text, (10, 150))
            pygame.display.flip()
            pygame.time.wait(2000)
            carryOn = False

        # eat apple
        if snake_Eddie.grow(applePos) or snake_Jason.grow(applePos):
            applePos = getRandApplePos()

        # Drawing section
        screen.fill(WHITE)                 # Set background color to white and clear the screen
        pygame.draw.circle(screen, RED, (applePos[0] + 5, applePos[1] + 5), 5, 0)  # Draw apple
        snake_Eddie.draw(screen)
        snake_Jason.draw(screen)

        pygame.display.flip()              # pygame.display.update() PyGame is double-buffered. This swaps the buffers. All you need to know is that this call is required in order for any updates that you make to the game screen to become visible.
        clock.tick(15)                     # unit in Hz, can be used for speed control

    pygame.quit()


main()
