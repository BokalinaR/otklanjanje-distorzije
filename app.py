# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
from numpy import linalg as la
from PIL import Image

def makePicture(P):
    myImage = Image.open('zgrada11.jpg')
    myImage = myImage.resize((int(myImage.size[0]*0.5), int(myImage.size[1]*0.5)))
    width, height = myImage.size

    P_inv = la.inv(P)

    newImage = Image.new('RGB', (width, height), color=1)
    for i in range(width):
        for j in range(height):
            slika = P_inv @ np.array([i, j, 1], dtype=np.int32).T

            x1 = slika[0]
            x2 = slika[1]
            x3 = slika[2]
            
            if x3 != 0:
                x = x1/x3
                y = x2/x3

            if x3 != 0 and int(x) < width and int(y) < height and int(x) >= 0 and int(y) >= 0:
                r, g, b = myImage.getpixel((x, y))

                newImage.putpixel((i, j), (r, g, b))

    newImage.show()

def naivni_algoritam(A, B, C, D):
        A0 = (1, 0, 0)
        B0 = (0, 1, 0)
        C0 = (0, 0, 1)
        D0 = (1, 1, 1)
        
        delta = [ [A[0], B[0], C[0]],
                [A[1], B[1], C[1]],
                [A[2], B[2], C[2]] ]
        
        delta1 = [ [D[0], B[0], C[0]],
                [D[1], B[1], C[1]],
                [D[2], B[2], C[2]] ]
        
    
        delta2 = [ [A[0], D[0], C[0]],
                [A[1], D[1], C[1]],
                [A[2], D[2], C[2]] ]
        
        delta3 = [ [A[0], B[0], D[0]],
                [A[1], B[1], D[1]],
                [A[2], B[2], D[2]] ]
        
        delta_det = la.det(delta)
        delta1_det = la.det(delta1)
        delta2_det = la.det(delta2)
        delta3_det = la.det(delta3)
        
        lambda1 = delta1_det/delta_det
        lambda2 = delta2_det/delta_det
        lambda3 = delta3_det/delta_det
        
    
        P = [[lambda1*x for x in A],
            [lambda2*x for x in B],
            [lambda3*x for x in C]]
        
    
        return np.transpose(P)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(431, 650)
        
        self.points = []
        self.points1 = []
        
    
        self.points1.append([100, 100])
        self.points1.append([310, 100])
        self.points1.append([310, 450])
        self.points1.append([100, 450])
        
        self.A = []
        self.B = []
        self.C = []
        self.D = []

        self.Ap = []
        self.Bp = []
        self.Cp = []
        self.Dp = []

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.image = QtWidgets.QLabel(self.centralwidget)
        self.image.setGeometry(QtCore.QRect(10, 10, 411, 551))
        self.image.setText("")
        self.image.setTextFormat(QtCore.Qt.AutoText)
        self.image.setPixmap(QtGui.QPixmap("zgrada11.jpg"))
        self.image.setScaledContents(True)
        self.image.setObjectName("image")
        self.image.mousePressEvent = self.getPos

        self.button = QtWidgets.QPushButton(MainWindow)
        self.button.setText("Pokrenite algoritam")
        self.button.setGeometry(QtCore.QRect(100, 571, 200, 50))
        self.button.clicked.connect(self.clicked)

        self.msg = QtWidgets.QMessageBox()
        self.msg.setText("Izaberite 4 tacke sa slike")
        self.msg.setIcon(QtWidgets.QMessageBox.Information)
        self.msg.exec_()
     
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def clicked(self):
        #print("You pressed the button")
        #print(self.points)
        self.A = self.points[0]
        self.A.append(1)
        self.B = self.points[1]
        self.B.append(1)
        self.C = self.points[2]
        self.C.append(1)
        self.D = self.points[3]
        self.D.append(1)
        
        self.Ap = self.points1[0]
        self.Ap.append(1)
        self.Bp = self.points1[1]
        self.Bp.append(1)
        self.Cp = self.points1[2]
        self.Cp.append(1)
        self.Dp = self.points1[3]
        self.Dp.append(1)

        P1 = naivni_algoritam(self.A, self.B, self.C, self.D)
        P2 = naivni_algoritam(self.Ap, self.Bp, self.Cp, self.Dp)
        print(np.around(P1, 5))
        print(np.around(P2, 5))

        P1_inv = la.inv(P1)
        P = np.matmul(P2, P1_inv)

        print()
        print("Matrica preslikavanja: ")
        print(np.around(P, 5))        
        makePicture(P)
    

    def getPos(self , event):
        x = event.pos().x()
        y = event.pos().y()
        print(x)
        print(y)
        A = [x, y]
        if(len(self.points) < 4):
            self.points.append(A)
            if(len(self.points) == 4):
                self.msg.setText("Pokrenite algoritam")
                self.msg.setIcon(QtWidgets.QMessageBox.Information)
                self.msg.exec_()

       # print(self.points)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
