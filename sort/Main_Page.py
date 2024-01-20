import resources
from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd

#Change Import Class Name if again converted ui file to python file as well as for the scrapping python file
from Search import Ui_SearchWindow
from Scrapping import Ui_ScrappingWindow
import Sorting_Algos
import Sorting_Dl

# ###########################
# Load Data Function #######
# #########################
df = pd.read_csv('Data.csv')
Medicine_MF       =df["Medicine MF"].values.tolist()       
Medicine_MW       =df["Medicine MW"].values.tolist()    
Medicine_Name     =df["Medicine Name "].values.tolist()  
IUPAC_Name        =df["IUPAC Name"].values.tolist()
Compound_CID      =df["Compound CID "].values.tolist()
Create_Date       =df["Create Date"].values.tolist()

def Load_Data():
    df = pd.read_csv('Data.csv')
    Medicine_MF       =df["Medicine MF"].values.tolist()       
    Medicine_MW       =df["Medicine MW"].values.tolist()    
    Medicine_Name     =df["Medicine Name "].values.tolist()  
    IUPAC_Name        =df["IUPAC Name"].values.tolist()
    Compound_CID      =df["Compound CID "].values.tolist()
    Create_Date       =df["Create Date"].values.tolist()
    return [Medicine_Name,Medicine_MF,Medicine_MW,IUPAC_Name,Compound_CID,Create_Date]

