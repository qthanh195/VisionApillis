# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QStackedWidget, QWidget)

from utils.config import topEdgeDistance, sideEdgeDistance,tolerance

class Ui_Widget(object):
        
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(1920, 1080)
        self.stackedWidget_Page = QStackedWidget(Widget)
        self.stackedWidget_Page.setObjectName(u"stackedWidget_Page")
        self.stackedWidget_Page.setGeometry(QRect(0, -13, 1920, 1080))
        self.stackedWidget_Page.setStyleSheet(u"")
        self.page_Operation = QWidget()
        self.page_Operation.setObjectName(u"page_Operation")
        self.page_Operation.setStyleSheet(u"QWidget#page_Operation {\n"
"                background-image: url('E:/2. GE/21. Apillis/ui/anh_ui/bg0.jpg');\n"
"                background-repeat: no-repeat;\n"
"                background-position: center;\n"
"                \n"
"            }")
        self.pushButton_Start = QPushButton(self.page_Operation)
        self.pushButton_Start.setObjectName(u"pushButton_Start")
        self.pushButton_Start.setEnabled(True)
        self.pushButton_Start.setGeometry(QRect(227, 943, 297, 71))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.pushButton_Start.setFont(font)
        self.pushButton_Start.setStyleSheet(u"QPushButton {\n"
"    background-color: #3498db;\n"
"    border: none;\n"
"    color: white;\n"
"    padding: 10px 20px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    font-size: 26px;\n"
"    margin: 4px 2px;\n"
"    transition-duration: 0.4s;\n"
"    cursor: pointer;\n"
"    border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #2980b9;\n"
"    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #2980b9;\n"
"    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);\n"
"    transform: translateY(2px);\n"
"}")
        self.pushButton_Stop = QPushButton(self.page_Operation)
        self.pushButton_Stop.setObjectName(u"pushButton_Stop")
        self.pushButton_Stop.setEnabled(True)
        self.pushButton_Stop.setGeometry(QRect(604, 943, 297, 71))
        self.pushButton_Stop.setFont(font)
        self.pushButton_Stop.setStyleSheet(u"QPushButton {\n"
"    background-color: #3498db;\n"
"    border: none;\n"
"    color: white;\n"
"    padding: 10px 20px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    font-size: 26px;\n"
"    margin: 4px 2px;\n"
"    transition-duration: 0.4s;\n"
"    cursor: pointer;\n"
"    border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #2980b9;\n"
"    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #2980b9;\n"
"    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);\n"
"    transform: translateY(2px);\n"
"}")
        self.pushButton_Reset = QPushButton(self.page_Operation)
        self.pushButton_Reset.setObjectName(u"pushButton_Reset")
        self.pushButton_Reset.setEnabled(True)
        self.pushButton_Reset.setGeometry(QRect(975, 943, 297, 71))
        self.pushButton_Reset.setFont(font)
        self.pushButton_Reset.setStyleSheet(u"QPushButton {\n"
"    background-color: #3498db;\n"
"    border: none;\n"
"    color: white;\n"
"    padding: 10px 20px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    font-size: 26px;\n"
"    margin: 4px 2px;\n"
"    transition-duration: 0.4s;\n"
"    cursor: pointer;\n"
"    border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #2980b9;\n"
"    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #2980b9;\n"
"    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);\n"
"    transform: translateY(2px);\n"
"}")
        self.lineEdit_P2 = QLineEdit(self.page_Operation)
        self.lineEdit_P2.setObjectName(u"lineEdit_P2")
        self.lineEdit_P2.setGeometry(QRect(357, 66, 167, 43))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setBold(True)
        self.lineEdit_P2.setFont(font1)
        self.lineEdit_P2.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #000000;\n"
"    border-radius:4px;\n"
"    padding: 8px;\n"
"    font-size: 22px;\n"
"    background-color: #ecf0f1;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #2980b9;\n"
"    background-color: #ffffff;\n"
"}")
        self.lineEdit_P2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_P1 = QLineEdit(self.page_Operation)
        self.lineEdit_P1.setObjectName(u"lineEdit_P1")
        self.lineEdit_P1.setGeometry(QRect(674, 67, 167, 43))
        self.lineEdit_P1.setFont(font1)
        self.lineEdit_P1.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #000000;\n"
