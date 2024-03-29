from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Search(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 700)
        self.searchInput = QtWidgets.QLineEdit(Form)
        self.searchInput.setGeometry(QtCore.QRect(90, 10, 311, 31))
        self.searchInput.setText("")
        self.searchInput.setObjectName("searchInput")
        self.searchBtn = QtWidgets.QPushButton(Form)
        self.searchBtn.setGeometry(QtCore.QRect(410, 10, 81, 31))
        self.searchBtn.setObjectName("searchBtn")
        self.languageBox = QtWidgets.QComboBox(Form)
        self.languageBox.setGeometry(QtCore.QRect(10, 10, 73, 31))
        self.languageBox.setObjectName("languageBox")
        self.languageBox.addItem("")
        self.languageBox.addItem("")
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(20, 60, 461, 581))
        self.listWidget.setObjectName("listWidget")
        self.listOfWordsBtn = QtWidgets.QPushButton(Form)
        self.listOfWordsBtn.setGeometry(QtCore.QRect(328, 660, 150, 28))
        self.listOfWordsBtn.setObjectName("listOfWordsBtn")
        self.menuBtn = QtWidgets.QPushButton(Form)
        self.menuBtn.setGeometry(QtCore.QRect(8, 660, 150, 28))
        self.menuBtn.setObjectName("menuBtn")
        self.addNewWordBtn = QtWidgets.QPushButton(Form)
        self.addNewWordBtn.setGeometry(QtCore.QRect(170, 660, 150, 28))
        self.addNewWordBtn.setObjectName("addNewWordBtn")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "search"))
        self.searchInput.setPlaceholderText(_translate("Form", "So\'z kiriting..."))
        self.searchBtn.setText(_translate("Form", "Search"))
        self.languageBox.setItemText(0, _translate("Form", "Uz-En"))
        self.languageBox.setItemText(1, _translate("Form", "En-Uz"))
        self.listOfWordsBtn.setText(_translate("Form", "List of words"))
        self.menuBtn.setText(_translate("Form", "Menu"))
        self.addNewWordBtn.setText(_translate("Form", "Add new word"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Search()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
