from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit
from PyQt5.QtWidgets import QLayout, QGridLayout
from PyQt5.QtWidgets import QWidget,QPushButton,QHBoxLayout,QVBoxLayout,QApplication,QLabel,QComboBox,QTextEdit,QLineEdit
from PyQt5 import QtCore
from PyQt5.QtGui import *
import pickle
import sys


dbfilename='assignment6.dat'

class Calculator(QWidget):

    def __init__(self, parent=None):
        super().__init__()

        # 자료처리 관련 함수
        self.dbfilename='assignment6.dat'
        self.scoredb = self.readScoreDB()
        self.writeScoreDB()

        # Display Window
        self.display = QLineEdit('0')
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setMaxLength(10)


        # Layout
        mainLayout = QGridLayout()
        mainLayout.setSpacing(5)

        self.setLayout(mainLayout)
        self.setGeometry(300,300,500,250)
        self.setWindowTitle("Assignment6")

        # grid1
        self.grid1=QHBoxLayout()
        # grid2
        self.grid2 = QHBoxLayout()
        self.grid2.addStretch(1)
        self.grid2.setSpacing(10)
        #grid3
        self.grid3 = QHBoxLayout()
        self.grid3.setSpacing(10)
        #grid 4
        self.grid4=QVBoxLayout()

        # QLabel
        self.name = QLabel('Name: ')
        self.age = QLabel('Age: ')
        self.score = QLabel('Score: ')
        self.amount = QLabel('Amount: ')
        self.key = QLabel('Key: ')
        self.result=QLabel('Result: ')


        # QCombobox
        self.cb = QComboBox()
        self.cb.addItems(["Age","Name","Score"])


        # QPushButton
        self.addbtn=QPushButton("Add")
        self.delbtn=QPushButton("Del")
        self.findbtn=QPushButton("Find")
        self.incbtn=QPushButton("Inc")
        self.showbtn=QPushButton("Show")

        #Event

        self.addbtn.clicked.connect(self.addclicked)
        self.delbtn.clicked.connect(self.delclicked)
        self.findbtn.clicked.connect(self.findclicked)
        self.incbtn.clicked.connect(self.incclicked)
        self.showbtn.clicked.connect(self.showclicked)

        # TextEdit
        self.te=QTextEdit()


        # LineEdit
        self.nameEdit = QLineEdit()
        self.ageEdit = QLineEdit()
        self.scoreEdit = QLineEdit()
        self.amountEdit = QLineEdit()

        # grid1 설정
        self.grid1.addWidget(self.name)
        self.grid1.addWidget(self.nameEdit)
        self.grid1.addWidget(self.age)
        self.grid1.addWidget(self.ageEdit)
        self.grid1.addWidget(self.score)
        self.grid1.addWidget(self.scoreEdit)
        self.grid1.setAlignment(Qt.AlignTop)



        # grid2 설정
        self.grid2.addWidget(self.amount)
        self.grid2.addWidget(self.amountEdit)
        self.grid2.addWidget(self.key)
        self.grid2.addWidget(self.cb)



        # grid3 설정
        self.grid3.addWidget(self.addbtn)
        self.grid3.addWidget(self.delbtn)
        self.grid3.addWidget(self.findbtn)
        self.grid3.addWidget(self.incbtn)
        self.grid3.addWidget(self.showbtn)


        #grid4 설정
        self.grid4.addWidget(self.result)
        self.grid4.addWidget(self.te)

        # mainLayout에 배치
        mainLayout.addLayout(self.grid1,0,0)
        mainLayout.addLayout(self.grid2,1,0)
        mainLayout.addLayout(self.grid3,2,0)
        mainLayout.addLayout(self.grid4,3,0)

# Layout
        self.setLayout(mainLayout)
        self.show()

######################## 자료 관련 함수 #####################
    def closeEvent(self,event):
        self.writeScoreDB()

    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            self.scdb = []
            return

        try:
            self.scdb = pickle.load(fH)
        except:
            pass
        else:
            pass
        fH.close()
        return self.scdb


    def writeScoreDB(self):
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.scoredb, fH)
        fH.close()



    def showScoreDB(self,keyname):
        self.te.clear() 
        for p in sorted(self.scdb,key=lambda person: str(person[keyname])):
            for attr in sorted(p):
                last=attr+" = "+str(p[attr])+"  "
                self.te.insertPlainText(last)
            self.te.append("")

# 버튼 클릭연결

    def addclicked(self):
        self.name=self.nameEdit.text()
        self.age=self.ageEdit.text()
        self.score=self.scoreEdit.text()

        record={'Name':self.name,'Age':self.age,'Score':self.score}
        self.scdb+=[record]
        self.showScoreDB('Name')




    def delclicked(self):
        for p in self.scdb:
                if self.nameEdit.text()==p['Name']:
                    self.scdb.remove(p)
                    self.te.clear()
                    self.showScoreDB('Name')


       

    def findclicked(self):
        self.te.clear()
        for p in self.scdb:
            for p in sorted(self.scdb,key=lambda person: person['Name']):
                if self.nameEdit.text() == p ['Name']:
                    for attr in sorted(p):
                        last=attr+" = "+str(p[attr])+"  "
                        self.te.insertPlainText(last)
            break
            self.te.append("")


    def incclicked(self):
        addamount=int(self.amountEdit.text())

        for p in self.scdb:
            if self.nameEdit.text()==p['Name']:
                p['Score']+=addamount
                self.te.clear()
                self.showScoreDB('Name')   
                break
                

    def showclicked(self):

            self.sortkey = self.cb.currentText()
            self.showScoreDB(self.sortkey)



if __name__ == '__main__':

    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())

