#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 00:00:00 2020

@author: Paul Adkisson
"""


import sys

#%% Question 1
# https://doc.qt.io/qt-5/qcolordialog.html
# https://doc.qt.io/qt-5/qcolordialog.html#signals
# https://doc.qt.io/qt-5/qcolordialog.html#colorSelected
# since QColorDialog inherits from QWidget, it has a show method

from PyQt5.QtWidgets import QApplication, QWidget, QColorDialog
from PyQt5.QtGui import QPainter, QColor, QPalette
from random import randint

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.WINDOW_WIDTH = 600
        self.WINDOW_HEIGHT = 400
        self.setGeometry(0, 0, self.WINDOW_WIDTH, self.WINDOW_HEIGHT)
        self.setWindowTitle("HW7 Part 1")
        self.initSqr()
        self.show()
        
    def initSqr(self):
        self.sqr_l = 50
        self.sqr_x = randint(0, self.WINDOW_WIDTH - self.sqr_l)
        self.sqr_y = randint(0, self.WINDOW_HEIGHT - self.sqr_l)
        self.sqr_color = QColor(255, 0, 0)
        
        self.sqr_dialog = QColorDialog(self.sqr_color, self)
        self.sqr_dialog.colorSelected.connect(self.change_sqr_color)
        
    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw_background()
        self.draw_square(qp)
        qp.end()
    
    def draw_background(self):
        white = QColor(255, 255, 255)
        pal = QPalette()
        pal.setColor(QPalette.Background, white)
        self.setPalette(pal)
        
    def draw_square(self, qp):
        qp.setPen(self.sqr_color)
        qp.setBrush(self.sqr_color)
        qp.drawRect(self.sqr_x, self.sqr_y, self.sqr_l, self.sqr_l)
    
    def mousePressEvent(self, e):
        if(e.x() >= self.sqr_x and e.x() <= self.sqr_x + self.sqr_l
           and e.y() >= self.sqr_y and e.y() <= self.sqr_y + self.sqr_l):
            self.in_sqr = True
        else:
            self.in_sqr = False
        self.mouse_pos = [e.x(), e.y()]
                
    def mouseMoveEvent(self, e):
        if(self.in_sqr):
            self.sqr_x += e.x() - self.mouse_pos[0]
            self.sqr_y += e.y() - self.mouse_pos[1]
            self.mouse_pos[0] = e.x()
            self.mouse_pos[1] = e.y()  
        self.update()
        
    def mouseDoubleClickEvent(self, e):
        if(self.in_sqr):
            self.sqr_dialog.show()
        else:
            pass
    
    def change_sqr_color(self):
        self.sqr_color = self.sqr_dialog.selectedColor()
        self.update()

def main():
    app = QApplication([])
    w = MyWidget()
    app.exec_()

if len(sys.argv) == 2 and sys.argv[1] == '1':
    main()


#%% Question 2
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor, QPalette
from PyQt5.QtCore import QTimer, QThread, QEventLoop

class MyTimer(QThread):
    def __init__(self, parent, func, t):
        super().__init__()
        self.func = func
        self.t = t
        
    def run(self):
        timer = QTimer()
        timer.timeout.connect(self.func)
        timer.start(self.t)
        self.exec_()
        

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.initCirc()
        self.initTimer()

    def initUI(self):
        self.WINDOW_WIDTH = 600
        self.WINDOW_HEIGHT = 400
        self.setGeometry(0, 0, self.WINDOW_WIDTH, self.WINDOW_HEIGHT)
        self.setWindowTitle("HW7 Part 2")
        self.initCirc()
        self.show()
        
    def initCirc(self):
        self.DIAMETER = 30
        self.circ_x = self.x()
        self.circ_y = self.y()
        self.circ_color = QColor(255, 0, 0)
        self.circ_vx = 1
        self.circ_vy = 1
        
    def initTimer(self):
        self.timer = MyTimer(self, self.animate, 25)
        self.timer.start()
    
    def closeEvent(self, e):
        #Elegantly closes the timer thread when GUI terminates
        self.timer.quit()
    
    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw_background()
        self.draw_circ(qp)
        qp.end()
        
        #Troubleshooting
        print("circ_x =", self.circ_x)
        print("circ_y =", self.circ_y)
        print("x =", self.x())
        print("y =", self.y())
        
    
    def draw_background(self):
        white = QColor(255, 255, 255)
        pal = QPalette()
        pal.setColor(QPalette.Background, white)
        self.setPalette(pal)
    
    def draw_circ(self, qp):
        qp.setPen(self.circ_color)
        qp.setBrush(self.circ_color)
        qp.drawEllipse(self.circ_x, self.circ_y, self.DIAMETER, self.DIAMETER)
        
    def animate(self):
        self.circ_x += self.circ_vx
        self.circ_y += self.circ_vy
        self.update()
        self.check_collision()
        
        
    def check_collision(self):
        w = self.width()
        h = self.height()
        if(self.circ_x + self.DIAMETER > w):
            print("Ball hit right wall")
            self.circ_vx *= -1
            
        if(self.circ_x < 0):
            print("Ball hit left wall")
            self.circ_vx *= -1
        
        if(self.circ_y + self.DIAMETER > h):
            print("Ball hit ceiling")
            self.circ_vy *= -1
            
        if(self.circ_y < 0):
            print("Ball hit floor")
            self.circ_vy *= -1
        
    

def main():
    app = QApplication([])
    w = MyWidget()
    app.exec_()

if len(sys.argv) == 2 and sys.argv[1] == '2':
    main()