#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore

class GameofLife_GUI(QtGui.QWidget):
    
    def __init__(self):
        super(GameofLife_GUI, self).__init__()
        
        self.initUI()
        
    def initUI(self):
        
        QtGui.QToolTip.setFont(QtGui.QFont('SansSerif', 10))
        
        self.setToolTip('This is a <b>Game Of Life Widget</b>')

	#BUTTONS
	btn = QtGui.QPushButton('porco dio!', self)
        btn.setToolTip('<i> Bestemmiare Aiuta </i>')
        btn.resize(btn.sizeHint())
        btn.move(0, 0)  		

	#QUIT BUTTON        
        qbtn = QtGui.QPushButton('Quit', self)
	qbtn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        qbtn.setToolTip('This is a quit buttonn widget')
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(150,150)
	

	print qbtn.sizeHint()
       
        
        self.setGeometry(0, 0, 250, 150)
        self.setWindowTitle('The Game of Life')    
        self.show()

    def closeEvent(self, event):
        
        reply = QtGui.QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QtGui.QMessageBox.Yes | 
            QtGui.QMessageBox.No, QtGui.QMessageBox.Yes)

        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()    
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = GameofLife_GUI()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
