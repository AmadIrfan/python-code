from PyQt5 import QtWidgets, uic,QtCore, QtGui
from PyQt5.QtCore import Qt
import sys
import time
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from Main_Page import Ui_MainWindow
# #############################################
# Import Resource File For Images ############
# ###########################################
import resources
        
class UI(QtWidgets.QMainWindow):
    def Change_Window1(self): # Main Window Opener
        self.window = QtWidgets.QMainWindow()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.window.show()

    def __init__(self):
        super(UI, self).__init__() # Call the inherited classes __init__ method
        
        uic.loadUi('F_Window.ui', self) # Load the .ui file
        self.setWindowTitle("PharMart Pharmacy") # Set Title Name
        self.setWindowIcon(QtGui.QIcon('Logo.jpg')) # 
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)# Remove Title Bar Of Form
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        
        self.show() # Show the GUI
        # #############################################
        # Chk To Open Next Window If Clicked #########
        # ###########################################
        self.commandLinkButton.clicked.connect(self.Change_Window1)# Change Window
        self.commandLinkButton.clicked.connect(self.close)# Remove Previous One
        
app = QtWidgets.QApplication(sys.argv) # Create an instance of QtWidgets.QApplication
window = UI() # Create an instance of our class
app.exec_() # Start the application