"    border-radius:4px;\n"
"    padding: 8px;\n"
"    font-size: 22px;\n"
"    background-color: #ecf0f1;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #2980b9;\n"
"    background-color: #ffffff;\n"
"}")
        self.lineEdit_P1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_P4 = QLineEdit(self.page_Operation)
        self.lineEdit_P4.setObjectName(u"lineEdit_P4")
        self.lineEdit_P4.setGeometry(QRect(961, 183, 167, 43))
        self.lineEdit_P4.setFont(font1)
        self.lineEdit_P4.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #000000;\n"
"    border-radius:4px;\n"
"    padding: 8px;\n"
"    font-size: 22px;\n"
"    background-color: #ecf0f1;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #2980b9;\n"
"    background-color: #ffffff;\n"
"}")
        self.lineEdit_P4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_P3 = QLineEdit(self.page_Operation)
        self.lineEdit_P3.setObjectName(u"lineEdit_P3")
        self.lineEdit_P3.setGeometry(QRect(961, 444, 167, 43))
        self.lineEdit_P3.setFont(font1)
        self.lineEdit_P3.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #000000;\n"
"    border-radius:4px;\n"
"    padding: 8px;\n"
"    font-size: 22px;\n"
"    background-color: #ecf0f1;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #2980b9;\n"
"    background-color: #ffffff;\n"
"}")
        self.lineEdit_P3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_P5 = QLineEdit(self.page_Operation)
        self.lineEdit_P5.setObjectName(u"lineEdit_P5")
        self.lineEdit_P5.setGeometry(QRect(80, 444, 167, 43))
        self.lineEdit_P5.setFont(font1)
        self.lineEdit_P5.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #000000;\n"
"    border-radius:4px;\n"
"    padding: 8px;\n"
"    font-size: 22px;\n"
"    background-color: #ecf0f1;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #2980b9;\n"
"    background-color: #ffffff;\n"
"}")
        self.lineEdit_P5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_P6 = QLineEdit(self.page_Operation)
        self.lineEdit_P6.setObjectName(u"lineEdit_P6")
        self.lineEdit_P6.setGeometry(QRect(80, 184, 167, 43))
        self.lineEdit_P6.setFont(font1)
        self.lineEdit_P6.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #000000;\n"
"    border-radius:4px;\n"
"    padding: 8px;\n"
"    font-size: 22px;\n"
"    background-color: #ecf0f1;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #2980b9;\n"
"    background-color: #ffffff;\n"
"}")
        self.lineEdit_P6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_Top = QLineEdit(self.page_Operation)
        self.lineEdit_Top.setObjectName(u"lineEdit_Top")
        self.lineEdit_Top.setGeometry(QRect(471, 685, 167, 44))
        self.lineEdit_Top.setFont(font1)
        self.lineEdit_Top.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #000000;\n"
"    border-radius:4px;\n"
"    padding: 8px;\n"
"    font-size: 22px;\n"
"    background-color: #ecf0f1;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #2980b9;\n"
"    background-color: #ffffff;\n"
"}")
        self.lineEdit_Top.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_Side = QLineEdit(self.page_Operation)
        self.lineEdit_Side.setObjectName(u"lineEdit_Side")
        self.lineEdit_Side.setGeometry(QRect(471, 752, 167, 44))
        self.lineEdit_Side.setFont(font1)
        self.lineEdit_Side.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #000000;\n"
"    border-radius:4px;\n"
"    padding: 8px;\n"
"    font-size: 22px;\n"
"    background-color: #ecf0f1;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #2980b9;\n"
"    background-color: #ffffff;\n"
"}")
        self.lineEdit_Side.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_Tolerance = QLineEdit(self.page_Operation)
        self.lineEdit_Tolerance.setObjectName(u"lineEdit_Tolerance")
        self.lineEdit_Tolerance.setGeometry(QRect(471, 820, 167, 44))
        self.lineEdit_Tolerance.setFont(font1)
        self.lineEdit_Tolerance.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #000000;\n"
