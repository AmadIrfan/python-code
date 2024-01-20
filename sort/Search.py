from Scrapping import Ui_ScrappingWindow
import resources
from tkinter import messagebox
from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
df = pd.read_csv('Data.csv')
Medicine_MF       =df["Medicine MF"].values.tolist()       
Medicine_MW       =df["Medicine MW"].values.tolist()    
Medicine_Name     =df["Medicine Name "].values.tolist()  
IUPAC_Name        =df["IUPAC Name"].values.tolist()
Compound_CID      =df["Compound CID "].values.tolist()
Create_Date       =df["Create Date"].values.tolist()

Text_Search = 'Temp'
Medicine_Name2 = []
Medicine_MF2 = []
Medicine_MW2 = []
IUPAC_Name2 = []
Compound_CID2 = []
Create_Date2 = []

class Ui_SearchWindow(object):
    def Change_Window_Scrapping(self): # Scrapping Window Opener
        self.window = QtWidgets.QMainWindow()
        self.ui=Ui_ScrappingWindow()
        self.ui.setupUi(self.window)
        self.window.show()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1089, 579)
        MainWindow.setMaximumSize(QtCore.QSize(1089, 579))
        font = QtGui.QFont()
        font.setFamily("SimSun-ExtB")
        font.setPointSize(8)
        MainWindow.setFont(font)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("#centralwidget\n"
"{backgroound colour:#1b1b27}")
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 540, 1091, 41))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("background-color: rgb(40, 43, 122);\n"
"background-color: rgb(0, 5, 39);")
        self.label.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setIndent(-1)
        self.label.setObjectName("label")
        self.Menu_Label = QtWidgets.QLabel(self.centralwidget)
        self.Menu_Label.setGeometry(QtCore.QRect(0, 70, 171, 471))
        self.Menu_Label.setStyleSheet("background-color:  rgb(0, 8, 67);")
        self.Menu_Label.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.Menu_Label.setText("")
        self.Menu_Label.setObjectName("Menu_Label")
        self.Header_Label = QtWidgets.QLabel(self.centralwidget)
        self.Header_Label.setGeometry(QtCore.QRect(0, 0, 1091, 71))
        font = QtGui.QFont()
        font.setFamily("Rage Italic")
        font.setPointSize(24)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.Header_Label.setFont(font)
        self.Header_Label.setStyleSheet("background-color: rgb(0, 8, 66);\n"
"background-color: rgb(92, 255, 228);\n"
"background-color: rgb(40, 145, 166);")
        self.Header_Label.setText("")
        self.Header_Label.setTextFormat(QtCore.Qt.RichText)
        self.Header_Label.setPixmap(QtGui.QPixmap(":/Logo/header.jpg"))
        self.Header_Label.setScaledContents(True)
        self.Header_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Header_Label.setObjectName("Header_Label")
        self.Sort_Label = QtWidgets.QLabel(self.centralwidget)
        self.Sort_Label.setGeometry(QtCore.QRect(950, 70, 141, 471))
        self.Sort_Label.setStyleSheet("background-color: rgb(0, 8, 67);")
        self.Sort_Label.setText("")
        self.Sort_Label.setObjectName("Sort_Label")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(960, 280, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setTextFormat(QtCore.Qt.RichText)
        self.label_5.setObjectName("label_5")
        self.Sort = QtWidgets.QPushButton(self.centralwidget)
        self.Sort.setGeometry(QtCore.QRect(980, 400, 75, 23))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Search/search-more.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Sort.setIcon(icon)
        self.Sort.setCheckable(False)
        self.Sort.setObjectName("Sort")
        self.Account_Label = QtWidgets.QLabel(self.centralwidget)
        self.Account_Label.setGeometry(QtCore.QRect(840, 0, 61, 61))
        self.Account_Label.setText("")
        self.Account_Label.setPixmap(QtGui.QPixmap(":/Account/account.png"))
        self.Account_Label.setScaledContents(True)
        self.Account_Label.setObjectName("Account_Label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 51, 51))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/Menu/menu.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(40, 110, 121, 31))
        self.pushButton.setAutoFillBackground(False)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Map/map.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 180, 121, 31))
        self.pushButton_2.setAutoFillBackground(False)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 180, 31, 31))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap(":/Arrow/arrow.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(40, 250, 121, 31))
        self.pushButton_3.setAutoFillBackground(False)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/CRUD/CRUD.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(170, 70, 781, 471))
        self.tableWidget.setMinimumSize(QtCore.QSize(781, 471))
        self.tableWidget.setDragEnabled(True)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setWordWrap(False)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(len(Compound_CID2))
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(130)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(960, 310, 113, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(970, 150, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setTextFormat(QtCore.Qt.RichText)
        self.label_6.setObjectName("label_6")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(960, 181, 111, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setItemText(2, "")
        self.label.raise_()
        self.Menu_Label.raise_()
        self.Header_Label.raise_()
        self.Sort_Label.raise_()
        self.label_5.raise_()
        self.Sort.raise_()
        self.Account_Label.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.label_7.raise_()
        self.label_2.raise_()
        self.pushButton_3.raise_()
        self.tableWidget.raise_()
        self.lineEdit.raise_()
        self.label_6.raise_()
        self.comboBox.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.Sort.clicked.connect(self.ShowDataInTable)
        self.pushButton_3.clicked.connect(self.Change_Window_Scrapping)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def binary_search(list_num, first_index, last_index, to_search,self):
        if last_index >= first_index:
            
            mid_index = (first_index + last_index) // 2
            mid_element = list_num[mid_index]

        if mid_element == to_search:
            return f"{mid_element} occurs in position {mid_index}"

        elif mid_element > to_search:
            new_position = mid_index - 1
            # new last index is the new position
            return self.binary_search(list_num, first_index, new_position, to_search)

        elif mid_element < to_search:
            new_position = mid_index + 1
            # new first index is the new position
            return self.binary_search(list_num, new_position, last_index, to_search)

    def Clears_List(self):
        Medicine_Name2.clear()
        Medicine_MF2.clear()
        Medicine_MW2.clear()
        IUPAC_Name2.clear()
        Compound_CID2.clear()
        Create_Date2.clear()
        
    def Linear_Search(self):
        Text_Search = self.lineEdit.text()
        length = len(Text_Search)+1
        for i in range(0, len(Compound_CID)):
            Temp = str(Compound_CID[i])
            if str(Text_Search) == Temp[0:length]:
                Medicine_Name2.append(Medicine_Name[i])
                Medicine_MF2.append(Medicine_MF[i])
                Medicine_MW2.append(Medicine_MW[i])
                IUPAC_Name2.append(IUPAC_Name[i])
                Compound_CID2.append(Compound_CID[i])
                Create_Date2.append(Create_Date[i])

    def ShowDataInTable(self):
        Search_Method=self.comboBox.currentText()
        self.Linear_Search()
        self.tableWidget.setRowCount(len(Compound_CID2))
        row1 = 0
        for i in range(len(Medicine_Name2)):
            self.tableWidget.setItem(
                row1, 0, QtWidgets.QTableWidgetItem(str(Medicine_Name2[i])))
            self.tableWidget.setItem(
                row1, 1, QtWidgets.QTableWidgetItem(str(Medicine_MF2[i])))
            self.tableWidget.setItem(
                row1, 2, QtWidgets.QTableWidgetItem(str(Medicine_MW2[i])))
            self.tableWidget.setItem(
                row1, 3, QtWidgets.QTableWidgetItem(str(IUPAC_Name2[i])))
            self.tableWidget.setItem(
                row1, 4, QtWidgets.QTableWidgetItem(str(Compound_CID2[i])))
            self.tableWidget.setItem(
                row1, 5, QtWidgets.QTableWidgetItem(str(Create_Date2[i])))
            row1 += 1
        if len(Compound_CID2) < 1:
            messagebox.showerror("Error","Data Not Found")
        self.Clears_List()
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Copyright @ [Yasir , Moazam &amp; 2022]</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Compound CID</span></p></body></html>"))
        self.Sort.setText(_translate("MainWindow", "Search"))
        self.pushButton.setText(_translate("MainWindow", "Medicines"))
        self.pushButton_2.setText(_translate("MainWindow", "Search"))
        self.pushButton_3.setText(_translate("MainWindow", "Scrapping"))
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Medicine MF"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Medicine MW"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "IUPAC Name"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Compound CID"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Create Date"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Search By :</span></p></body></html>"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Binary Search"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Linear Search"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_SearchWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
