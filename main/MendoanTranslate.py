import sys

from PyQt5.QtWidgets import *
from translate import Translator


### Author
# @Dery Sudrajat


class TranslateForm(QWidget):
    def __init__(self):
        super(TranslateForm, self).__init__()
        self.setupUI()

    def setupUI(self):
        self.resize(415, 505)
        self.move(300, 300)
        self.setWindowTitle("Mendoan Translate")
        '''
            mendefinisikan untuk combo box bahasa awal
            :param langFrom
        '''
        self.langFrom = QComboBox()
        self.langFrom.addItem("Indonesia")
        self.langFrom.addItem("English")
        self.langFrom.addItem("Japan")
        self.langFrom.addItem("Ngapak")
        '''
            mendefinisikan Button untuk aksi menukar bahasa
            pada combo box
            :param btnSwap
        '''
        self.btnSwap = QPushButton("Swap")
        '''
            mendefinisikan untuk combo box bahasa tujuan
            :param langTo
        '''
        self.langTo = QComboBox()
        self.langTo.addItem("English")
        self.langTo.addItem("Indonesia")
        self.langTo.addItem("Japan")
        self.langTo.addItem("Ngapak")
        '''
            pengaturan layout untuk menu menu di atas
            diatur secara horizontal
        '''
        hbox = QHBoxLayout()
        hbox.addWidget(self.langFrom)
        hbox.addWidget(self.btnSwap)
        hbox.addWidget(self.langTo)

        self.leFrom = QTextEdit()
        font = self.leFrom.font()
        font.setPointSize(12)
        self.leFrom.setFont(font)

        self.btnTranslate = QPushButton("Translate")
        self.leTo = QTextEdit()

        vbox = QVBoxLayout()
        vbox.addItem(hbox)
        vbox.addWidget(self.leFrom)
        vbox.addWidget(self.btnTranslate)
        vbox.addWidget(self.leTo)

        self.btnTranslate.clicked.connect(self.Show)
        self.btnSwap.clicked.connect(self.swap)

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
        elif lang == "Japan":
            mLang = "ja"
            return mLang
        else:
            mLang = "pk"
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
