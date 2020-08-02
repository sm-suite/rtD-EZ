from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtGui import QPalette
from PyQt5.QtCore import Qt


import sys
import numpy as np

ro = lambda x : round(x, ndigits=2)

app = QApplication([])
app.setStyle('Fusion')

win = QMainWindow()
win.setGeometry(0,0,600, 200)
win.setWindowTitle("rtD pre-script v1.5.1")

tpOlabel = QtWidgets.QLabel(win)
tpOlabel.setText("Total Points Low End")
tpOlabel.adjustSize()
tpOlabel.move(95,20)

tpUlabel = QtWidgets.QLabel(win)
tpUlabel.setText("Total Points High End")
tpUlabel.adjustSize()
tpUlabel.move(387,20)



vrlo_lbl = QtWidgets.QLabel(win)
vrlo_lbl.setText('40')
vrlo_lbl.adjustSize()
vrlo_lbl.move(137,55)

vrhi_lbl = QtWidgets.QLabel(win)
vrhi_lbl.setText('50')
vrhi_lbl.adjustSize()
vrhi_lbl.move(437,55)


dvr_lbl = QtWidgets.QLabel(win)
dvr_lbl.setText("Viz Range")
dvr_lbl.adjustSize()
dvr_lbl.move(265,65)


#display viz_rng label low
def dlow():
	vrlo_lbl.setText(str(slider.value()))
	vrlo_lbl.adjustSize()
	vrlo_lbl.setAlignment(Qt.AlignCenter)

def dhigh():
	vrhi_lbl.setText(str(slider2.value()))
	vrhi_lbl.adjustSize()
	vrhi_lbl.setAlignment(Qt.AlignCenter)

def dvr():
	dvr_lbl.setText(str("Viz Range\n"+str(slider.value())+','+str(slider2.value())))
	dvr_lbl.adjustSize()
	dvr_lbl.setAlignment(Qt.AlignCenter)

def vizlow():
	global vizlo
	vizlo = int(slider.value())

def vizhigh():
	global vizhi
	vizhi = 1 + int(slider2.value())





def makevizrng():
	try: viz = np.arange(vizlo, vizhi, 1)
	except: viz = np.arange(0, 11, 1)
	with open('viz_range.txt', 'w') as f:
		for n in range(0,len(viz)): print(viz[n], ",", 'jb', file=f)
	dvr()


def imp_rtD():
	from main1 import gui



but_qu = QtWidgets.QPushButton(win)
but_qu.setText("Quit")
but_qu.clicked.connect(win.close)
but_qu.adjustSize()
but_qu.move(254,130)



slider = QtWidgets.QSlider(Qt.Horizontal, win)
slider.setGeometry(45,80, 200, 50)
slider.setMinimum(30)
slider.setMaximum(50)
slider.setValue(40)
slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
slider.setTickInterval(4)
slider.setSingleStep(10)
slider.valueChanged.connect(dlow)
slider.valueChanged.connect(vizlow)
slider.valueChanged.connect(dhigh)
slider.valueChanged.connect(vizhigh)
slider.valueChanged.connect(makevizrng)


slider2 = QtWidgets.QSlider(Qt.Horizontal, win)
slider2.setGeometry(345, 80, 200, 50)
slider2.setMinimum(40)
slider2.setMaximum(60)
slider2.setValue(50)
slider2.setTickPosition(QtWidgets.QSlider.TicksBelow)
slider2.setTickInterval(4)
slider2.setSingleStep(10)
slider2.valueChanged.connect(dlow)
slider2.valueChanged.connect(vizlow)
slider2.valueChanged.connect(dhigh)
slider2.valueChanged.connect(vizhigh)
slider2.valueChanged.connect(makevizrng)



qpal = QPalette()
qpal.setColor(QPalette.ButtonText, Qt.blue)
app.setPalette(qpal)



win.show()
sys.exit(app.exec_())

if app.exec_ == False:
	from main1 import gui
	gui()
