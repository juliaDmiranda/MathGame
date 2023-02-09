import sys
from ui.screen1 import *
from ui.screen2 import *
from ui.screen3 import *
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.Qt import QPixmap, QIcon, QDialog
import pathlib

class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("ui/screen1.ui", self)
        self.setWindowTitle("MATH GAME")
        self.bgLabel.setPixmap(QPixmap('imgs/bg/main.png'))
        self.bgLabel.setScaledContents(True) 

        self.playNowButton.clicked.connect(self.gotoLevels)
        self.helpButton.clicked.connect(self.gotoHelp)

    def gotoLevels(self):
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gotoHelp(self):
        widget.setCurrentIndex(widget.currentIndex()+3)
        
class HelpWindow(QDialog):
    def __init__(self):
        super(HelpWindow, self).__init__()
        loadUi("ui/screen4.ui", self)
        self.setWindowTitle("MATH GAME")

        self.menuButton.clicked.connect(self.gotoMain)

    def gotoMain(self):
        widget.setCurrentIndex(widget.currentIndex()-3)

class LevelsWindow(QDialog):
    def __init__(self):
        super(LevelsWindow, self).__init__()
        loadUi("ui/screen2.ui", self)
        self.setWindowTitle("MATH GAME")
        self.bgLabel.setPixmap(QPixmap('imgs/bg/main.png'))
        self.bgLabel.setScaledContents(True)

        self.menuButton.clicked.connect(self.gotoMain)
        self.easyButton.clicked.connect(self.chooseLevel)
        self.normalButton.clicked.connect(self.chooseLevel)
        self.mediumButton.clicked.connect(self.chooseLevel)
        self.hardButton.clicked.connect(self.chooseLevel)

    def chooseLevel(self):
        widget.setCurrentIndex(widget.currentIndex()+1)
    def gotoMain(self):
        widget.setCurrentIndex(widget.currentIndex()-1)

class GameWindow(QDialog):
    # scores = 0
    def __init__(self):
        super(GameWindow, self).__init__()
        loadUi("ui/screen3.ui", self)
        self.setWindowTitle("MATH GAME")
        self.menuButton.clicked.connect(self.gotoMain)

    def gotoMain(self):
        widget.setCurrentIndex(widget.currentIndex()-2)

    def checkAnswer(self):
        if True:
            # Show a motivational phrase and congratulatin the player
             
            width = int(self.inputWidth.text())

            self.updateScore()
        else:
            # Show a motivational phrase
            print("Try again!")
            pass

    def updateScore(self):
        # this event only occor after pressing the check button and if the ansewr is corretc.
        score = 0
        score+=10
        self.scoreLabel.setText(str(self.scoreLabel.test + 10))
    


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    widget=QtWidgets.QStackedWidget()
    widget.addWidget(MainWindow())
    widget.addWidget(LevelsWindow())
    widget.addWidget(GameWindow())
    widget.addWidget(HelpWindow())
    widget.setFixedWidth(591)
    widget.setFixedHeight(441)
    # new = MainWindow()
    widget.show()
    qt.exec_()