# Constant & enum
UP = 0
DOWN = 3
LEFT = 1
RIGHT = 2
HEIGHT = 490
WIDTH = 490
class Snake(object):
    def __init__(self):
        self.snakePos = [(50, 50), (60, 50)]
        self.direction = RIGHT

    def setDirection(self, dir_):
        if self.direction == RIGHT and dir_ != LEFT:
            self.direction = dir_
        elif self.direction == LEFT and dir_ != RIGHT:
            self.direction = dir_
        elif self.direction == UP and dir_ != DOWN:
            self.direction = dir_
        elif self.direction == DOWN and dir_ != UP:
            self.direction = dir_

        #if self.direction + dir_ != 3:
            #self.direction = dir_

    def getNextHead(self):
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
        return (positionX, positionY)

    def move(self):
        self.snakePos.insert(0, self.getNextHead())
        self.snakePos.pop()

    def isEatApple(self, pos):

        if self.snakePos[0] == pos:                        # when snake head overlap with apple
            self.snakePos.append(self.snakePos[-1])        # Grow

            return True
        else:
            return False
    def isCollision(self):
        head = self.snakePos[0]
        if head[0] > WIDTH or head[0] < 0:
            return True
        if head[1] > HEIGHT or head[1] < 0:
            return True
        return False


