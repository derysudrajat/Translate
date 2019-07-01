import csv
import sys

from PyQt5.QtWidgets import *


class IndoNgapakForm(QWidget):
    def __init__(self):
        super(IndoNgapakForm, self).__init__()
        self.setupUI()

    def setupUI(self):
        self.resize(415, 505)
        self.move(300, 300)
        self.setWindowTitle("Indo-Ngapak")
        '''
            mendefinisikan untuk combo box bahasa awal
            :param langFrom
        '''
        self.langFrom = QComboBox()
        self.langFrom.addItem("Indonesia")
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
        self.langTo.addItem("Ngapak")
        self.langTo.addItem("Indonesia")
        '''
            pengaturan layout untuk menu menu di atas
            diatur secara horizontal
        '''
        hbox = QHBoxLayout()
        hbox.addWidget(self.langFrom)
        hbox.addWidget(self.btnSwap)
        hbox.addWidget(self.langTo)
        '''
            mendefinisikan Text Edit untuk bahasa awal
            dengan ukuran text 12sp
            :param leFrom
        '''
        self.leFrom = QTextEdit()
        font = self.leFrom.font()
        font.setPointSize(12)
        self.leFrom.setFont(font)
        '''
            mendefinisikan Button untuk aksi menerjemahkan text
            dari bahasa awal ke bahasa tujuan
            :param btnTranslate
        '''
        self.btnTranslate = QPushButton("Translate")
        '''
            mendefinisikan Text Edit untuk bahasa awal
            dengan ukuran text 12sp
            :param leFrom
        '''
        self.leTo = QTextEdit()
        font2 = self.leTo.font()
        font2.setPointSize(12)
        self.leTo.setFont(font2)
        '''
            pengaturan layout utama dengan semua komponen
            diatur secara vertical
        '''
        vbox = QVBoxLayout()
        vbox.addItem(hbox)
        vbox.addWidget(self.leFrom)
        vbox.addWidget(self.btnTranslate)
        vbox.addWidget(self.leTo)
        '''
            penanganan aksi untuk semua button pada file ini
        '''
        self.btnTranslate.clicked.connect(self.Show)
        self.btnSwap.clicked.connect(self.swap)

        self.setLayout(vbox)

    '''
       method untuk menukar bahasa awal dan bahasa tujuan
    '''

    def swap(self):
        txtF = self.langFrom.currentText()
        txtT = self.langTo.currentText()
        self.langFrom.setCurrentText(txtT)
        self.langTo.setCurrentText(txtF)

    def cekSym(self, str):
        afound = False
        for i, x in enumerate(str):
            if x == "?":
                afound = True
                break
            else:
                print("false")
                afound = False

        return afound

    '''
       method untuk mendapatkan string kata yang sudah di
       terjemahkan
       :param data # adalah data inputan dari leFrom
       :param dataFrom # adalah data bahasa awal
       :param dataTo # adalah data bahasa tujuan 
    '''

    def nTrans(self, data, dataFrom, dataTo):
        translate = []
        strResult = ""
        for a in data:
            stat = False
            ff = self.cekSym(a)
            for i, x in enumerate(dataFrom):
                if ff == True:
                    if a.replace("?", "") == x:
                        translate.append(dataTo[i] + "?")
                        stat = True
                else:
                    if a == x:
                        translate.append(dataTo[i])
                        stat = True
            if stat != True:
                if ff == True:
                    translate.append(a + "?")
                else:
                    translate.append(a)

        for j, b in enumerate(translate):
            strResult += translate[j] + " "
        return strResult

    '''
        menampilkan hasil bahasa yang sudah di terjemahkan ke
        leTo
    '''

    def Show(self):
        txtInput = self.leFrom.toPlainText()
        txtF = self.langFrom.currentText()
        data = txtInput.split()
        print(data)
        indo = []
        ngapak = []
        strResult = ""
        '''
        membaca data dari datalang.csv dan menyimpan pada
        varible indo dan ngapak
        '''
        with open('datalang.csv') as csvDataFile:
            csvReader = csv.reader(csvDataFile)
            for row in csvReader:
                indo.append(row[0])
                ngapak.append(row[1])

        if txtF == "Indonesia":
            strResult = self.nTrans(data, indo, ngapak)
        else:
            strResult = self.nTrans(data, ngapak, indo)
        print(indo)
        print(ngapak)
        print(strResult)
        self.leTo.setText(strResult)


if __name__ == '__main__':
    a = QApplication(sys.argv)

    form = IndoNgapakForm()
    form.show()

    a.exec_()