"    border-radius:4px;\n"
"    padding: 8px;\n"
"    font-size: 22px;\n"
"    background-color: #ecf0f1;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #2980b9;\n"
"    background-color: #ffffff;\n"
"}")
        self.lineEdit_Tolerance.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_passed = QLineEdit(self.page_Operation)
        self.lineEdit_passed.setObjectName(u"lineEdit_passed")
        self.lineEdit_passed.setGeometry(QRect(1175, 685, 167, 44))
        self.lineEdit_passed.setFont(font1)
        self.lineEdit_passed.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #000000;\n"
"    border-radius:4px;\n"
"    padding: 8px;\n"
"    font-size: 22px;\n"
"    background-color: #ecf0f1;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #2980b9;\n"
"    background-color: #ffffff;\n"
"}")
        self.lineEdit_passed.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_Total = QLineEdit(self.page_Operation)
        self.lineEdit_Total.setObjectName(u"lineEdit_Total")
        self.lineEdit_Total.setGeometry(QRect(1175, 752, 167, 44))
        self.lineEdit_Total.setFont(font1)
        self.lineEdit_Total.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #000000;\n"
"    border-radius:4px;\n"
"    padding: 8px;\n"
"    font-size: 22px;\n"
"    background-color: #ecf0f1;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #2980b9;\n"
"    background-color: #ffffff;\n"
"}")
        self.lineEdit_Total.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_Serial = QLineEdit(self.page_Operation)
        self.lineEdit_Serial.setObjectName(u"lineEdit_Serial")
        self.lineEdit_Serial.setGeometry(QRect(1175, 820, 167, 44))
        self.lineEdit_Serial.setFont(font1)
        self.lineEdit_Serial.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #000000;\n"
