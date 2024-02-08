from PyQt5 import QtCore, QtGui, QtWidgets
from addNewWord import Ui_addWordWindow
from listWords import Ui_ListWords
from search import Ui_Search


class Ui_Main(object):
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(500, 700)
        Main.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.addNewWordBtn = QtWidgets.QPushButton(Main)
        self.addNewWordBtn.setGeometry(QtCore.QRect(100, 170, 281, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.addNewWordBtn.setFont(font)
        self.addNewWordBtn.setObjectName("addNewWordBtn")
        self.listOfWordBtn = QtWidgets.QPushButton(Main)
        self.listOfWordBtn.setGeometry(QtCore.QRect(100, 270, 281, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.listOfWordBtn.setFont(font)
        self.listOfWordBtn.setObjectName("listOfWordBtn")
        self.searchWordBtn = QtWidgets.QPushButton(Main)
        self.searchWordBtn.setGeometry(QtCore.QRect(100, 370, 281, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.searchWordBtn.setFont(font)
        self.searchWordBtn.setObjectName("searchWordBtn")
        self.exitBtn = QtWidgets.QPushButton(Main)
        self.exitBtn.setGeometry(QtCore.QRect(100, 470, 281, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.exitBtn.setFont(font)
        self.exitBtn.setObjectName("exitBtn")

        self.addNewWordBtn.clicked.connect(self.openAddNewWordWindow)
        self.listOfWordBtn.clicked.connect(self.openListOfWordWindow)
        self.searchWordBtn.clicked.connect(self.openSearchWindow)
        self.exitBtn.clicked.connect(self.exitFunction)

        self.retranslateUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", "Main"))
        self.addNewWordBtn.setText(_translate("Main", "Add new word"))
        self.listOfWordBtn.setText(_translate("Main", "List of word"))
        self.searchWordBtn.setText(_translate("Main", "Search word"))
        self.exitBtn.setText(_translate("Main", "Exit"))

    def openAddNewWordWindow(self):
        self.addNewWordWidget = QtWidgets.QWidget()
        self.addNewWordWindow = Ui_addWordWindow()
        self.addNewWordWindow.setupUi(self.addNewWordWidget)
        self.addNewWordWidget.show()
        Main.close()

    def openListOfWordWindow(self):
        self.listOfWordWidget = QtWidgets.QWidget()
        self.listOfWordWindow = Ui_ListWords()
        self.listOfWordWindow.setupUi(self.listOfWordWidget)
        self.listOfWordWidget.show()
        Main.close()

    def openSearchWindow(self):
        self.searchWidget = QtWidgets.QWidget()
        self.searchWindow = Ui_Search()
        self.searchWindow.setupUi(self.searchWidget)
        self.searchWidget.show()
        Main.close()

    def exitFunction(self):
        Main.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Main = QtWidgets.QWidget()
    ui = Ui_Main()
    ui.setupUi(Main)
    Main.show()
    sys.exit(app.exec_())
