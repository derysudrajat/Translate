# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Translate.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

import csv

from PyQt5 import QtCore, QtWidgets
from translate import Translator


class Ui_MainWindow(object):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        """
        Define the variable name
        """
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.langFrom = QtWidgets.QComboBox(self.widget)
        self.btnSwap = QtWidgets.QPushButton(self.widget)
        self.langTo = QtWidgets.QComboBox(self.widget)
        self.txtFrom = QtWidgets.QTextEdit(self.widget)
        self.btnTranslate = QtWidgets.QPushButton(self.widget)
        self.txtTo = QtWidgets.QTextEdit(self.widget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)

    def setupUi(self, MainWindow):
        """
        set nama window dan ukuran gui
        :param MainWindow:
        :return:
        """
        MainWindow.setObjectName("My Translate")
        MainWindow.resize(415, 505)
        """
        mengatur Combo box untuk bahasa awal
        :param langFrom
        """
        self.langFrom.setObjectName("langFrom")
        self.langFrom.addItem("Indonesia")
        self.langFrom.addItem("English")
        self.langFrom.addItem("Japan")
        self.langFrom.addItem("Ngapak")
        '''
        mengatur Combo boc untuk bahasa tujuan
        :param langTo
        '''
        self.langTo.setObjectName("langTo")
        self.langTo.addItem("English")
        self.langTo.addItem("Indonesia")
        self.langTo.addItem("Japan")
        self.langTo.addItem("Ngapak")
        '''
        mengatur Buttonn untuk swap bahasa
        :param btnSwap
        '''
        self.btnSwap.setObjectName("btnSwap")
        '''
        mengatur TextEdit untuk teks bahasa awal
        :param txtFrom
        '''
        self.txtFrom.setObjectName("txtFrom")
        mfont1 = self.txtFrom.font()
        mfont1.setPointSize(12)
        self.txtFrom.setFont(mfont1)
        '''
        mengatur Button untuk menerjemahkan text ke bahasa tujuan
        :param btnTranslate
        '''
        self.btnTranslate.setObjectName("btnTranslate")
        '''
        mengatur TextEdit untuk teks bahasa tujuan
        :param txtTO
        '''
        self.txtTo.setObjectName("txtTo")
        mfont2 = self.txtTo.font()
        mfont2.setPointSize(12)
        self.txtTo.setFont(mfont2)
        '''
        pengaturan layout
        '''
        self.centralwidget.setObjectName("centralwidget")
        self.widget.setGeometry(QtCore.QRect(20, 10, 371, 452))
        self.widget.setObjectName("widget")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.addWidget(self.langFrom)
        self.horizontalLayout.addWidget(self.btnSwap)
        self.horizontalLayout.addWidget(self.langTo)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout.addWidget(self.txtFrom)
        self.verticalLayout.addWidget(self.btnTranslate)
        self.verticalLayout.addWidget(self.txtTo)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 415, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        '''
        aksi untuk button
        '''
        self.btnTranslate.clicked.connect(self.Show)
        self.btnSwap.clicked.connect(self.swap)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    '''
        fungsi untuk mengecek bahasa dari Combo box
        :param mLang # nilai kembalian
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
            mLang = "ng"
            return mLang

    '''
        method untuk menukar bahasa awal dan bahasa tujuan
    '''

    def swap(self):
        txtF = self.langFrom.currentText()
        txtT = self.langTo.currentText()
        self.langFrom.setCurrentText(txtT)
        self.langTo.setCurrentText(txtF)

    """
        fungsi untuk mengecek apakah ada simbol "?" pada string kata
        :param afound # nilai kembalian
    """

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
       fungsi untuk mendapatkan string kata yang sudah di
       terjemahkan
       :param data # adalah data inputan dari leFrom
       :param dataFrom # adalah data bahasa awal
       :param dataTo # adalah data bahasa tujuan 
       :param strResult # nilai kembalian
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
        fungsi untuk menerjemahkan text antara bahasa indonesia dan ngapak
        :param strResult # nilai kembalian
    '''

    def ngapakTrans(self, mText, langF):
        data = mText.lower().split()
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
        if langF == "id":
            strResult = self.nTrans(data, indo, ngapak)
        else:
            strResult = self.nTrans(data, ngapak, indo)
        print(indo)
        print(ngapak)
        print(strResult)
        return strResult

    '''
        method untuk menampilkan text yang sudah di terjemahkan 
        dari bahasa awal ke bahasa tujuan
    '''

    def Show(self):
        self.txtTo.setText("Translating...")
        lgF = self.cekLang(self.langFrom.currentText())
        lgT = self.cekLang(self.langTo.currentText())
        print(lgF, lgT)
        if (lgF == "id" and lgT == "ng") or (lgF == "ng" and lgT == "id"):
            try:
                strResult = self.ngapakTrans(self.txtFrom.toPlainText(), lgF)
                self.txtTo.setText(strResult)
            except:
                self.txtTo.setText("Please try again...")
        elif lgF == "ng" and lgT != "id":
            try:
                strResult = self.ngapakTrans(self.txtFrom.toPlainText(), "ng")
                engTrans = Translator(from_lang="id", to_lang=lgT)
                try:
                    engTxt = engTrans.translate(strResult)
                    self.txtTo.setText(engTxt)
                except:
                    self.txtTo.setText("Please try again...")
            except:
                self.txtTo.setText("Please try again...")
        elif lgT == "ng" and lgF != "id":
            engTrans = Translator(from_lang=lgF, to_lang="id")
            try:
                engTxt = engTrans.translate(self.txtFrom.toPlainText())
                strResult = self.ngapakTrans(engTxt, "id")
                self.txtTo.setText(strResult)
            except:
                self.txtTo.setText("Please try again...")
        else:
            engTrans = Translator(from_lang=lgF, to_lang=lgT)
            try:
                engTxt = engTrans.translate(self.txtFrom.toPlainText())
                self.txtTo.setText(engTxt)
            except:
                self.txtTo.setText("Please try again...")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "My Translate"))
        self.btnSwap.setText(_translate("MainWindow", "Swap"))
        self.btnTranslate.setText(_translate("MainWindow", "Translate"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