"    border-radius:4px;\n"
"    padding: 8px;\n"
"    font-size: 22px;\n"
"    background-color: #ecf0f1;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #2980b9;\n"
"    background-color: #ffffff;\n"
"}")
        self.lineEdit_Serial.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.frame_Cam1 = QFrame(self.page_Operation)
        self.frame_Cam1.setObjectName(u"frame_Cam1")
        self.frame_Cam1.setGeometry(QRect(277, 127, 649, 434))
        self.frame_Cam1.setStyleSheet(u"QFrame {\n"
"    border: 3px solid red;\n"
"	border-radius: 5px;\n"
"    background-color: transparent;\n"
"}\n"
"")
        self.frame_Cam1.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_Cam1.setFrameShadow(QFrame.Shadow.Raised)
        self.label_Cam1 = QLabel(self.frame_Cam1)
        self.label_Cam1.setObjectName(u"label_Cam1")
        self.label_Cam1.setGeometry(QRect(5, 5, 640, 425))
        self.label_Cam1.setStyleSheet(u"QLabel {\n"
"    border: 2px ;\n"
"\n"
"}")
        self.label_Status1 = QLabel(self.page_Operation)
        self.label_Status1.setObjectName(u"label_Status1")
        self.label_Status1.setGeometry(QRect(53, 1017, 171, 51))
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(24)
        self.label_Status1.setFont(font2)
        self.label_Status1.setStyleSheet(u"QLabel{\n"
"	color: red;\n"
"}")
        self.label_PassFail = QLabel(self.page_Operation)
        self.label_PassFail.setObjectName(u"label_PassFail")
        self.label_PassFail.setGeometry(QRect(1250, 260, 211, 81))
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(54)
        font3.setBold(True)
        self.label_PassFail.setFont(font3)
        self.label_PassFail.setStyleSheet(u"QLabel{\n"
"	color: GREEN;\n"
"}")
        self.pushButton_5 = QPushButton(self.page_Operation)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setEnabled(True)
        self.pushButton_5.setGeometry(QRect(1510, 105, 412, 111))
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet(u"QPushButton {\n"
"    background-color: #2980b9;\n"
"    border: 2px solid #2980b9;\n"
"    color: Black;\n"
"    padding: 10px 20px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    font-size: 30px;\n"
"    margin: 4px 2px;\n"
"    transition-duration: 0.4s;\n"
"    cursor: pointer;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #2980b9;\n"
"    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #2980b9;\n"
"    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);\n"
"    transform: translateY(2px);\n"
"}")
        self.pushButton_5.setCheckable(False)
        self.pushButton_5.setAutoRepeat(False)
        self.pushButton_Calibration = QPushButton(self.page_Operation)
        self.pushButton_Calibration.setObjectName(u"pushButton_Calibration")
        self.pushButton_Calibration.setEnabled(True)
        self.pushButton_Calibration.setGeometry(QRect(1510, 207, 412, 111))
        self.pushButton_Calibration.setFont(font)
        self.pushButton_Calibration.setStyleSheet(u"QPushButton {\n"
"	 border: 2px solid #2980b9;\n"
"    background-color: white;\n"
"    color: Black;\n"
"    padding: 10px 20px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    font-size: 30px;\n"
"    margin: 4px 2px;\n"
"    transition-duration: 0.4s;\n"
"    cursor: pointer;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #2980b9;\n"
"    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #2980b9;\n"
"    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);\n"
"    transform: translateY(2px);\n"
"}")
        self.pushButton_DataLog1 = QPushButton(self.page_Operation)
        self.pushButton_DataLog1.setObjectName(u"pushButton_DataLog1")
        self.pushButton_DataLog1.setEnabled(True)
        self.pushButton_DataLog1.setGeometry(QRect(1510, 309, 412, 111))
        self.pushButton_DataLog1.setFont(font)
        self.pushButton_DataLog1.setStyleSheet(u"QPushButton {\n"
"    background-color: white;\n"
"    border: 2px solid #2980b9;\n"
"    color: Black;\n"
"    padding: 10px 20px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    font-size: 30px;\n"
"    margin: 4px 2px;\n"
"    transition-duration: 0.4s;\n"
"    cursor: pointer;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #2980b9;\n"
"    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #2980b9;\n"
"    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);\n"
"    transform: translateY(2px);\n"
"}")
        self.label_Time1 = QLabel(self.page_Operation)
        self.label_Time1.setObjectName(u"label_Time1")
        self.label_Time1.setGeometry(QRect(1510, 40, 411, 51))
        font4 = QFont()
        font4.setFamilies([u"Arial"])
        font4.setPointSize(22)
        self.label_Time1.setFont(font4)
        self.label_Time1.setStyleSheet(u"QLabel{\n"
"	color: black;\n"
"}")
        self.label_Time1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.stackedWidget_Page.addWidget(self.page_Operation)
        self.page_Calibration = QWidget()
        self.page_Calibration.setObjectName(u"page_Calibration")
        self.page_Calibration.setStyleSheet(u"QWidget #page_Calibration{\n"
"                background-image: url('E:/2. GE/21. Apillis/ui/anh_ui/bg1.jpg');\n"
"                background-repeat: no-repeat;\n"
"                background-position: center;\n"
"                background-size: cover;\n"
"            }")
        self.pushButton_DataLog2 = QPushButton(self.page_Calibration)
        self.pushButton_DataLog2.setObjectName(u"pushButton_DataLog2")
        self.pushButton_DataLog2.setEnabled(True)
        self.pushButton_DataLog2.setGeometry(QRect(1510, 309, 412, 111))
        self.pushButton_DataLog2.setFont(font)
        self.pushButton_DataLog2.setStyleSheet(u"QPushButton {\n"
"    background-color: white;\n"
"    border: 2px solid #2980b9;\n"
"    color: Black;\n"
"    padding: 10px 20px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    font-size: 30px;\n"
"    margin: 4px 2px;\n"
"    transition-duration: 0.4s;\n"
"    cursor: pointer;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #2980b9;\n"
"    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #2980b9;\n"
"    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);\n"
"    transform: translateY(2px);\n"
"}")
        self.pushButton_Operation = QPushButton(self.page_Calibration)
        self.pushButton_Operation.setObjectName(u"pushButton_Operation")
        self.pushButton_Operation.setEnabled(True)
        self.pushButton_Operation.setGeometry(QRect(1510, 105, 412, 111))
        self.pushButton_Operation.setFont(font)
        self.pushButton_Operation.setStyleSheet(u"QPushButton {\n"
"    background-color: white;\n"
"    border: 2px solid #2980b9;\n"
"    color: Black;\n"
"    padding: 10px 20px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    font-size: 30px;\n"
"    margin: 4px 2px;\n"
"    transition-duration: 0.4s;\n"
"    cursor: pointer;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #2980b9;\n"
"    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #2980b9;\n"
"    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);\n"
"    transform: translateY(2px);\n"
"}")
        self.pushButton_Operation.setCheckable(False)
        self.pushButton_Operation.setAutoRepeat(False)
        self.pushButton_Calibration_2 = QPushButton(self.page_Calibration)
        self.pushButton_Calibration_2.setObjectName(u"pushButton_Calibration_2")
        self.pushButton_Calibration_2.setEnabled(True)
        self.pushButton_Calibration_2.setGeometry(QRect(1510, 207, 412, 111))
        self.pushButton_Calibration_2.setFont(font)
        self.pushButton_Calibration_2.setStyleSheet(u"QPushButton {\n"
"    background-color: #2980b9;\n"
"    border: 2px solid #2980b9;\n"
"    color: Black;\n"
"    padding: 10px 20px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    font-size: 30px;\n"
"    margin: 4px 2px;\n"
"    transition-duration: 0.4s;\n"
"    cursor: pointer;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #2980b9;\n"
"    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #2980b9;\n"
"    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);\n"
"    transform: translateY(2px);\n"
"}")
        self.label_Cam2 = QLabel(self.page_Calibration)
        self.label_Cam2.setObjectName(u"label_Cam2")
        self.label_Cam2.setGeometry(QRect(281, 130, 640, 425))
        self.label_Cam2.setStyleSheet(u"")
        self.lineEdit_PixelFormat = QLineEdit(self.page_Calibration)
        self.lineEdit_PixelFormat.setObjectName(u"lineEdit_PixelFormat")
        self.lineEdit_PixelFormat.setGeometry(QRect(472, 679, 167, 44))
        self.lineEdit_PixelFormat.setFont(font1)
        self.lineEdit_PixelFormat.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #000000;\n"
