import pygame
import random
HEIGHT = 600
WIDTH = 600
UP = 0 
DOWN  = 1
LEFT = 2
RIGHT = 3
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
YELLOW = (255,255,0)
WHITE = (255, 255, 255)
PINK = (255, 0, 247)
BLACK = (0, 0, 0)
point2 = (1,1)

########################################################################################## START OF CLASS
class Snake(object):
    def __init__(self, startingPos, rgb = BLUE):
        self.snakePos = [startingPos]
        self.direction = RIGHT #Up = 0 DOWN = 1, LEFT = 2, RIGHT = 3
        self.color = rgb
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def setDirection(self, dir):
        if self.direction == RIGHT and dir != LEFT:
            self.direction = dir
        if self.direction == LEFT and dir != RIGHT:
            self.direction = dir
        if self.direction == UP and dir != DOWN:
            self.direction = dir
        if self.direction == DOWN and dir!= UP:
            self.direction = dir
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def move(self):
        positionX = self.snakePos[0][0] #initial X
        positionY = self.snakePos[0][1] #initial Y
    
            # your code goes here
        if self.direction == UP: #Up
            positionY -= 10
        elif self.direction == DOWN: #DOWN
            positionY += 10
        elif self.direction == LEFT:
            positionX -= 10
        elif self.direction == RIGHT:
            positionX += 10

        self.snakePos.insert(0, (positionX, positionY))
        self.snakePos.pop()
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #def autonomus(self, apple):
            #if apple.x > self.snakePos[0][0]:
               # if self.setDirection(RIGHT):
                   # return
            #if apple.x < self.snakePos[0][0]:
               # if self.setDirection(LEFT):
                #    return
           # if apple.y > self.snakePos[0][1]:
                #if self.setDirection(DOWN):
                  #  return
           # if apple.y < self.snakePos[0][1]:
                # if self.setDirection(DOWN):
                   # return
           # if apple.y < self.snakePos[0][1]:
                 #if self.setDirection(UP):
                    #return

            
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------

    
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def isCollision(self, anotherSnakePos):
        head = self.snakePos[0]
        if head[0] < 0 or head[0] >= WIDTH: #head[0] = x
            print("Game over")
            return True
            
        if head[1] < 0 or head[1] >= HEIGHT:
            print("Game over")
            return True

        

        if head in self.snakePos[1:] :
            print("Game over")
            return True
# If touch another snake
        if head in anotherSnakePos:
            return True
        return False
            
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------        
    def draw(self, screen):
        for point in self.snakePos:
            pygame.draw.rect(screen, self.color , [point, (10, 10)])

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------

    #Growth
    def grow(self, applePos):
         if self.snakePos[0] == applePos:
            applePos = getRandApplePos()
            
            self.snakePos.append(self.snakePos[-1])
            return True
         else:
            return False

########################################################### END OF CLASS

def getRandApplePos():
    appleX = random.randint(0, WIDTH / 10 - 1) * 10
    appleY = random.randint(0, HEIGHT / 10 - 1) * 10
    return (appleX, appleY)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
def main():
    pygame.init()
    #RGB(Red, Green, Blue)
    snake1 = Snake( (350,350), GREEN )
    snake2 = Snake( (400, 450) )


    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake Game")
    clock = pygame.time.Clock()
    carryOn = True

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------

    # Initial Apple Description
    applePos = getRandApplePos()
    
    # Background picture
    backgroundImg = pygame.image.load('BG.jpg')
    
    while carryOn:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                carryOn = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                snake1.setDirection(LEFT)
            elif keys[pygame.K_RIGHT]:
                snake1.setDirection(RIGHT)
            elif keys[pygame.K_UP]:
                snake1.setDirection(UP)
            elif keys[pygame.K_DOWN]: 
                snake1.setDirection(DOWN)
            elif keys[pygame.K_a]:
                snake2.setDirection(LEFT)
            elif keys[pygame.K_d]:
                snake2.setDirection(RIGHT)
            elif keys[pygame.K_w]:
                snake2.setDirection(UP)
            elif keys[pygame.K_s]:
                snake2.setDirection(DOWN)
        score = len(snake1.snakePos)
       # snake2.autonomus(applePos)
            
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
        snake1.move()  # Move
        snake2.move()

        if snake2.isCollision(snake1.snakePos) or snake1.isCollision(snake2.snakePos):
                font =  pygame.font.SysFont("comicsansms", 72)
                text = font.render("Game Over", True, (0, 128, 0))
                screen.blit(text, (10, 150))
                pygame.display.flip()
                pygame.time.wait(2000)
                carryOn = False


    
    
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
        
        # eat apple
        if snake1.grow(applePos) is True or snake2.grow(applePos):
            applePos = getRandApplePos()
        #if snake2.grow(applePos) is True:
            #applePos = getRandApplePos()

#------------------- Drawing Section -------------------------
        #screen.fill(BLACK)
        screen.blit(backgroundImg, (0, 0));
        #resize
        backgroundImg = pygame.transform.scale(backgroundImg, (620, 620))
        snake1.draw(screen)
        snake2.draw(screen)

        pygame.draw.circle(screen,RED , (applePos[0] + 5, applePos[1] + 5), 5, 0)
        pygame.display.flip()
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
        

      
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------   
        
        print(len(snake1.snakePos))

        #scoretext = myfont.render("Score = "+str(score), 1, (0,0,0))
        
        clock.tick(20)
        

    
    pygame.quit()


    
main()
