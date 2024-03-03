import pygame   # this is of course needed to access the PyGame framework.
import random
import Snake_class
from pygame.locals import *
# Initialization pygame
HEIGHT = 500
WIDTH = 500
# Color definition
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

BackGround = Background('running.jpg', [0,0])


def getRandApplePos():
    appleX = random.randint(0, WIDTH / 10 - 1) * 10
    appleY = random.randint(0, HEIGHT / 10 - 1) * 10
    return (appleX, appleY)



def main():
    pygame.init()
    pygame.mixer.music.load('Running in the 90s.mp3')
    pygame.mixer.music.play(-1)
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("My Snake Game")
    clock = pygame.time.Clock()
    # Initial Snake & Apple
    applePos = getRandApplePos()
    snake_Harold = Snake_class.Snake()
    isCollision = snake_Harold.isCollision()
    carryOn = True 
    while carryOn:       # main time control loop
        # pygame.mixer.music.load('Running in the 90s.mp3')
        # pygame.mixer.music.play(-1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                carryOn = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake_Harold.setDirection(Snake_class.LEFT)
                elif event.key == pygame.K_RIGHT:
                    snake_Harold.setDirection(Snake_class.RIGHT)
                elif event.key == pygame.K_UP:
                    snake_Harold.setDirection(Snake_class.UP)
                elif event.key == pygame.K_DOWN:
                    snake_Harold.setDirection(Snake_class.DOWN)
        snake_Harold.move()

        if snake_Harold.isEatApple(applePos) is True:  # when snake head overlap with apple
            applePos = getRandApplePos()

        # Drawing section
        screen.fill(WHITE)

        screen.blit(BackGround.image, BackGround.rect)
        for point in snake_Harold.snakePos:
            pygame.draw.rect(screen, BLUE, [point, (10, 10)], 0)
        pygame.draw.circle(screen, RED, (applePos[0] + 5, applePos[1] + 5), 5, 0)

        pygame.display.flip()
        if snake_Harold.isCollision():
            carryOn = False


        clock.tick(50)

    pygame.quit()


main()
