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
        
        self.Pbegin=1
        self.PointsOnScreen=10
        self.f=np.array([[0,1,2,3,4,5,6,7,8,9.],
                        [1,2,1,5,-4,7,4,6,3,1.]])
        self.gap=10
        self.BrushSize=2
    
    def putfun(self, x, y):
        if len(x) == len(y):
            self.f = np.array(x, y)
        else:
            print("length of x inequal to length of y!")
        return
    
    def paintEvent(self,event):
        
        P0=self.Pbegin-1
        POS=self.PointsOnScreen
        gp=self.gap
        BS=self.BrushSize
        h=self.height()
        w=self.width()
        
        lgp = 3*gp  #left gap
        rgp = gp    #right
        tgp = gp    #top
        bgp = 2*gp  #bottom
        
        qp=QtGui.QPainter()
        qp.begin(self)
        #pens etc
        #For 
        pen1=QtGui.QPen(QtCore.Qt.black)
        pen2=QtGui.QPen(QtCore.Qt.black,1,QtCore.Qt.PenStyle(QtCore.Qt.DashLine))
        #For graph itself
        brush=QtGui.QPen(QtCore.Qt.red,BS)
        
        lett = qp.font()
        lett.setPixelSize(gp*2-2)
        qp.setFont(lett)
        
        #normalization
        if POS>len(self.f[0]):
            POS=len(self.f[0])
        maxy = np.max(self.f[1][P0:P0+POS])
        miny = np.min(self.f[1][P0:P0+POS])
        maxx = np.max(self.f[0][P0:P0+POS])
        minx = np.min(self.f[0][P0:P0+POS])
        #anti division by 0 division
        if maxy == miny:
            miny = np.nan
            if maxy == 0.:
                maxy = np.nan
        
        if maxx == minx:
            minx = np.nan
            if maxx == 0.:
                maxx = np.nan
        
        fnormie = (self.f[1]-miny)/(maxy-miny)
        fnormx = (self.f[0]-minx)/(maxx-minx)
        
        #Рисуем окно для графиков
        qp.setPen(pen1)
        qp.drawRect(self.rect().adjusted(lgp,tgp,-rgp,-bgp))
#        #Рисуем полоски на 0, 0.5 вверх и вниз
#        qp.setPen(pen2)
#        for hei in (h/4, h/2, h*3/4):
#            q=(QtCore.QPointF(gp,hei),QtCore.QPointF(w-gp,hei))
#            qp.drawLine(q[0],q[1])
#        #Рисуем полоски по вертикали, 9 шт
#        for wid in [(w-gp*2)*k/10+gp for k in range(1,10)]:
#            q=(QtCore.QPointF(wid,gp),QtCore.QPointF(wid,h-gp))
#            qp.drawLine(q[0],q[1])
        
        
        #Создаем массивы - графики
        x=[(w-rgp-lgp-BS)*fnormx[k]+lgp+BS for k in range(P0,P0+POS)]
        y=[(1.-fnormie[k])*(h-tgp-bgp-BS)+tgp+BS for k in range(P0,P0+POS)]
        pts=[QtCore.QPointF(x[k],y[k]) for k in range(P0,P0+POS)]

        #Рисуем Графики
        qp.setPen(brush)
        for k in range(1,POS):
            qp.drawLine(pts[k-1],pts[k])
        
        qp.end()