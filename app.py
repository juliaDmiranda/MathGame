import sys
from ui.screen1 import *
from ui.screen2 import *
from ui.screen3 import *
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.Qt import QPixmap, QIcon, QDialog
import pathlib
from GameClass import Game, LEVEL
from functools import partial
from time import sleep
manager = Game()
class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("ui/screen1.ui", self)
        self.setWindowTitle("MATH GAME")
        self.bgLabel.setPixmap(QPixmap('images/bg/main.png'))
        self.bgLabel.setScaledContents(True) 

        self.playNowButton.clicked.connect(self.gotoLevels)
        self.helpButton.clicked.connect(self.gotoHelp)

    def gotoLevels(self):
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gotoHelp(self):
        widget.setCurrentIndex(widget.currentIndex()+2)
        
class HelpWindow(QDialog):
    def __init__(self):
        super(HelpWindow, self).__init__()
        loadUi("ui/screen4.ui", self)
        self.setWindowTitle("MATH GAME")

        self.menuButton.clicked.connect(self.gotoMain)

    def gotoMain(self):
        widget.setCurrentIndex(widget.currentIndex()-2)

class LevelsWindow(QDialog):

    def __init__(self):
        super(LevelsWindow, self).__init__()
        loadUi("ui/screen2.ui", self)
        self.setWindowTitle("MATH GAME")
        self.bgLabel.setPixmap(QPixmap('images/bg/main.png'))
        self.bgLabel.setScaledContents(True)

        self.menuButton.clicked.connect(self.gotoMain)
        self.easyButton.clicked.connect(partial(self.chooseLevel, LEVEL.EASY))
        self.normalButton.clicked.connect(partial(self.chooseLevel, LEVEL.NORMAL))
        self.mediumButton.clicked.connect(partial(self.chooseLevel, LEVEL.MEDIUM))
        self.hardButton.clicked.connect(partial(self.chooseLevel, LEVEL.HARD))

    def chooseLevel(self, level):
        manager.level = level
        gameW = GameWindow()
        gameW.questionLabel.setText(manager.newQuestion())
        widget.addWidget(gameW)

        widget.setCurrentIndex(widget.currentIndex()+2)
        
    def gotoMain(self):
        widget.setCurrentIndex(widget.currentIndex()-1)


class GameWindow(QDialog):

    def __init__(self):
        super(GameWindow, self).__init__()
        loadUi("ui/screen3.ui", self)
        self.setWindowTitle("MATH GAME")
        self.menuButton.clicked.connect(self.gotoMain)
        self.checkAnswerButton.clicked.connect(self.checkAnswer)

    def exec(self):
        '''
        DIDN'T WORKED!
        '''
        # this method will be executed every time the dialog is executed (i.e., shown)
        self.my_method()
        super().exec()
    
    def my_method(self):
        self.questionLabel.setText("PERFEITO")

    def gotoMain(self):
        manager.scores = 0
        self.scoreLabel.setText(str(manager.scores))
        widget.setCurrentIndex(widget.currentIndex()-3)
        
        widget.removeWidget(self)

    def checkAnswer(self):
        try:
            if int(manager.result) == int(self.lineEdit.text()):
                self.questionLabel.setText("You are right!")
                self.updateScore()
    
            else:
                if isinstance(manager.result, float):
                    manager.result = "{:.2f}".format(manager.result)
                self.questionLabel.setText(f"No, {manager.result}.")
            
            self.lineEdit.setText("")
            QtCore.QTimer.singleShot(2000, lambda: self.questionLabel.setText(manager.newQuestion()))
        except:
            self.questionLabel.setText(manager.newQuestion())

    def updateScore(self):
        manager.scores +=10
        
        self.scoreLabel.setText(str(manager.scores))

if __name__ == '__main__':
    qt = QApplication(sys.argv)
    widget=QtWidgets.QStackedWidget()
    widget.addWidget(MainWindow())
    widget.addWidget(LevelsWindow())
    widget.addWidget(HelpWindow())
    # widget.addWidget(GameWindow())
    widget.setFixedWidth(591)
    widget.setFixedHeight(441)
    # new = MainWindow()
    widget.show()
    qt.exec_()
    
