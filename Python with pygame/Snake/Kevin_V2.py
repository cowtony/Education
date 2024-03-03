import pygame  # this is of course needed to access the PyGame framework.
import random
import time

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

########### APPLE CLASS #################

class Apple(object):
    def __init__(self, pow):
        self.power = pow
        self.x = random.randint(0, WIDTH / 10 - 1) * 10
        self.y = random.randint(0, HEIGHT / 10 - 1) * 10

    def getRandApplePos(self):
        self.x = random.randint(0, WIDTH / 10 - 1) * 10
        self.y = random.randint(0, HEIGHT / 10 - 1) * 10
########### END OF APPLE CLASS ##################

########### BEGINNING OF CLASS DEFINITION #########################
class Snake(object):
    def __init__(self, startingPos, rgb = BLUE):
        self.snakePos = [startingPos]
        self.direction = RIGHT
        self.color = rgb

    def setDirection(self, dir):
        if self.direction == RIGHT and dir != LEFT:
            self.direction = dir
            return True
        if self.direction == LEFT and dir != RIGHT:
            self.direction = dir
            return True
        if self.direction == UP and dir != DOWN:
            self.direction = dir
            return True
        if self.direction == DOWN and dir != UP:
            self.direction = dir
            return True
        return False

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

        if head in anotherSnakePos:
            return True

        return False

    def draw(self, screen):
        for point in self.snakePos:
            pygame.draw.rect(screen, self.color, [point, (10, 10)], 0)

    def grow(self, apple):
        if self.snakePos[0] == (apple.x, apple.y):
            for i in range(apple.power):
                self.snakePos.append(self.snakePos[-1])
            return True
        else:
            return False


    #Mu: You don't need to define grow2() function, try to find out a general way for snake to grow 1 or more.
    # def grow2(self, apple2Pos):
    #      if self.snakePos[0] == apple2Pos:
    #          for i in range(1):
    #              self.snakePos.append(self.snakePos[-1])
    #          return True
    #      else:
    #          return False

    def autonomous(self, apple):
        if apple.x > self.snakePos[0][0]:
            if self.setDirection(RIGHT):
                return
        if apple.x < self.snakePos[0][0]:
            if self.setDirection(LEFT):
                return
        if apple.y > self.snakePos[0][1]:
            if self.setDirection(DOWN):
                return
        if apple.y < self.snakePos[0][1]:
            if self.setDirection(UP):
                return

        # handle RIGHT BEHIND YOU situation
        if apple.x == self.snakePos[0][0] and apple.y < self.snakePos[0][1] and self.direction == DOWN:
            if self.setDirection(LEFT):
                return
        if apple.y == self.snakePos[0][1] and apple.x < self.snakePos[0][0] and self.direction == RIGHT:
            if self.setDirection(DOWN):
                return
        if apple.x == self.snakePos[0][0] and apple.y > self.snakePos[0][1] and self.direction == UP:
            if self.setDirection(RIGHT):
                return
        if apple.y == self.snakePos[0][1] and apple.x > self.snakePos[0][0] and self.direction == LEFT:
            if self.setDirection(UP):
                return


################ END OF CLASS DEFINITION #########################


# this can be deleted since this function is moved in to the class of Apple
# def getRandApplePos():
#     appleX = random.randint(0, WIDTH / 10 - 1) * 10
#     appleY = random.randint(0, HEIGHT / 10 - 1) * 10
#     return (appleX, appleY)