"    border-radius:4px;\n"
"    padding: 8px;\n"
"    font-size: 22px;\n"
"    background-color: #ecf0f1;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #2980b9;\n"
"    background-color: #ffffff;\n"
"}")
        self.lineEdit_PixelFormat.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_ModeExposure = QLineEdit(self.page_Calibration)
        self.lineEdit_ModeExposure.setObjectName(u"lineEdit_ModeExposure")
        self.lineEdit_ModeExposure.setGeometry(QRect(472, 754, 167, 44))
        self.lineEdit_ModeExposure.setFont(font1)
        self.lineEdit_ModeExposure.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #000000;\n"
"    border-radius:4px;\n"
"    padding: 8px;\n"
"    font-size: 22px;\n"
"    background-color: #ecf0f1;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #2980b9;\n"
"    background-color: #ffffff;\n"
"}")
        self.lineEdit_ModeExposure.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_ModeBalance = QLineEdit(self.page_Calibration)
        self.lineEdit_ModeBalance.setObjectName(u"lineEdit_ModeBalance")
        self.lineEdit_ModeBalance.setGeometry(QRect(472, 830, 167, 44))
        self.lineEdit_ModeBalance.setFont(font1)
        self.lineEdit_ModeBalance.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #000000;\n"
"    border-radius:4px;\n"
"    padding: 8px;\n"
"    font-size: 22px;\n"
"    background-color: #ecf0f1;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #2980b9;\n"
"    background-color: #ffffff;\n"
"}")
        self.lineEdit_ModeBalance.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_Exposure = QLineEdit(self.page_Calibration)
        self.lineEdit_Exposure.setObjectName(u"lineEdit_Exposure")
        self.lineEdit_Exposure.setGeometry(QRect(1175, 679, 167, 44))
        self.lineEdit_Exposure.setFont(font1)
        self.lineEdit_Exposure.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #000000;\n"
