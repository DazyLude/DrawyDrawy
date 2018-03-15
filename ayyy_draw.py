# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 14:56:07 2018

@author: Admin
"""
#draws a single graph


from PyQt5 import QtGui, QtCore, QtWidgets
import numpy as np

class MyFace(QtWidgets.QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        
        self.Pbegin=0
        self.PointsOnScreen=10
        self.f=np.array([1,2,1,5,4,7,4,6,3,1.])
        self.gap=10
        self.BrushSize=2
        
    def paintEvent(self,event):
        
        P0=self.Pbegin
        POS=self.PointsOnScreen
        gp=self.gap
        BS=self.BrushSize
        h=self.height()
        w=self.width()
        
        qp=QtGui.QPainter()
        qp.begin(self)
        #Пенал
        #For 
        pen1=QtGui.QPen(QtCore.Qt.black)
        pen2=QtGui.QPen(QtCore.Qt.black,1,QtCore.Qt.PenStyle(QtCore.Qt.DashLine))
        #For graph itself
        brush=QtGui.QPen(QtCore.Qt.red,BS)
        
        lett = qp.font()
        lett.setPixelSize(gp*2-2)
        qp.setFont(lett)
        
        #Нормировка
        im = [np.max(np.abs(self.f[P0:P0+POS]))]
        #не забываем избежать деления на 0
        if im == 0:
            im=np.NaN
        
        #Рисуем окно для графиков
        qp.setPen(pen1)
        qp.drawRect(self.rect().adjusted(gp,gp,-gp,-gp))
        #Рисуем полоски на 0, 0.5 вверх и вниз
        qp.setPen(pen2)
        for hei in (h/4, h/2, h*3/4):
            q=(QtCore.QPointF(gp,hei),QtCore.QPointF(w-gp,hei))
            qp.drawLine(q[0],q[1])
        #Рисуем полоски по вертикали, 9 шт
        for wid in [(w-gp*2)*k/10+gp for k in range(1,10)]:
            q=(QtCore.QPointF(wid,gp),QtCore.QPointF(wid,h-gp))
            qp.drawLine(q[0],q[1])
        
        #Создаем массивы - графики
        x=[(w-gp*2-BS)*k/(POS-1)+gp+BS for k in range(0,POS)]
        y=[(self.f[k+P0]/im[0])*((h-gp*4-2*BS)/4)+h/4 for k in range(0,POS)]
        pts=[QtCore.QPointF(x[k],y[k]) for k in range(0,POS)]

        #Рисуем Графики
        qp.setPen(brush)
        for k in range(1,POS):
            qp.drawLine(pts[k-1],pts[k])
        
        qp.end()
