# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 14:56:07 2018

@author: Admin
"""
#draws a single graph


from PyQt5 import QtGui, QtCore, QtWidgets
import numpy as np

#rounding abs to the needed significant figures up and down
def rsfceil(x, sf = 2):
    if x==0.:
        return 0.
    else:
        sf = sf-1
        deg = 10**(np.floor(np.log10(abs(x)))-sf)
        return np.ceil(x/deg)*deg

def rsffloor(x, sf = 2):
    if x==0.:
        return 0.
    else:
        sf = sf-1
        deg = 10**(np.floor(np.log10(abs(x)))-sf)
        return np.floor(x/deg)*deg

#writes down values based on their exponent, Qpainter is a musthave lul
def smartText(QPainter, x, y, w, h, align=0, value=0):
    if value==0.:
        QPainter.drawText(QtCore.QRectF(x,y,w,h),align,"0")
    elif abs(np.floor(np.log10(abs(value))))>2:
        QPainter.drawText(QtCore.QRectF(x,y,w,h),align,'%.2e' % float(value))
    else:
        QPainter.drawText(QtCore.QRectF(x,y,w,h),align,'%.2f' % float(value))

class MyFace(QtWidgets.QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        
        self.Pbegin=1
        self.PointsOnScreen=10
        self.f=np.array([[0,1,2],
                        [1,2,3]])
        self.gap=10
        self.BrushSize=2
    
    def putfun(self, x, y):
        if len(x) == len(y):
            self.f = np.array([x, y])
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
        hdiv=5.     #amount of horizontal grids
        wdiv=10.    #amount of vertical grids
        
        
        lgp = 7.5*gp        #left gap
        rgp = 4*gp          #right
        tgp = 2*gp          #top
        bgp = 3*gp          #bottom
        drawh = h-tgp-bgp   #width of the drawing field
        draww = w-lgp-rgp   #heigth of the drawing field
        ts = 1.5*gp         #textsize
        
        qp=QtGui.QPainter()
        qp.begin(self)
        #pens etc. Pen1 - borderline, pen2 - grids, brush - graph itself
        pen1=QtGui.QPen(QtCore.Qt.black)
        pen2=QtGui.QPen(QtCore.Qt.black,1,QtCore.Qt.PenStyle(QtCore.Qt.DashLine))
        brush=QtGui.QPen(QtCore.Qt.red,BS)
        lett = qp.font(); lett.setPixelSize(ts); qp.setFont(lett)
        
        #normalization
        if POS>len(self.f[0]):
            POS=len(self.f[0])
        maxy = rsfceil(np.max(self.f[1][P0:P0+POS]))
        miny = rsffloor(np.min(self.f[1][P0:P0+POS]))
        maxx = rsfceil(np.max(self.f[0][P0:P0+POS]))
        minx = rsffloor(np.min(self.f[0][P0:P0+POS]))
        
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
        
        #Drawing grids and graph border
        qp.setPen(pen1)
        qp.drawRect(self.rect().adjusted(lgp,tgp,-rgp,-bgp))
        #Small dinguses at min/max y/x
        qp.drawLine(QtCore.QPointF(lgp-gp/4,h-bgp),QtCore.QPointF(lgp,h-bgp))
        qp.drawLine(QtCore.QPointF(lgp-gp/4,tgp),QtCore.QPointF(lgp,tgp))
        qp.drawLine(QtCore.QPointF(lgp,h-bgp),QtCore.QPointF(lgp,h-bgp+gp/4))
        qp.drawLine(QtCore.QPointF(w-rgp,h-bgp),QtCore.QPointF(w-rgp,h-bgp+gp/4))
        #horizontal grids and y text
        for parth in np.arange(1/hdiv, 1, 1/hdiv):
            qp.setPen(pen2)
            hei=drawh*parth+tgp
            q=(QtCore.QPointF(lgp-gp/4,hei),QtCore.QPointF(w-rgp,hei))
            qp.drawLine(q[0],q[1])
            qp.setPen(pen1)
            smartText(qp, gp/2,hei-ts,lgp-gp,ts, QtCore.Qt.AlignRight,
                      (1-parth)*(maxy-miny)+miny)
        
        #writing down min/max y values
        smartText(qp, gp/2,h-bgp-ts,lgp-gp,ts, QtCore.Qt.AlignRight, miny)
        smartText(qp, gp/2,tgp-ts,lgp-gp,ts, QtCore.Qt.AlignRight, maxy)
        
        #vertical grips ant x text
        for partw in np.arange(1/wdiv, 1, 1/wdiv):
            qp.setPen(pen2)
            wid=draww*partw+lgp
            q=(QtCore.QPointF(wid,h-bgp+gp/4),QtCore.QPointF(wid,tgp))
            qp.drawLine(q[0],q[1])
            qp.setPen(pen1)
            smartText(qp, wid,h-bgp+gp/4,ts*6,ts, 0, partw*(maxx-miny)+miny)
        
        #writing down min/max x values
        smartText(qp, lgp,h-bgp+gp/2,ts*6,ts, 0, minx)
        smartText(qp, w-rgp,h-bgp+gp/2,ts*6,ts, 0, maxx)
        
        #Creating arrays for the graph
        x=[(w-rgp-lgp-BS)*fnormx[k]+lgp+BS for k in range(P0,P0+POS)]
        y=[(1.-fnormie[k])*(h-tgp-bgp-BS)+tgp+BS/2 for k in range(P0,P0+POS)]
        pts=[QtCore.QPointF(x[k],y[k]) for k in range(P0,P0+POS)]
        
        #Drawing graph
        qp.setPen(brush)
        for k in range(1,POS):
            qp.drawLine(pts[k-1],pts[k])
        #Job's done!
        qp.end()