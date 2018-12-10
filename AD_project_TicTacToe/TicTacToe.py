from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLineEdit, QToolButton, QComboBox
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtWidgets import QLayout, QGridLayout

from time import sleep
from ai import AI

class Button(QToolButton):

    def __init__(self, callback):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.clicked.connect(callback)

        font = self.font()
        font.setFamily("Curier New")
        font.setBold(True)
        font.setPointSize(30)
        self.setFont(font)

    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(70)
        size.setWidth(size.height())
        return size


class TicTacToe(QWidget):

    def __init__(self, parent=None):
        self.turn = 0
        super().__init__(parent)

        self.current = [[-1] * 3 for i in range(3)]
        
        # Display Window
        self.display = QLineEdit("Your Turn!")
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignHCenter)
        font = self.display.font()
        font.setPointSize(15)
        font.setFamily("Curier New")
        self.display.setFont(font)

        # game grid create
        gameLayout = QGridLayout()
        self.Buttons = [[] * 3 for i in range(3)]
        for row in range(3):
            for col in range(3):
                self.Buttons[row].append(Button(self.gameButtonClicked))
                gameLayout.addWidget(self.Buttons[row][col], row, col)

        # AI level comboBox
        self.qb = QComboBox()
        self.qb.addItem("easy")
        self.qb.addItem("normal")
        self.qb.addItem("hard")
        self.qb.currentTextChanged.connect(self.gameStart)
        self.ai = AI(self.qb.currentText())

        # Button for a new game
        self.newGameButton = QToolButton()
        self.newGameButton.setText("New Game")
        self.newGameButton.clicked.connect(self.gameStart)

        # Layout
        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)
        mainLayout.addWidget(self.display, 0, 0, 1, 2)
        mainLayout.addLayout(gameLayout, 1, 0, 1, 2)
        mainLayout.addWidget(self.qb, 2, 0, 1, 1)
        mainLayout.addWidget(self.newGameButton, 2, 1, 1, 1)

        self.setLayout(mainLayout)

        self.setWindowTitle("Tic Tac Toe")

        self.gameStart()

    def gameButtonClicked(self):
        # User Turn
        clickedButton = self.sender()
        clickedButton.setText("O")
        clickedButton.setStyleSheet('QToolButton{color: blue;}')
        clickedButton.setEnabled(False)
        self.setCurrent()

        if self.gameEnd() == 0:
            self.display.setText("You Win!!")
            self.display.setStyleSheet('QLineEdit{color: blue;}')
            for r in range(3):
                for c in range(3):
                    self.Buttons[r][c].setEnabled(False)
            return

        self.turn += 1
        self.display.setText("Turn : " + str(self.turn))
        if self.turn == 5:
            self.display.setText("Draw!")
            return

        # AI Turn
        self.setCurrent()
        row, col = self.ai.guess(self.current, self.turn)
        self.Buttons[row][col].setText("X")
        self.Buttons[row][col].setStyleSheet('QToolButton{color: red;}')
        self.Buttons[row][col].setEnabled(False)
        self.setCurrent()

        if self.gameEnd() == 1:
            self.display.setText("AI Win!!")
            self.display.setStyleSheet('QLineEdit{color: red;}')
            for r in range(3):
                for c in range(3):
                    self.Buttons[r][c].setEnabled(False)
            return

    def gameStart(self):
        self.display.setText("Your Turn!")
        self.display.setStyleSheet('QLineEdit{color: black;}')
        self.ai = AI(self.qb.currentText())
        self.setCurrent()
        self.turn = 0

        for row in range(3):
            for col in range(3):
                self.Buttons[row][col].setText("")
                self.Buttons[row][col].setEnabled(True)

    def setCurrent(self):
        for row in range(3):
            for col in range(3):
                text = self.Buttons[row][col].text()
                if text == "O":
                    self.current[row][col] = 0
                elif text == "X": 
                    self.current[row][col] = 1
                else:
                    self.current[row][col] = -1

    def gameEnd(self):
        horizonRepeatNum  = [[0, 0] for i in range(3)]
        verticalRepeatNum = [[0, 0] for i in range(3)]
        diagonalRepeatNum = [[0, 0] for i in range(2)]

        # get RepeatNum
        for row in range(3):
            for col in range(3):
                currentValue = self.current[row][col]
                if currentValue == -1:
                    continue

                horizonRepeatNum[row][currentValue]    += 1
                verticalRepeatNum[col][currentValue]   += 1

                if row == col:
                    diagonalRepeatNum[0][currentValue] += 1
                if row == 2 - col:
                    diagonalRepeatNum[1][currentValue] += 1

        for i in range(3):
            if horizonRepeatNum[i][0] == 3 or verticalRepeatNum[i][0] == 3 or diagonalRepeatNum[0][0] == 3 or diagonalRepeatNum[1][0] == 3:
                return 0
            elif horizonRepeatNum[i][1] == 3 or verticalRepeatNum[i][1] == 3 or diagonalRepeatNum[0][1] == 3 or diagonalRepeatNum[1][1] == 3:
                return 1

        return -1

if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    game = TicTacToe()
    game.show()
    sys.exit(app.exec_())