class Ui_MainWindow(object):
    def Change_Window_Search(self): # Search Window Opener
        self.window = QtWidgets.QMainWindow()
        self.ui=Ui_SearchWindow()
        self.ui.setupUi(self.window)
        self.window.show()
    def Change_Window_Scrapping(self): # Scrapping Window Opener
        self.window = QtWidgets.QMainWindow()
        self.ui=Ui_ScrappingWindow()
        self.ui.setupUi(self.window)
        self.window.show()
    def setupUi(self, MainWindow):
        # ########################################
        # load Data as Combined Lists ###########
        # ######################################
        Combined_lists=Load_Data()
        # Main Program For Form........
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(1089, 579)
        MainWindow.setMaximumSize(QtCore.QSize(10000, 100000))
        MainWindow.setBaseSize(QtCore.QSize(921, 481))
        font = QtGui.QFont()
        font.setFamily("SimSun-ExtB")
        font.setPointSize(8)
        MainWindow.setFont(font)
        MainWindow.setWindowTitle("PharMart Pharmacy")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Logo/Logo.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setToolTip("")
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
        self.ComboMethod = QtWidgets.QComboBox(self.centralwidget)
        self.ComboMethod.setGeometry(QtCore.QRect(960, 230, 121, 31))
        self.ComboMethod.setEditable(True)
        self.ComboMethod.setObjectName("ComboMethod")
        self.ComboMethod.addItem("")
        self.ComboMethod.addItem("")
        self.ComboMethod.addItem("")
        self.ComboMethod.addItem("")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(960, 200, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setTextFormat(QtCore.Qt.RichText)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(950, 130, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setTextFormat(QtCore.Qt.RichText)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.ComboSortBy = QtWidgets.QComboBox(self.centralwidget)
        self.ComboSortBy.setGeometry(QtCore.QRect(960, 160, 121, 31))
        self.ComboSortBy.setEditable(True)
        self.ComboSortBy.setObjectName("ComboSortBy")
        self.ComboSortBy.addItem("")
        self.ComboSortBy.addItem("")
        self.ComboSortBy.addItem("")
        self.ComboSortBy.addItem("")
        self.ComboSortBy.addItem("")
        self.ComboSortBy.addItem("")
        self.Sort = QtWidgets.QPushButton(self.centralwidget)
        self.Sort.setGeometry(QtCore.QRect(990, 380, 75, 23))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Sort/sort-amount.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Sort.setIcon(icon1)
        self.Sort.setCheckable(False)
        self.Sort.setObjectName("Sort")
        self.Account_Label = QtWidgets.QLabel(self.centralwidget)
        self.Account_Label.setGeometry(QtCore.QRect(1020, 0, 61, 61))
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
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Map/map.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon2)
        self.pushButton.setObjectName("pushButton")
        self.SearchButton = QtWidgets.QPushButton(self.centralwidget)
        self.SearchButton.setGeometry(QtCore.QRect(40, 180, 121, 31))
        self.SearchButton.setAutoFillBackground(False)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/Search/search-more.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.SearchButton.setIcon(icon3)
        self.SearchButton.setObjectName("SearchButton")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 110, 31, 31))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap(":/Arrow/arrow.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(40, 250, 121, 31))
        self.pushButton_3.setAutoFillBackground(False)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/CRUD/CRUD.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon4)
        self.pushButton_3.setObjectName("pushButton_3")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(170, 70, 781, 471))
        self.tableWidget.setMinimumSize(QtCore.QSize(781, 471))
        self.tableWidget.setDragEnabled(True)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(len(Combined_lists[0])-1)
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
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(960, 270, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setTextFormat(QtCore.Qt.RichText)
        self.label_8.setObjectName("label_8")
        self.Sort_Order = QtWidgets.QComboBox(self.centralwidget)
        self.Sort_Order.setGeometry(QtCore.QRect(960, 300, 121, 31))
        self.Sort_Order.setEditable(True)
        self.Sort_Order.setObjectName("Sort_Order")
        self.Sort_Order.addItem("")
        self.Sort_Order.addItem("")
        self.label.raise_()
        self.Menu_Label.raise_()
        self.Header_Label.raise_()
        self.Sort_Label.raise_()
        self.ComboMethod.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.ComboSortBy.raise_()
        self.Sort.raise_()
        self.Account_Label.raise_()
        self.pushButton.raise_()
        self.SearchButton.raise_()
        self.label_7.raise_()
        self.label_2.raise_()
        self.pushButton_3.raise_()
        self.tableWidget.raise_()
        self.label_8.raise_()
        self.Sort_Order.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.ShowDataInTable(Combined_lists)
        self.Sort.clicked.connect(self.ShowDataInTable_Sorting)
        # ###########################
        # Search button Event ######
        # #########################
        
        self.SearchButton.clicked.connect(self.Change_Window_Search)
        self.pushButton_3.clicked.connect(self.Change_Window_Scrapping)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    # ####################################
    # Data Shown With sorting ###########
    # ##################################        
    def ShowDataInTable_Sorting(self,Combined_lists):
            Arr=[]
            Sorting_Dl.Load_Data()
            Sort_BY=self.ComboSortBy.currentText()
            print(Sort_BY)
            if Sort_BY=="Name":
                Arr= Medicine_Name
            elif Sort_BY== "Medicine_MF":
                Arr= Medicine_MF
            elif Sort_BY== "Medicine_MW":
                Arr= Medicine_MW
            elif Sort_BY== "IUPAC_Name":
                Arr= IUPAC_Name
            elif Sort_BY== "Compound_CID":
                Arr= Compound_CID
            elif Sort_BY== "Create_Date":
                Arr= Create_Date
            print(Arr[0:9])
            Sorting_Method=self.ComboMethod.currentText()
            Sort_Order=self.Sort_Order.currentText()
            if Sorting_Method=="Bubble Sort":
                if Sort_Order=="Ascending":
                    Sorting_Algos.BubbleSort("Ascending",Arr)
                else:
                    Sorting_Algos.BubbleSort("Descending",Arr)
            elif  Sorting_Method=="Selection Sort":
                if Sort_Order=="Ascending":
                    Sorting_Algos.SelectionSort("Ascending",Arr)
                else:
                    Sorting_Algos.SelectionSort("Descending",Arr)
            elif Sorting_Method=="Gnome Sort":
                if Sort_Order=="Ascending":
                    Sorting_Algos.gnomeSort("Ascending",Arr)
                else:
                    Sorting_Algos.gnomeSort("Descending",Arr)
            elif Sorting_Method=="Shell Sort":
                if Sort_Order=="Ascending":
                    Sorting_Algos.shellSort("Ascending",Arr)
                else:
                    Sorting_Algos.shellSort("Descending",Arr)
            print("End Sorting..... Calling Table")
            row1 = 0
            for i in range(len(Sorting_Dl.Mega_List)):
                self.tableWidget.setItem(row1,0,QtWidgets.QTableWidgetItem(str(Sorting_Dl.Mega_List[i].Medicine_Name)))
                self.tableWidget.setItem(row1,1,QtWidgets.QTableWidgetItem(str(Sorting_Dl.Mega_List[i].Medicine_MF)))
                self.tableWidget.setItem(row1,2,QtWidgets.QTableWidgetItem(str(Sorting_Dl.Mega_List[i].Medicine_MW)))
                self.tableWidget.setItem(row1,3,QtWidgets.QTableWidgetItem(str(Sorting_Dl.Mega_List[i].IUPAC_Name)))
                self.tableWidget.setItem(row1,4,QtWidgets.QTableWidgetItem(str(Sorting_Dl.Mega_List[i].Compound_CID)))
                self.tableWidget.setItem(row1,5,QtWidgets.QTableWidgetItem(str(Sorting_Dl.Mega_List[i].Create_Date)))
                row1 += 1
    # ####################################
    # Data Shown Without Sorting ########
    # ##################################
    def ShowDataInTable(self,Combined_lists):
        row1 = 0
        for i in range(len(Combined_lists[0])):
            self.tableWidget.setItem(row1,0,QtWidgets.QTableWidgetItem(str(Combined_lists[0][i])))
            self.tableWidget.setItem(row1,1,QtWidgets.QTableWidgetItem(str(Combined_lists[1][i])))
            self.tableWidget.setItem(row1,2,QtWidgets.QTableWidgetItem(str(Combined_lists[2][i])))
            self.tableWidget.setItem(row1,3,QtWidgets.QTableWidgetItem(str(Combined_lists[3][i])))
            self.tableWidget.setItem(row1,4,QtWidgets.QTableWidgetItem(str(Combined_lists[4][i])))
            self.tableWidget.setItem(row1,5,QtWidgets.QTableWidgetItem(str(Combined_lists[5][i])))
            row1 += 1
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Copyright @ [Yasir , Moazam &amp; 2022]</span></p></body></html>"))
        self.ComboMethod.setCurrentText(_translate("MainWindow", "Bubble Sort"))
        self.ComboMethod.setItemText(0, _translate("MainWindow", "Bubble Sort"))
        self.ComboMethod.setItemText(1, _translate("MainWindow", "Selection Sort"))
        self.ComboMethod.setItemText(2, _translate("MainWindow", "Gnome Sort"))
        self.ComboMethod.setItemText(3, _translate("MainWindow", "Shell Sort"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Sorting Method</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">      Sort By</span></p></body></html>"))
        self.ComboSortBy.setCurrentText(_translate("MainWindow", "Name"))
        self.ComboSortBy.setItemText(0, _translate("MainWindow", "Name"))
        self.ComboSortBy.setItemText(1, _translate("MainWindow", "Medicine_MF"))
        self.ComboSortBy.setItemText(2, _translate("MainWindow", "Medicine_MW"))
        self.ComboSortBy.setItemText(3, _translate("MainWindow", "IUPAC_Name"))
        self.ComboSortBy.setItemText(4, _translate("MainWindow", "Compound_CID"))
        self.ComboSortBy.setItemText(5, _translate("MainWindow", "Create_Date"))
        self.Sort.setText(_translate("MainWindow", "Sort"))
        self.pushButton.setText(_translate("MainWindow", "Medicines"))
        self.SearchButton.setText(_translate("MainWindow", "Search"))
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
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Sorting Order</span></p></body></html>"))
        self.Sort_Order.setItemText(0, _translate("MainWindow", "Ascending"))
        self.Sort_Order.setItemText(1, _translate("MainWindow", "Descending"))
import resources


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
