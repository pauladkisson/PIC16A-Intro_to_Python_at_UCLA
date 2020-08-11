#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on June 10, 2020

@author: Paul Adkisson
"""

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor, QPalette

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('My Final Widget')
        self.setGeometry(0, 0, 600, 400)
        self.initPoly()
        self.show()
        
    def initPoly(self):
        self.vertices = []
        self.poly_color = QColor(0, 0, 255)
        self.closed = False
        
    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw_background()
        self.draw_poly(qp)
        qp.end()
        
    def draw_background(self):
        WHITE = QColor(255, 255, 255)
        pal = QPalette()
        pal.setColor(QPalette.Background, WHITE)
        self.setPalette(pal)
        
    def draw_poly(self, qp):
        qp.setPen(self.poly_color)
        qp.setBrush(self.poly_color)
        for v in range(len(self.vertices)-1):
            qp.drawLine(self.vertices[v][0], self.vertices[v][1], self.vertices[v+1][0], self.vertices[v+1][1])
            
        if self.closed:
            qp.drawLine(self.vertices[0][0], self.vertices[0][1], self.vertices[-1][0], self.vertices[-1][1])
        
        
    def mousePressEvent(self, e):
        if self.closed:
            self.vertices = [[e.x(), e.y()]]
            self.closed = False
        else:
            self.vertices.append([e.x(), e.y()])
        self.update()
        
    def mouseDoubleClickEvent(self, e):
        self.closed = True
        self.update()
        


def main():
    app = QApplication([])
    w = MyWidget()
    app.exec_()

main()