import sys
from PyQt4 import QtGui, QtCore

class porcoWidget(QtGui.QWidget):

    def __init__(self):
        super(porcoWidget, self).__init__()
        self.initUI()

    def initUI(self):
        
        #Actions
        porcodioAction = QtGui.QAction(QtGui.QIcon('farm6.png'), '&Dio', self) 
        porcodioAction.setStatusTip('Bestemmiare Aiuta')                

        #BUTTONS
        btn1 = QtGui.QPushButton('porco dio!', self)
        btn1.setToolTip('<i> Bestemmiare Aiuta </i>')		
        btn2 = QtGui.QPushButton('dio porco', self)
        btn2.setToolTip('<i> Bestemmiare Aiuta sempre di piu\' </i>')		
        
        #LABEL
        lbl1 = QtGui.QLabel('ZetCode', self)
        lbl1.move(15, 10)
        
        #LAYOUT
        hbox = QtGui.QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(btn1)
        hbox.addWidget(btn2)

        vbox = QtGui.QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        self.setLayout(vbox)
        
        #Label absolute position
        
        
        QtGui.QToolTip.setFont(QtGui.QFont('SansSerif', 10))
        self.setToolTip('This is a <b>Game Of Life Widget</b>')
        self.setGeometry(0, 0, 250, 150)
        self.setWindowTitle('Porco')
        
        self.show()

    #centra la finestra principale al centro dello schermo
    def center(self):

        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        print 'cp '+str(cp)
        qr.moveCenter(cp)
        self.move(qr.topLeft())



def main():

    app = QtGui.QApplication(sys.argv)
    ex = porcoWidget()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
