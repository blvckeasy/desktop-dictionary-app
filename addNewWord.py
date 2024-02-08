from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_addWordWindow(object):
    def setupUi(self, addWordWindow):
        addWordWindow.setObjectName("addWordWindow")
        addWordWindow.resize(500, 700)
        self.englishInput = QtWidgets.QLineEdit(addWordWindow)
        self.englishInput.setGeometry(QtCore.QRect(30, 30, 341, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.englishInput.setFont(font)
        self.englishInput.setText("")
        self.englishInput.setObjectName("englishInput")
        self.uzbekInput = QtWidgets.QLineEdit(addWordWindow)
        self.uzbekInput.setGeometry(QtCore.QRect(30, 80, 341, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.uzbekInput.setFont(font)
        self.uzbekInput.setInputMethodHints(QtCore.Qt.ImhSensitiveData)
        self.uzbekInput.setText("")
        self.uzbekInput.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.uzbekInput.setReadOnly(True)
        self.uzbekInput.setObjectName("uzbekInput")
        self.sendBtn = QtWidgets.QPushButton(addWordWindow)
        self.sendBtn.setGeometry(QtCore.QRect(390, 50, 93, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.sendBtn.setFont(font)
        self.sendBtn.setObjectName("sendBtn")
        self.menuBtn = QtWidgets.QPushButton(addWordWindow)
        self.menuBtn.setGeometry(QtCore.QRect(10, 650, 150, 28))
        self.menuBtn.setObjectName("menuBtn")
        self.listOfWordsBtn = QtWidgets.QPushButton(addWordWindow)
        self.listOfWordsBtn.setGeometry(QtCore.QRect(172, 650, 150, 28))
        self.listOfWordsBtn.setObjectName("listOfWordsBtn")
        self.searchBtn = QtWidgets.QPushButton(addWordWindow)
        self.searchBtn.setGeometry(QtCore.QRect(330, 650, 150, 28))
        self.searchBtn.setObjectName("searchBtn")

        self.retranslateUi(addWordWindow)
        QtCore.QMetaObject.connectSlotsByName(addWordWindow)

    def retranslateUi(self, addWordWindow):
        _translate = QtCore.QCoreApplication.translate
        addWordWindow.setWindowTitle(_translate("addWordWindow", "add new word"))
        self.englishInput.setPlaceholderText(_translate("addWordWindow", "English..."))
        self.uzbekInput.setPlaceholderText(_translate("addWordWindow", "Uzbek..."))
        self.sendBtn.setText(_translate("addWordWindow", "Send"))
        self.menuBtn.setText(_translate("addWordWindow", "Menu"))
        self.listOfWordsBtn.setText(_translate("addWordWindow", "List of words"))
        self.searchBtn.setText(_translate("addWordWindow", "search"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    addWordWindow = QtWidgets.QWidget()
    ui = Ui_addWordWindow()
    ui.setupUi(addWordWindow)
    addWordWindow.show()
    sys.exit(app.exec_())
