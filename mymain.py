# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 14:52:34 2018

@author: Admin
"""
#showcase of how to use the widget

import sys
from PyQt5 import QtWidgets
import ayyy_draw as graph


app = QtWidgets.QApplication(sys.argv)
w = graph.YourFace()
x = [0,1,2,3,4,5,6,7,8,9.]
y = [1,2,1,5,-0.00585,7.576,4,6,3,1.]
w.show()
w.DrawyDrawy.putfun(x,y)
sys.exit(app.exec_())