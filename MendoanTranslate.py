import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from translate import Translator

### Author
# @Dery Sudrajat

from PyQt5.QtWidgets import *


class TranslateForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.resize(350, 100)
        self.move(300, 300)
        self.setWindowTitle("Mendoan Translate")

        self.leFrom = QTextEdit()
        font  = self.leFrom.font()
        font.setPointSize(12)
        self.leFrom.setFont(font)

        self.btnTranslate = QPushButton("Translate")
        self.leTo = QTextEdit()

        vbox = QVBoxLayout()
        vbox.addWidget(self.leFrom)
        vbox.addWidget(self.btnTranslate)
        vbox.addWidget(self.leTo)

        self.btnTranslate.clicked.connect(self.Show)

        self.setLayout(vbox)

    def Show(self):
        indoTrans = Translator(to_lang="id")
        engTrans = Translator(from_lang="id", to_lang="en")
        # indoTxt = indoTrans.translate("I was buy new book")
        engTxt = engTrans.translate(self.leFrom.toPlainText())
        # print("Indo: \n", indoTxt)
        self.leTo.setText("<font size = 5>" + engTxt + "</font>")


if __name__ == '__main__':
    a = QApplication(sys.argv)

    form = TranslateForm()
    form.show()

    a.exec_()