def main():
    pygame.init()  # This kicks things off. It initializes all the modules required for PyGame.
    score = 0
    score1 = 0
    screen = pygame.display.set_mode((WIDTH, HEIGHT))  # This will launch a window of the desired size. The return value is a Surface object which is the object you will perform graphical operations on.
    pygame.display.set_caption("My Snake Game")   # optional to set caption
    clock = pygame.time.Clock()                   # The clock will be used to control how fast the screen updates
    myfont = pygame.font.SysFont("comicsans", 16)
    myImage = pygame.image.load('BG.jpg')
    myImage = pygame.transform.scale(myImage, (WIDTH, HEIGHT))

    # applePos = getRandApplePos()  # Get first random apple
    # apple2Pos = getRandApplePos()
    normalApple = Apple(1)
    superApple = Apple(1)  # New way of generating two different apple.



    snake_Eddie = Snake((0, 0), RED)    # Create a Snake object
    snake_Jason = Snake((50, 70))


    start = time.time()

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
                if event.key == pygame.K_w:
                    snake_Jason.setDirection(UP)
                elif event.key == pygame.K_s:
                    snake_Jason.setDirection(DOWN)
                elif event.key == pygame.K_a:
                    snake_Jason.setDirection(LEFT)
                elif event.key == pygame.K_d:
                    snake_Jason.setDirection(RIGHT)

       # snake_Eddie.autonomous(normalApple)
        snake_Jason.autonomous(superApple)

        snake_Eddie.move()           # Move your snake to next position
        snake_Jason.move()

        if snake_Jason.isCollision(snake_Eddie.snakePos):
            font = pygame.font.SysFont("comicsansms", 72)
            text = font.render("Red Wins", True, (0, 128, 0))
            screen.blit(text, (10, 150))
            pygame.display.flip()
            pygame.time.wait(2000)
            carryOn = False

        if snake_Eddie.isCollision(snake_Jason.snakePos):
            font = pygame.font.SysFont("comicsansms", 72)
            text = font.render("Blue Wins", True, (0, 128, 0))
            screen.blit(text, (10, 150))
            pygame.display.flip()
            pygame.time.wait(2000)
            carryOn = False


        # eat apples
        if snake_Eddie.grow(normalApple) or snake_Jason.grow(normalApple):
            normalApple.getRandApplePos()
        if snake_Eddie.grow(superApple) or snake_Jason.grow(superApple):
            superApple.getRandApplePos()



        # Drawing section
        screen.blit(myImage,(0, 0));           # Set background color to white and clear the screen
        pygame.draw.circle(screen, RED, (normalApple.x + 5, normalApple.y + 5), 5, 0)  # Draw apple
        pygame.draw.circle(screen, BLUE, (superApple.x + 5, superApple.y + 5), 5, 0)  # Draw apple
        snake_Eddie.draw(screen)
        snake_Jason.draw(screen)


        score1 = len(snake_Eddie.snakePos)-1
        disclaimertext = myfont.render("Some disclaimer...", 1, (155, 155, 155))
        screen.blit(disclaimertext, (5, 480))

        score1text = myfont.render("Red Score {0}".format(score1), 1, (0, 0, 0))
        screen.blit(score1text, (5, 10))
#/////////////////////////////////////////////////////////////////////////////
        score = len(snake_Jason.snakePos) - 1
        disclaimertext = myfont.render("Some disclaimer...", 1, (155, 155, 155))
        screen.blit(disclaimertext, (5, 480))

        scoretext = myfont.render("Blue Score {0}".format(score), 1, (0, 0, 0))
        screen.blit(scoretext, (5, 30))




        pygame.display.flip()              # pygame.display.update() PyGame is double-buffered. This swaps the buffers. All you need to know is that this call is required in order for any updates that you make to the game screen to become visible.

        currentTime = time.time()

        if currentTime - start > 30:
            carryOn = False

        clock.tick(15)                     # unit in Hz, can be used for speed control

    if score1 > score:
        font = pygame.font.SysFont("comicsansms", 72)
        text = font.render("Red Wins", True, (0, 128, 0))
        screen.blit(text, (10, 150))
        pygame.display.flip()
        pygame.time.wait(2000)
        carryOn = False

    if score > score1:
        font = pygame.font.SysFont("comicsansms", 72)
        text = font.render("Blue Wins", True, (0, 128, 0))
        screen.blit(text, (10, 150))
        pygame.display.flip()
        pygame.time.wait(2000)
        carryOn = False

    pygame.quit()


main()