# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 14:52:34 2018

@author: Admin
"""

import sys
import numpy as np
import scipy.integrate
from PyQt5 import QtGui, QtCore, QtWidgets
import model
import draw_n_export as graph

class YourFace(QtWidgets.QDialog):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setGeometry(50,50,1280,720)
        self.setWindowTitle('Platelets ftw')
        
        self.widget=graph.MyFace(self)
        self.widget.setGeometry(0,0,1100,720)
        
        self.pbOK=QtWidgets.QPushButton(self)
        self.pbOK.setText('click me!')
        self.pbOK.setGeometry(1110,505,87,210)
        self.pbOK.clicked.connect(self.onOK)
        
        self.widget.update()
    
    def onOK(self):
        self.widget.update()

app = QtWidgets.QApplication(sys.argv)
w = YourFace()
w.show()
sys.exit(app.exec_())