"    border-radius:4px;\n"
"    padding: 8px;\n"
"    font-size: 22px;\n"
"    background-color: #ecf0f1;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #2980b9;\n"
"    background-color: #ffffff;\n"
"}")
        self.lineEdit_Exposure.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_Status2 = QLabel(self.page_Calibration)
        self.label_Status2.setObjectName(u"label_Status2")
        self.label_Status2.setGeometry(QRect(53, 1017, 171, 51))
        self.label_Status2.setFont(font2)
        self.label_Status2.setStyleSheet(u"QLabel{\n"
"	color: green;\n"
"}")
        self.lineEdit_Gain = QLineEdit(self.page_Calibration)
        self.lineEdit_Gain.setObjectName(u"lineEdit_Gain")
        self.lineEdit_Gain.setGeometry(QRect(1175, 754, 167, 44))
        self.lineEdit_Gain.setFont(font1)
        self.lineEdit_Gain.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #000000;\n"
"    border-radius:4px;\n"
"    padding: 8px;\n"
"    font-size: 22px;\n"
"    background-color: #ecf0f1;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #2980b9;\n"
"    background-color: #ffffff;\n"
"}")
        self.lineEdit_Gain.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_FrameRate = QLineEdit(self.page_Calibration)
        self.lineEdit_FrameRate.setObjectName(u"lineEdit_FrameRate")
        self.lineEdit_FrameRate.setGeometry(QRect(1175, 830, 167, 44))
        self.lineEdit_FrameRate.setFont(font1)
        self.lineEdit_FrameRate.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #000000;\n"
