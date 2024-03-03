import pygame
import random

HEIGHT = 700  # rows- 35
WIDTH = 1300  # columns- 65
SCALE = 20

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

WHITE = (255, 255, 255) # CORVETTE IS WHITE
RED = (255, 0, 0)
GREEN = (0, 255, 0) # CAMERO IS GREEN
BLUE = (0, 10, 255)
BLACK = (0, 0, 0)

class Snake(object):
    def __init__(self, startingPos, rgb=BLACK):  # rgb = BLACK is a defalt color for the snake.
        self.snakePos = [startingPos]
        self.direction = RIGHT
        self.color = rgb

    def setDirection(self, dir):
        if self.direction == RIGHT and dir != LEFT and dir != RIGHT:
            self.direction = dir
            return True
        if self.direction == LEFT and dir != RIGHT and dir != LEFT:
            self.direction = dir
            return True
        if self.direction == UP and dir != DOWN and dir != UP:
            self.direction = dir
            return True
        if self.direction == DOWN and dir != UP and dir != DOWN:
            self.direction = dir
            return True
        return False

    # def autonomous(self, apple):
    #     if apple.x > self.snakePos[0][0] and self.setDirection(RIGHT):
    #         return
    #     if apple.x < self.snakePos[0][0] and self.setDirection(LEFT):
    #         return
    #     if apple.x > self.snakePos[0][1] and self.setDirection(DOWN):
    #         return
    #     if apple.x < self.snakePos[0][1] and self.setDirection(UP):
    #         return


    def move(self):
        positionX = self.snakePos[0][0]
        positionY = self.snakePos[0][1]

        if self.direction == UP:
            positionY -= SCALE
        elif self.direction == DOWN:
            positionY += SCALE
        elif self.direction == LEFT:
            positionX -= SCALE
        elif self.direction == RIGHT:
            positionX += SCALE

        self.snakePos.insert(0, (positionX, positionY))
        self.snakePos.pop()  # Remove tail

    def isCollision(self, anotherSnakePos):
        head = self.snakePos[0]  # head = (x, y)
        if head[0] < 0 or head[0] >= WIDTH:  # head[0] = x value
            return True
        if head[1] < 0 or head[1] >= HEIGHT:  # head[1] = y value
            return True
        if head in self.snakePos[1:]:
            return True
        if head in anotherSnakePos:
            return True
        return False

    def draw(self, screen):
        for point in self.snakePos:
            pygame.draw.rect(screen, self.color, [point, (SCALE, SCALE)], 0)

    def grow(self, appleMatrix):
        x = self.snakePos[0][0] // SCALE
        y = self.snakePos[0][1] // SCALE

        if appleMatrix[x][y] == 1:
            #self.point += 1
            appleMatrix[x][y] = 0
            pass
        elif appleMatrix[x][y] == 2:
            #self.point += 10
            appleMatrix[x][y] = 0
            self.snakePos.append(self.snakePos[-1])  # tail position


def getRandApplepos():
    appleX = random.randint(0, WIDTH / SCALE - 1) * SCALE
    appleY = random.randint(0, HEIGHT / SCALE - 1) * SCALE
    return (appleX, appleY)


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("SNAKE GAME")
    clock = pygame.time.Clock()
    snake_Corvette = Snake((5 * SCALE, 5 * SCALE), WHITE)
    snake_Camero = Snake((6 * SCALE, 6 * SCALE), GREEN)

    appleMatrix = [[1 for x in range(HEIGHT // SCALE)] for y in range(WIDTH // SCALE)]   # 0 = no apple, 1 = red apple (points only), 2 = green apple (growth)
    for i in range(10):
        appleMatrix[random.randint(0, WIDTH / SCALE - 1)][random.randint(0, HEIGHT / SCALE - 1)] = 2
    # applePos = getRandApplepos()

    carryOn = True
    while carryOn:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                carryOn = False
            elif event.type == pygame.KEYDOWN:  # keys = pygame.key.get_pressed()
                if event.key == pygame.K_LEFT:
                    snake_Corvette.setDirection(LEFT)
                elif event.key == pygame.K_RIGHT:
                    snake_Corvette.setDirection(RIGHT)
                elif event.key == pygame.K_UP:
                    snake_Corvette.setDirection(UP)
                elif event.key == pygame.K_DOWN:
                    snake_Corvette.setDirection(DOWN)
                if event.key == pygame.K_w:
                    snake_Camero.setDirection(UP)
                elif event.key == pygame.K_s:
                    snake_Camero.setDirection(DOWN)
                elif event.key == pygame.K_a:
                    snake_Camero.setDirection(LEFT)
                elif event.key == pygame.K_d:
                    snake_Camero.setDirection(RIGHT)

        snake_Corvette.move()
        snake_Camero.move()

        if snake_Corvette.isCollision(snake_Camero.snakePos) or snake_Camero.isCollision(snake_Corvette.snakePos):
            font = pygame.font.SysFont("comicsansms", 150)
            text = font.render("Game Over", True, (0, 128, 0))
            screen.blit(text, (520, 350))
            pygame.display.flip()
            pygame.time.wait(2000)
            carryOn = False

        snake_Corvette.grow(appleMatrix)
        snake_Camero.grow(appleMatrix)

        screen.fill(BLACK)

        # pygame.draw.circle(screen, RED, (applePos[0] + SCALE//2, applePos[1] + SCALE//2), SCALE//2, 0)

        for w in range(WIDTH // SCALE):
            for h in range(HEIGHT // SCALE):
                if appleMatrix[w][h] == 1:
                    pygame.draw.circle(screen, RED, (w * SCALE + SCALE // 2, h * SCALE + SCALE // 2), SCALE // 2, 0)
                if appleMatrix[w][h] == 2:
                    pygame.draw.circle(screen, BLUE, (w * SCALE + SCALE // 2, h * SCALE + SCALE // 2), SCALE // 2, 0)

        snake_Corvette.draw(screen)
        snake_Camero.draw(screen)

        pygame.display.flip()
        clock.tick(15)
    pygame.quit()


main()