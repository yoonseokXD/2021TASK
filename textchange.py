
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import QTimer, QTime, Qt, QSize, QPoint
from PyQt5.QtGui import QIcon, QTextCursor, QStandardItem, QColor
from datetime import datetime
from mylogger import logger
from QLABEL2 import QLabel_alterada
import random
from setting_device import SettingDeviceUI
import string, sys
from db.database import Database
from db.models import TDEVICE, TCODE
import os, queue


form_class = uic.loadUiType("./ui/Keyboard_ENG.ui")[0]
with open ("/opt/sensorlist.conf", 'r') as data :
	board_data = data.read()

class SettingIPUI(QWidget, form_class):
	db_session = None
	device_info = None
		
	def __init__(self, parent):
		super().__init__()
		self.setupUi(self)
		print(sys.maxunicode)
		self.parent = parent
		self.main_window = parent
		self.board_data = board_data
		print(self.board_data)
		
		self.msg.setWindowTitle("Setting Board")
		self.msg.setText("저장 완료!")

		# 마우스 클릭 이벤트(숫자 입력)
		self.pushButton_E0.clicked.connect(lambda: self.buttonKeyClicked(0))
		self.pushButton_E1.clicked.connect(lambda: self.buttonKeyClicked(1))
		self.pushButton_E2.clicked.connect(lambda: self.buttonKeyClicked(2))
		self.pushButton_E3.clicked.connect(lambda: self.buttonKeyClicked(3))
		self.pushButton_E4.clicked.connect(lambda: self.buttonKeyClicked(4))
		self.pushButton_E5.clicked.connect(lambda: self.buttonKeyClicked(5))
		self.pushButton_E6.clicked.connect(lambda: self.buttonKeyClicked(6))
		self.pushButton_E7.clicked.connect(lambda: self.buttonKeyClicked(7))
		self.pushButton_E8.clicked.connect(lambda: self.buttonKeyClicked(8))
		self.pushButton_E9.clicked.connect(lambda: self.buttonKeyClicked(9))
		self.pushButton_EDEL.clicked.connect(lambda: self.buttonKeyClicked(-1))
		self.pushButton_EQ.clicked.connect(lambda: self.buttonKeyClicked('q'))
		self.pushButton_EW.clicked.connect(lambda: self.buttonKeyClicked('w'))
		self.pushButton_EE.clicked.connect(lambda: self.buttonKeyClicked('e'))
		self.pushButton_ER.clicked.connect(lambda: self.buttonKeyClicked('r'))
		self.pushButton_ET.clicked.connect(lambda: self.buttonKeyClicked('t'))
		self.pushButton_EY.clicked.connect(lambda: self.buttonKeyClicked('y'))
		self.pushButton_EU.clicked.connect(lambda: self.buttonKeyClicked('u'))
		self.pushButton_EI.clicked.connect(lambda: self.buttonKeyClicked('i'))
		self.pushButton_EO.clicked.connect(lambda: self.buttonKeyClicked('o'))
		self.pushButton_EP.clicked.connect(lambda: self.buttonKeyClicked('p'))
		self.pushButton_EA.clicked.connect(lambda: self.buttonKeyClicked('a'))
		self.pushButton_ES.clicked.connect(lambda: self.buttonKeyClicked('s'))
		self.pushButton_ED.clicked.connect(lambda: self.buttonKeyClicked('d'))
		self.pushButton_EF.clicked.connect(lambda: self.buttonKeyClicked('f'))
		self.pushButton_EG.clicked.connect(lambda: self.buttonKeyClicked('g'))
		self.pushButton_EH.clicked.connect(lambda: self.buttonKeyClicked('h'))
		self.pushButton_EJ.clicked.connect(lambda: self.buttonKeyClicked('j'))
		self.pushButton_EK.clicked.connect(lambda: self.buttonKeyClicked('k'))
		self.pushButton_EL.clicked.connect(lambda: self.buttonKeyClicked('l'))
		self.pushButton_EZ.clicked.connect(lambda: self.buttonKeyClicked('z'))
		self.pushButton_EX.clicked.connect(lambda: self.buttonKeyClicked('x'))
		self.pushButton_EC.clicked.connect(lambda: self.buttonKeyClicked('c'))
		self.pushButton_EV.clicked.connect(lambda: self.buttonKeyClicked('v'))
		self.pushButton_EB.clicked.connect(lambda: self.buttonKeyClicked('b'))
		self.pushButton_EN.clicked.connect(lambda: self.buttonKeyClicked('n'))
		self.pushButton_EM.clicked.connect(lambda: self.buttonKeyClicked('m'))
		self.pushButton_SPACE.clicked.connect(lambda: self.buttonKeyClicked(' '))
		self.pushButton_COMMA.clicked.connect(lambda: self.buttonKeyClicked(','))
		#로그인 이벤트 연결
		self.textEdit_board.setFontPointSize(22)
		self.pushButton_SAVE.clicked.connect(self.confirmClicked)
		#self.button_del.setText(u'\u232B')
		self.button_back.clicked.connect(self.backClicked)
		self.textEdit_board.setPlainText(self.board_data)
		
		
	def backClicked(self, event):
		print("backbutton clicked")
		self.backClicked2()

	def backClicked2(self):
		print("backbutton2 clicked")
		self.main_window.main_stackedWidget.addWidget(self.parent)
		self.main_window.main_stackedWidget.setCurrentWidget(self.parent)

		
	def board_Info(self):
		with open ("/opt/sensorlist.conf", 'r') as data :
			self.board_data = data.read()
		
		
		
	def confirmClicked(self, msg):
		with open("/opt/sensorlist.conf", 'w') as data : 
			data.write(self.textEdit_board.toPlainText())
		msg = QMessageBox()
		msg.setIcon(QMessageBox.Information)
		msg.setText("저장 완료")
		msg.setInformativeText('저장 완료')
		msg.exec_()
		
	def buttonKeyClicked(self, val):
		logger.info(val)
		print(self.board_data)
		with open ("/opt/sensorlist.conf", 'r') as data :
			self.board_data = data.read()
			print(self.board_data)
		if(val == -1):
			self.textEdit_board.setPlainText(self.textEdit_board.toPlainText()[:-1])
		else:
			self.textEdit_board.setPlainText(self.textEdit_board.toPlainText() + str(val))
			self.addr = self.textEdit_board.toPlainText()

		
		

		c = self.textEdit_board.textCursor();
		c.movePosition(QTextCursor.End)
		self.textEdit_board.setTextCursor(c);



if __name__ == "__main__":
	app = QApplication(sys.argv)
	mainWindow = SettingIPUI(None)
	mainWindow.show()
	app.exec_()
	