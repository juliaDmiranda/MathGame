from enum import Enum, auto
from random import randrange, choice


class LEVEL(Enum):
    '''
    Why? I don't know if in the future someone will use 
    this code and try to change the way to represent the levels.
    Thou, this is the most obvous way to represente what will 
    represent variables.
    '''
    EASY    = auto()
    NORMAL  = auto()
    MEDIUM  = auto()
    HARD    = auto()

class Game:
    '''
    This class will store the currently status of a round
    '''
    player_name = ''
    scores      = 0
    level       = ''
    result      = 0
    operations = ['-','+','-','*','/']
    def newQuestion(self):
        try:
            if(self.level == LEVEL.EASY): 
                text = str(randrange(11)) + str(choice(self.operations)) + str(randrange(11))
                self.result = eval(text)
                return text
            elif(self.level == LEVEL.NORMAL):
                text = str(randrange(10, 101)) + str(choice(self.operations)) + str(randrange(10, 101))
                self.result = eval(text)
                return text
            elif(self.level == LEVEL.MEDIUM):
                text = str(randrange(100, 1001)) + str(choice(self.operations)) + str(randrange(100, 1001))
                self.result = eval(text)
                return text

            elif(self.level == LEVEL.HARD):
                text = str(randrange(1000, 10001)) + str(choice(self.operations)) + str(randrange(1000, 10001))
                self.result = eval(text)
                return text
        except ZeroDivisionError:
            self.newQuestion()
ame = Game()
ame.newQuestion()
ame.newQuestion()
ame.newQuestion()
ame.newQuestion()


