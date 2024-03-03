import pygame
import random
HEIGHT=500
WIDTH=500*2
#GoldAppleTimer=700
###############################################################################################################################################################################################
SNAKE_WIDTH=10
snakePos=[(30+SNAKE_WIDTH,30),(30,30)]
###############################################################################################################################################################################################
class Apple (object):
    def __init__(self, startX, startY, Color, Timer = 0):
        self.appleX=startX
        self.appleY=startY
        self.color=Color
        self.timer=Timer

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, [(self.appleX,self.appleY), (SNAKE_WIDTH, SNAKE_WIDTH)], 0)

    def randomizeApple(self):
        self.appleX=random.randint(0, WIDTH-SNAKE_WIDTH)
        self.appleY=random.randint(0, HEIGHT-SNAKE_WIDTH)
        while not self.appleX%SNAKE_WIDTH == 0:
            self.appleX=random.randint(0, WIDTH-SNAKE_WIDTH)
        while not self.appleY%SNAKE_WIDTH == 0:
            self.appleY=random.randint(0, HEIGHT-SNAKE_WIDTH)

    def checkIfEaten(self, otherSnakePos):
        if otherSnakePos[0]==(self.appleX,self.appleY):
            return True
        return False

    def changeTimer(self):
        self.timer -= 1
        if self.timer < -200:
            self.timer = 400