"    border-radius:4px;\n"
"    padding: 8px;\n"
"    font-size: 22px;\n"
"    background-color: #ecf0f1;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #2980b9;\n"
"    background-color: #ffffff;\n"
"}")
        self.lineEdit_FrameRate.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.pushButton_OpenCamera = QPushButton(self.page_Calibration)
        self.pushButton_OpenCamera.setObjectName(u"pushButton_OpenCamera")
        self.pushButton_OpenCamera.setEnabled(True)
        self.pushButton_OpenCamera.setGeometry(QRect(1128, 128, 297, 71))
        self.pushButton_OpenCamera.setFont(font)
        self.pushButton_OpenCamera.setStyleSheet(u"QPushButton {\n"
"    background-color: #3498db;\n"
"    border: none;\n"
"    color: white;\n"
"    padding: 10px 20px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    font-size: 26px;\n"
"    margin: 4px 2px;\n"
"    transition-duration: 0.4s;\n"
"    cursor: pointer;\n"
"    border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #2980b9;\n"
"    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #2980b9;\n"
"    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);\n"
"    transform: translateY(2px);\n"
"}")
        self.pushButton_StartCalibration = QPushButton(self.page_Calibration)
        self.pushButton_StartCalibration.setObjectName(u"pushButton_StartCalibration")
        self.pushButton_StartCalibration.setEnabled(True)
        self.pushButton_StartCalibration.setGeometry(QRect(1128, 229, 297, 71))
        self.pushButton_StartCalibration.setFont(font)
        self.pushButton_StartCalibration.setStyleSheet(u"QPushButton {\n"
"    background-color: #3498db;\n"
"    border: none;\n"
"    color: white;\n"
"    padding: 10px 20px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    font-size: 26px;\n"
"    margin: 4px 2px;\n"
"    transition-duration: 0.4s;\n"
"    cursor: pointer;\n"
"    border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #2980b9;\n"
"    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #2980b9;\n"
"    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);\n"
"    transform: translateY(2px);\n"
"}")
        self.label_Time2 = QLabel(self.page_Calibration)
        self.label_Time2.setObjectName(u"label_Time2")
        self.label_Time2.setGeometry(QRect(1510, 40, 411, 51))
        self.label_Time2.setFont(font4)
        self.label_Time2.setStyleSheet(u"QLabel{\n"
"	color: black;\n"
"}")
        self.label_Time2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.frame_Cam2 = QFrame(self.page_Calibration)
        self.frame_Cam2.setObjectName(u"frame_Cam2")
        self.frame_Cam2.setGeometry(QRect(452, 245, 297, 197))
        self.frame_Cam2.setStyleSheet(u"QFrame {\n"
"    border: 3px solid green;\n"
"	 border-radius: 10px;\n"
"    background-color: transparent;\n"
"}\n"
"")
        self.frame_Cam2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_Cam2.setFrameShadow(QFrame.Shadow.Raised)
        self.stackedWidget_Page.addWidget(self.page_Calibration)

        self.retranslateUi(Widget)

        self.stackedWidget_Page.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.pushButton_Start.setText(QCoreApplication.translate("Widget", u"Start", None))
        self.pushButton_Stop.setText(QCoreApplication.translate("Widget", u"Stop", None))
        self.pushButton_Reset.setText(QCoreApplication.translate("Widget", u"Reset", None))
        self.lineEdit_P2.setText(QCoreApplication.translate("Widget", u"0.00", None))
        self.lineEdit_P1.setText(QCoreApplication.translate("Widget", u"0.00", None))
        self.lineEdit_P4.setText(QCoreApplication.translate("Widget", u"0.00", None))
        self.lineEdit_P3.setText(QCoreApplication.translate("Widget", u"0.00", None))
        self.lineEdit_P5.setText(QCoreApplication.translate("Widget", u"0.00", None))
        self.lineEdit_P6.setText(QCoreApplication.translate("Widget", u"0.00", None))
        self.lineEdit_Top.setText(QCoreApplication.translate("Widget", f"{topEdgeDistance:.2f}", None))
        self.lineEdit_Side.setText(QCoreApplication.translate("Widget", f"{sideEdgeDistance:.2f}", None))
        self.lineEdit_Tolerance.setText(QCoreApplication.translate("Widget", f"{tolerance:.2f}", None))
        self.lineEdit_passed.setText(QCoreApplication.translate("Widget", u"0", None))
        self.lineEdit_Total.setText(QCoreApplication.translate("Widget", u"0", None))
        self.lineEdit_Serial.setText(QCoreApplication.translate("Widget", u"0", None))
        self.label_Cam1.setText("")
        self.label_Status1.setText(QCoreApplication.translate("Widget", u"Stop", None))
        self.label_PassFail.setText(QCoreApplication.translate("Widget", u"", None))
        self.pushButton_5.setText(QCoreApplication.translate("Widget", u"Operation", None))
        self.pushButton_Calibration.setText(QCoreApplication.translate("Widget", u"Calibration", None))
        self.pushButton_DataLog1.setText(QCoreApplication.translate("Widget", u"Data Log", None))
        self.label_Time1.setText(QCoreApplication.translate("Widget", u"19 - 05 - 2000", None))
        self.pushButton_DataLog2.setText(QCoreApplication.translate("Widget", u"Data Log", None))
        self.pushButton_Operation.setText(QCoreApplication.translate("Widget", u"Operation", None))
        self.pushButton_Calibration_2.setText(QCoreApplication.translate("Widget", u"Calibration", None))
        self.label_Cam2.setText("")
        self.lineEdit_PixelFormat.setText(QCoreApplication.translate("Widget", u"Mono8", None))
        self.lineEdit_ModeExposure.setText(QCoreApplication.translate("Widget", u"Once", None))
        self.lineEdit_ModeBalance.setText(QCoreApplication.translate("Widget", u"Once", None))
        self.lineEdit_Exposure.setText(QCoreApplication.translate("Widget", u"525", None))
        self.label_Status2.setText(QCoreApplication.translate("Widget", u"Running...", None))
        self.lineEdit_Gain.setText(QCoreApplication.translate("Widget", u"0.0", None))
        self.lineEdit_FrameRate.setText(QCoreApplication.translate("Widget", u"14", None))
        self.pushButton_OpenCamera.setText(QCoreApplication.translate("Widget", u"Open Camera", None))
        self.pushButton_StartCalibration.setText(QCoreApplication.translate("Widget", u"Start Calibration", None))
        self.label_Time2.setText(QCoreApplication.translate("Widget", u"19 - 05 - 2000", None))
    # retranslateUi

