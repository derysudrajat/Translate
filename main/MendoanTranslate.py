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
        self.resize(415, 505)
        self.move(300, 300)
        self.setWindowTitle("Mendoan Translate")

        self.leFrom = QTextEdit()
        font = self.leFrom.font()
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

    '''
    Methos untuk mengecek bahasa dari Combo box
    '''

    def cekLang(self, lang):
        if lang == "English":
            mLang = "en"
            return mLang
        elif lang == "Indonesia":
            mLang = "id"
            return mLang
        else:
            mLang = "ja"
            return mLang

    '''
    method untuk menukar bahasa awal dan bahasa tujuan
    '''

    def swap(self):
        txtF = self.langFrom.currentText()
        txtT = self.langTo.currentText()
        self.langFrom.setCurrentText(txtT)
        self.langTo.setCurrentText(txtF)

    '''
    method untuk menampilkan text yang sudah di terjemahkan dari bahasa awal ke bahasa tujuan
    '''

    def Show(self):
        lgF = self.cekLang(self.langFrom.currentText())
        lgT = self.cekLang(self.langTo.currentText())
        indoTrans = Translator(to_lang="id")
        engTrans = Translator(from_lang=lgF, to_lang=lgT)
        # indoTxt = indoTrans.translate("I was buy new book")
        engTxt = engTrans.translate(self.txtFrom.toPlainText())
        # print("Indo: \n", indoTxt)
        self.txtTo.setText(engTxt)


if __name__ == '__main__':
    a = QApplication(sys.argv)

    form = TranslateForm()
    form.show()

    a.exec_()