###############################################################################################################################################################################################
class Snake (object):
    def __init__(self, startingPos, dic):
        self.snakePos = [(startingPos[0]+SNAKE_WIDTH,startingPos[1]),(startingPos)]
        self.facing = dic
        self.grow=0
        self.wait=0
        self.dead=False
        self.length=len(self.snakePos)
        self.invincible=0

    def changeDic(self, direction):
        if self.wait==0:
            self.facing = direction

    def move(self):
        if self.wait==0:
            x=self.snakePos[0][0]
            y=self.snakePos[0][1]

            if self.facing==LEFT and x > 0: #LEFT
                x -= SNAKE_WIDTH
            if self.facing==RIGHT and x < WIDTH-SNAKE_WIDTH: #RIGHT
                x += SNAKE_WIDTH
            if self.facing==UP and y > 0: #DOWN
                y -= SNAKE_WIDTH
            if self.facing==DOWN and y < HEIGHT-SNAKE_WIDTH: #UP
                y += SNAKE_WIDTH

            self.snakePos.insert(0, (x,y))
            self.snakePos.pop()
        else:
            self.wait-=1
            if self.wait == 0:
                self.invincible=12

    def isCollision(self, anotherSnake):
        if self.snakePos[0] in self.snakePos[1:] or self.snakePos[0] in anotherSnake:
            return True
        return False

    def ifEatingApple(self,ApplePos):
        head = self.snakePos[0]
        if head==(ApplePos):
            self.grow += 80
        if self.grow > 0:
            self.snakePos.append(self.snakePos[-1])
            self.grow-=1

    def draw(self, screen, color):
        for point in self.snakePos:
            pygame.draw.rect(screen, color, [point, (SNAKE_WIDTH, SNAKE_WIDTH)], 0)

    def respawn(self,restartPos,restartDic,anotherSnake):
        self.length=len(self.snakePos)-2
        if self.invincible > 0:
            self.invincible-=1
        if self.isCollision(anotherSnake):
            self.invincible = 2
        if self.dead:
            self.snakePos = restartPos
            self.facing = restartDic
            if not self.wait > 0:
                self.wait = 30
            self.grow //= 2
            for i in range(self.length//2):
                self.snakePos.append(restartPos[1])
            self.dead=False
###############################################################################################################################################################################################
BLACK=(0,0,0)
GOLD=(255,205,0)
YELLOW=(255,230,0)
RED=(255,0,0)
GREEN=(124,252,0)
###############################################################################################################################################################################################
facing=3
UP=0
DOWN=1
LEFT=2
RIGHT=3
###############################################################################################################################################################################################
def main():
    snakeScreen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.init()
    carryOn = True
###############################################################################################################################################################################################
    snakeySnake = Snake((0,0), RIGHT)
    pythonyPython = Snake((WIDTH-SNAKE_WIDTH*2,HEIGHT-SNAKE_WIDTH), LEFT)
###############################################################################################################################################################################################
    global GoldAppleTimer
    snakeGoldApple = Apple(0,HEIGHT//2, GOLD, 300)
    pythonGoldApple = Apple(WIDTH-SNAKE_WIDTH,HEIGHT//2, GOLD, 600)
    normalApple = Apple(30,30, RED)
    normalApple.randomizeApple()
###############################################################################################################################################################################################
    clock=pygame.time.Clock()
    while carryOn:
        snakeGoldApple.changeTimer()
        pythonGoldApple.changeTimer()
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                carryOn = False
                keys=pygame.key.get_pressed()
            elif event.type==pygame.KEYDOWN:
                if event.key == pygame.K_UP and snakeySnake.facing != DOWN:
                    snakeySnake.changeDic(UP) 
                if event.key == pygame.K_LEFT and snakeySnake.facing != RIGHT:
                    snakeySnake.changeDic(LEFT)
                if event.key == pygame.K_RIGHT and snakeySnake.facing !=LEFT:
                    snakeySnake.changeDic(RIGHT)
                if event.key == pygame.K_DOWN and snakeySnake.facing != UP:
                    snakeySnake.changeDic(DOWN)

                if event.key == pygame.K_w and pythonyPython.facing != DOWN:
                    pythonyPython.changeDic(UP) 
                if event.key == pygame.K_a and pythonyPython.facing != RIGHT:
                    pythonyPython.changeDic(LEFT)
                if event.key == pygame.K_d and pythonyPython.facing !=LEFT:
                    pythonyPython.changeDic(RIGHT)
                if event.key == pygame.K_s and pythonyPython.facing != UP:
                    pythonyPython.changeDic(DOWN)
###############################################################################################################################################################################################
        snakeySnake.move()
        snakeySnake.ifEatingApple((normalApple.appleX, normalApple.appleY))
        pythonyPython.move()
        pythonyPython.ifEatingApple((normalApple.appleX, normalApple.appleY))
        if pythonyPython.snakePos[0] == (normalApple.appleX, normalApple.appleY) or snakeySnake.snakePos[0] == (normalApple.appleX, normalApple.appleY):
            normalApple.randomizeApple()
###############################################################################################################################################################################################
        snakeScreen.fill(BLACK)
        if snakeySnake.wait%6<=2 and snakeySnake.invincible%6<=2:
            snakeySnake.draw(snakeScreen, YELLOW)
        if pythonyPython.wait%6<=2 and pythonyPython.invincible%6<=2:
            pythonyPython.draw(snakeScreen, GREEN)
###############################################################################################################################################################################################
        normalApple.draw(snakeScreen)
        if snakeGoldApple.timer < 0:
            snakeGoldApple.draw(snakeScreen)
        if pythonGoldApple.timer < 0:
            pythonGoldApple.draw(snakeScreen)
###############################################################################################################################################################################################
        clock.tick(50) #I am able to change the snakes speed here#
###############################################################################################################################################################################################
        pygame.display.flip()
###############################################################################################################################################################################################
        if snakeGoldApple.checkIfEaten(pythonyPython.snakePos) and snakeGoldApple.timer < 0:
            font = pygame.font.SysFont("comicsansms", 72)
            text = font.render("Python wins!", True, (255, 255, 255))
            snakeScreen.blit(text, (10, 150))
            pygame.display.flip()
            carryOn=False

        if pythonGoldApple.checkIfEaten(snakeySnake.snakePos) and pythonGoldApple.timer < 0:
            font = pygame.font.SysFont("comicsansms", 72)
            text = font.render("Snake wins!", True, (255, 255, 255))
            snakeScreen.blit(text, (10, 150))
            pygame.display.flip()
            carryOn=False

        if snakeySnake.isCollision(pythonyPython.snakePos) and not snakeySnake.invincible > 0 :
            snakeySnake.dead=True

        if pythonyPython.isCollision(snakeySnake.snakePos) and not pythonyPython.invincible > 0:
            pythonyPython.dead=True

        snakeySnake.respawn([(10,0),(0,0)], RIGHT,pythonyPython.snakePos)
        pythonyPython.respawn([(WIDTH-SNAKE_WIDTH*2,HEIGHT-SNAKE_WIDTH),(WIDTH-SNAKE_WIDTH,HEIGHT-SNAKE_WIDTH)], LEFT,snakeySnake.snakePos)

        #DEBUG
        #print(GoldAppleTimer)
        #print(snakeySnake.wait)
        #print(pythonGoldApple.timer)
        #print(snakeGoldApple.timer)
        #print(snakeySnake.invincible)
###############################################################################################################################################################################################
main()
