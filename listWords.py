from PyQt5 import QtCore, QtGui, QtWidgets
from database import Database

class Ui_ListWords(object):
    def setupUi(self, Form):
        self.database = Database()

        Form.setObjectName("Form")
        Form.resize(500, 700)
        self.englishLabel = QtWidgets.QLabel(Form)
        self.englishLabel.setGeometry(QtCore.QRect(30, 50, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.englishLabel.setFont(font)
        self.englishLabel.setObjectName("englishLabel")
        self.uzbekLabel = QtWidgets.QLabel(Form)
        self.uzbekLabel.setGeometry(QtCore.QRect(270, 50, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.uzbekLabel.setFont(font)
        self.uzbekLabel.setObjectName("uzbekLabel")
        self.englishList = QtWidgets.QListWidget(Form)
        self.englishList.setGeometry(QtCore.QRect(20, 100, 221, 541))
        self.englishList.setObjectName("englishList")
        self.uzbekList = QtWidgets.QListWidget(Form)
        self.uzbekList.setGeometry(QtCore.QRect(260, 100, 221, 541))
        self.uzbekList.setObjectName("uzbekList")
        self.searchBtn = QtWidgets.QPushButton(Form)
        self.searchBtn.setGeometry(QtCore.QRect(330, 660, 150, 28))
        self.searchBtn.setObjectName("searchBtn")
        self.addNewWordBtn = QtWidgets.QPushButton(Form)
        self.addNewWordBtn.setGeometry(QtCore.QRect(172, 660, 150, 28))
        self.addNewWordBtn.setObjectName("addNewWordBtn")
        self.menuBtn = QtWidgets.QPushButton(Form)
        self.menuBtn.setGeometry(QtCore.QRect(10, 660, 150, 28))
        self.menuBtn.setObjectName("menuBtn")

        self.words = self.database.selectWords()

        for word in self.words:
            englishItem = QtWidgets.QListWidgetItem()
            englishItem.setText(word[1])
            self.englishList.addItem(englishItem)

            uzbekItem = QtWidgets.QListWidgetItem()
            uzbekItem.setText(word[2])
            self.uzbekList.addItem(uzbekItem)  

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "list words"))
        self.englishLabel.setText(_translate("Form", "English:"))
        self.uzbekLabel.setText(_translate("Form", "Uzbek:"))
        self.searchBtn.setText(_translate("Form", "search"))
        self.addNewWordBtn.setText(_translate("Form", "Add new word"))
        self.menuBtn.setText(_translate("Form", "Menu"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_ListWords()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
