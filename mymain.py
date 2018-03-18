# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 14:52:34 2018

@author: Admin
"""
#showcase of how to use the widget

import sys
from PyQt5 import QtWidgets
import ayyy_draw as graph

class YourFace(QtWidgets.QDialog):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setGeometry(50,50,1280,720)
        self.setWindowTitle("DrawyDrawy more like it's haaaaaa noon")
        
        self.DrawyDrawy=graph.MyFace(self)
        self.DrawyDrawy.setGeometry(0,0,1280,720)
    
    def resizeEvent(self, event):
        self.DrawyDrawy.setGeometry(0,0,self.width(),self.height())


app = QtWidgets.QApplication(sys.argv)
w = YourFace()
x = [0,1,2,3,4,5,6,7,8,9.]
y = [1,2,1,5,-0.00585,7.576,4,6,3,1.]
w.show()
w.DrawyDrawy.putfun(x,y)
sys.exit(app.exec_())