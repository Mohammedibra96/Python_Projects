# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pinConfig.ui'
##
## Created by: Qt User Interface Compiler version 5.14.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import sys,re
import os.path
from pathlib import Path


from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt, SIGNAL)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *
global list
list=[]
class Ui_Form(object):
    def setupUi(self, Form):
        if Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(901, 596)
        Form.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.mainGroup = QGroupBox(Form)
        self.mainGroup.setObjectName(u"mainGroup")
        self.mainGroup.setGeometry(QRect(20, 90, 641, 301))
        self.outGroup = QGroupBox(self.mainGroup)
        self.outGroup.setObjectName(u"outGroup")
        self.outGroup.setGeometry(QRect(310, 40, 301, 71))
        self.highBtn = QRadioButton(self.outGroup)
        self.highBtn.setObjectName(u"highBtn")
        self.highBtn.setGeometry(QRect(20, 30, 97, 20))
        self.lowBtn = QRadioButton(self.outGroup)
        self.lowBtn.setObjectName(u"lowBtn")
        self.lowBtn.setGeometry(QRect(120, 30, 97, 20))
        self.lowBtn.setChecked(True)
        self.inGroup = QGroupBox(self.mainGroup)
        self.inGroup.setObjectName(u"inGroup")
        self.inGroup.setEnabled(False)
        self.inGroup.setGeometry(QRect(310, 130, 301, 71))
        self.pullBtn = QRadioButton(self.inGroup)
        self.pullBtn.setObjectName(u"pullBtn")
        self.pullBtn.setGeometry(QRect(20, 30, 97, 31))
        self.pullBtn.setChecked(True)
        self.impedBtn = QRadioButton(self.inGroup)
        self.impedBtn.setObjectName(u"impedBtn")
        self.impedBtn.setGeometry(QRect(120, 30, 151, 31))
        self.pinNameLbl = QLabel(self.mainGroup)
        self.pinNameLbl.setObjectName(u"pinNameLbl")
        self.pinNameLbl.setGeometry(QRect(40, 200, 101, 31))
        self.pinNameTxt = QLineEdit(self.mainGroup)
        self.pinNameTxt.setObjectName(u"pinNameTxt")
        self.pinNameTxt.setEnabled(False)
        self.pinNameTxt.setGeometry(QRect(40, 240, 231, 31))
        self.pinNameTxt.setStyleSheet(u"")
        self.defaultBtn = QCheckBox(self.mainGroup)
        self.defaultBtn.setObjectName(u"defaultBtn")
        self.defaultBtn.setGeometry(QRect(310, 250, 301, 20))
        self.defaultBtn.setChecked(True)
        self.groupBox = QGroupBox(self.mainGroup)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(40, 40, 221, 161))
        self.outBtn = QRadioButton(self.groupBox)
        self.outBtn.setObjectName(u"outBtn")
        self.outBtn.setGeometry(QRect(20, 30, 97, 20))
        self.outBtn.setChecked(True)
        self.inBtn = QRadioButton(self.groupBox)
        self.inBtn.setObjectName(u"inBtn")
        self.inBtn.setGeometry(QRect(20, 110, 97, 20))
        self.pathLbl = QLabel(Form)
        self.pathLbl.setObjectName(u"pathLbl")
        self.pathLbl.setGeometry(QRect(30, 400, 131, 21))
        self.pathTxt = QLineEdit(Form)
        self.pathTxt.setObjectName(u"pathTxt")
        self.pathTxt.setGeometry(QRect(20, 440, 641, 41))
        self.CreateButton = QPushButton(Form)
        self.CreateButton.setObjectName(u"CreateButton")
        self.CreateButton.setGeometry(QRect(20, 500, 181, 41))
        self.CreateButton.setStyleSheet(u"color: rgb(35, 35, 35);\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.PinSelect_comboBox = QComboBox(Form)
        self.PinSelect_comboBox.addItem(str())
        self.PinSelect_comboBox.addItem(str())
        self.PinSelect_comboBox.addItem(str())
        self.PinSelect_comboBox.addItem(str())
        self.PinSelect_comboBox.addItem(str())
        self.PinSelect_comboBox.addItem(str())
        self.PinSelect_comboBox.addItem(str())
        self.PinSelect_comboBox.addItem(str())
        self.PinSelect_comboBox.addItem(str())
        self.PinSelect_comboBox.addItem(str())
        self.PinSelect_comboBox.addItem(str())
        self.PinSelect_comboBox.addItem(str())
        self.PinSelect_comboBox.addItem(str())
        self.PinSelect_comboBox.addItem(str())
        self.PinSelect_comboBox.addItem(str())
        self.PinSelect_comboBox.addItem(str())
        self.PinSelect_comboBox.addItem(str())
        self.PinSelect_comboBox.addItem(str())
        self.PinSelect_comboBox.addItem(str())
        self.PinSelect_comboBox.addItem(str())
        self.PinSelect_comboBox.addItem(str())
        self.PinSelect_comboBox.addItem(str())
        self.PinSelect_comboBox.setObjectName(u"PinSelect_comboBox")
        self.PinSelect_comboBox.setGeometry(QRect(100, 20, 92, 26))
        self.SelectButton = QPushButton(Form)
        self.SelectButton.setObjectName(u"SelectButton")
        self.SelectButton.setGeometry(QRect(460, 20, 112, 34))
        self.LoadButton = QPushButton(Form)
        self.LoadButton.setObjectName(u"LoadButton")
        self.LoadButton.setGeometry(QRect(250, 500, 181, 41))
        self.LoadButton.setStyleSheet(u"color: rgb(35, 35, 35);\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.SaveButton = QPushButton(Form)
        self.SaveButton.setObjectName(u"SaveButton")
        self.SaveButton.setGeometry(QRect(480, 500, 181, 41))
        self.SaveButton.setStyleSheet(u"color: rgb(35, 35, 35);\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.ConfigDisplay = QTextBrowser(Form)
        self.ConfigDisplay.setObjectName(u"ConfigDisplay")
        self.ConfigDisplay.setGeometry(QRect(670, 100, 211, 421))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(670, 80, 141, 16))

        self.retranslateUi(Form)

        QObject.connect(self.outBtn, SIGNAL("clicked(bool)"), self.inGroup.setDisabled )
        QObject.connect(self.inBtn, SIGNAL("clicked(bool)"), self.outGroup.setDisabled )
        QObject.connect(self.outBtn, SIGNAL("clicked(bool)"), self.outGroup.setEnabled )
        QObject.connect(self.inBtn, SIGNAL("clicked(bool)"), self.inGroup.setEnabled )
        
        QObject.connect(self.defaultBtn, SIGNAL("clicked(bool)"), self.pinNameTxt.setDisabled )

        self.SelectButton.clicked.connect(self.SelectBtnHandler)
        self.CreateButton.clicked.connect(self.CreateBtnHandler)
        self.SaveButton.clicked.connect(self.SaveBtnHandler)
        self.LoadButton.clicked.connect(self.LoadBtnHandler)
        
        
        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.mainGroup.setTitle(QCoreApplication.translate("Form", u"Pin 0", None))
        self.outGroup.setTitle(QCoreApplication.translate("Form", u"Output Level", None))
        self.highBtn.setText(QCoreApplication.translate("Form", u"High", None))
        self.lowBtn.setText(QCoreApplication.translate("Form", u"Low", None))
        self.inGroup.setTitle(QCoreApplication.translate("Form", u"Input Configuration", None))
        self.pullBtn.setText(QCoreApplication.translate("Form", u"Pull-up", None))
        self.impedBtn.setText(QCoreApplication.translate("Form", u"High Impedance", None))
        self.pinNameLbl.setText(QCoreApplication.translate("Form", u"Pin Name", None))
        self.pinNameTxt.setText(QCoreApplication.translate("Form", u"Enter Pin Value", None))
        self.defaultBtn.setText(QCoreApplication.translate("Form", u"Use Default Name", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"Mode", None))
        self.outBtn.setText(QCoreApplication.translate("Form", u"Output", None))
        self.inBtn.setText(QCoreApplication.translate("Form", u"Input", None))
        self.pathLbl.setText(QCoreApplication.translate("Form", u"Output Path", None))
        self.CreateButton.setText(QCoreApplication.translate("Form", u"Creat New", None))
        self.PinSelect_comboBox.setItemText(0, QCoreApplication.translate("Form", u"Pin0", None))
        self.PinSelect_comboBox.setItemText(1, QCoreApplication.translate("Form", u"Pin9", None))
        self.PinSelect_comboBox.setItemText(2, QCoreApplication.translate("Form", u"Pin10", None))
        self.PinSelect_comboBox.setItemText(3, QCoreApplication.translate("Form", u"Pin11", None))
        self.PinSelect_comboBox.setItemText(4, QCoreApplication.translate("Form", u"Pin12", None))
        self.PinSelect_comboBox.setItemText(5, QCoreApplication.translate("Form", u"Pin13", None))
        self.PinSelect_comboBox.setItemText(6, QCoreApplication.translate("Form", u"Pin14", None))
        self.PinSelect_comboBox.setItemText(7, QCoreApplication.translate("Form", u"Pin15", None))
        self.PinSelect_comboBox.setItemText(8, QCoreApplication.translate("Form", u"Pin16", None))
        self.PinSelect_comboBox.setItemText(9, QCoreApplication.translate("Form", u"Pin17", None))
        self.PinSelect_comboBox.setItemText(10, QCoreApplication.translate("Form", u"Pin18", None))
        self.PinSelect_comboBox.setItemText(11, QCoreApplication.translate("Form", u"Pin19", None))
        self.PinSelect_comboBox.setItemText(12, QCoreApplication.translate("Form", u"Pin20", None))
        self.PinSelect_comboBox.setItemText(13, QCoreApplication.translate("Form", u"Pin21", None))
        self.PinSelect_comboBox.setItemText(14, QCoreApplication.translate("Form", u"Pin1", None))
        self.PinSelect_comboBox.setItemText(15, QCoreApplication.translate("Form", u"Pin2", None))
        self.PinSelect_comboBox.setItemText(16, QCoreApplication.translate("Form", u"Pin3", None))
        self.PinSelect_comboBox.setItemText(17, QCoreApplication.translate("Form", u"Pin4", None))
        self.PinSelect_comboBox.setItemText(18, QCoreApplication.translate("Form", u"Pin5", None))
        self.PinSelect_comboBox.setItemText(19, QCoreApplication.translate("Form", u"Pin6", None))
        self.PinSelect_comboBox.setItemText(20, QCoreApplication.translate("Form", u"Pin7", None))
        self.PinSelect_comboBox.setItemText(21, QCoreApplication.translate("Form", u"Pin8", None))

        self.SelectButton.setText(QCoreApplication.translate("Form", u"Select", None))
        self.LoadButton.setText(QCoreApplication.translate("Form", u"Load", None))
        self.SaveButton.setText(QCoreApplication.translate("Form", u"Save", None))
        self.ConfigDisplay.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("Form", u"Selected Configuratons", None))
    # retranslateUi
    
    def SelectBtnHandler(self,Form):
      print (list)
      for i in range(0,len(list)-1,4):
        if self.PinSelect_comboBox.currentText()== list[i]:
          #list.pop()
          #list.pop()
          #list.pop()
          #list.pop()
          del list[i:i+4]
          break
      list.append(self.PinSelect_comboBox.currentText())
      name=str(self.PinSelect_comboBox.currentText())
      if self.outBtn.isChecked():
        if self.highBtn.isChecked():
          list.append("HIGH")
          status="HIGH"
        else:
            list.append("LOW")
            status="LOW"
        list.append("Output")
        dir="OUTPUT"
      else:
        if self.pullBtn.isChecked():
          list.append("PULLUP")
          status="PULLUP"
        else:
          list.append("HIGH_IMPEDENCE")
          status="HIGH_IMPEDENCE"
        list.append("Input")
        dir="INPUT"
      x=self.PinSelect_comboBox.currentText()
      if self.defaultBtn.isChecked():
         list.append("#define DIO_"+self.PinSelect_comboBox.currentText()+'    '+str(x[3:]))
      else:
        list.append("#define "+self.pinNameTxt.text()+'    '+str(x[3:]))
      #self.ConfigDisplay.append(name+'   '+dir+'_'+status)
      self.ConfigDisplay.clear()
      for i in range(0,len(list)-1,4):
        print(i)
        self.ConfigDisplay.append(list[i]+'   '+list[i+2]+'_'+list[i+1])
      #print(list)
    
    def CreateBtnHandler(self):
      for i in range(0,len(list)-1,4):
        if self.pathTxt.text() == '':
          print('Yabny ekteb PATH!')
          return
        MFIC_Handler = open(self.pathTxt.text() + '\MFIC.h', 'a')
        DIO_Handler = open(self.pathTxt.text() + '\DIO_config.h', 'a')
        if list[i+2] == 'Output':
          if list[i+1]=='HIGH':
            DIO_Handler.write('#define DIO_'+str(list[i])+'_MODE    DIO_HIGH\n')
          else:
            DIO_Handler.write('#define DIO_'+str(list[i])+'_MODE    DIO_LOW\n')
        else:
          if list[i+1]=='PULLUP':
            DIO_Handler.write('#define DIO_'+str(list[i])+'_MODE    DIO_PULLUP\n')
          else:
            DIO_Handler.write('#define DIO_'+str(list[i])+'_MODE    DIO_HIGH_IMPEDENCE\n')
        
        MFIC_Handler.write(str(list[i+3])+'\n')
      MFIC_Handler.close()
      DIO_Handler.close()
      
    def SaveBtnHandler(self):
      if Path(self.pathTxt.text() + '\Configuratons.txt').is_file():
        print("File is exist")
        os.remove(self.pathTxt.text() + '\Configuratons.txt')
      for i in range(0,len(list)-1,4):
        if self.pathTxt.text() == '':
          print('Yabny ekteb PATH!')
          return
        cfg_Handler = open(self.pathTxt.text() + '\Configuratons.txt', 'a')
        
        if list[i+2] == 'Output':
          if list[i+1]=='HIGH':
            cfg_Handler.write('#define DIO_'+str(list[i])+'_MODE    DIO_HIGH\n')
          else:
            cfg_Handler.write('#define DIO_'+str(list[i])+'_MODE    DIO_LOW\n')
        else:
          if list[i+1]=='PULLUP':
            cfg_Handler.write('#define DIO_'+str(list[i])+'_MODE    DIO_PULLUP\n')
          else:
            cfg_Handler.write('#define DIO_'+str(list[i])+'_MODE    DIO_HIGH_IMPEDENCE\n')
      cfg_Handler.close()
      
    def LoadBtnHandler(self):
      self.ConfigDisplay.clear()
      if self.pathTxt.text() == '':
        print('Yabny ekteb PATH!')
        return
      load_Handler = open(self.pathTxt.text() + '\Configuratons.txt', 'r+')
      read_list = load_Handler.readlines()
      for line in read_list:
        line=line.rstrip('\n')
        split_line=line.split('_')
        name=split_line[1]
        status=split_line[3]
        if status == 'HIGH' or 'LOW':
          dir='OUTPUT'
        else:
          dir='INPUT'
        list.append(name)
        list.append(status)
        list.append(dir)
        if self.defaultBtn.isChecked():
          list.append("#define DIO_"+name+'    '+str(name[3:]))
        else:
          list.append("#define "+name+'    '+str(name[3:]))

        self.ConfigDisplay.append(name+'   '+dir+'_'+status)
      
        #print(status)

app = QApplication(sys.argv)
Widget = QWidget()
Form = Ui_Form()
Form.setupUi(Widget)
Widget.show()
sys.exit(app.exec_())