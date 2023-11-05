# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLayout, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QStackedWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)
from .resources_rc import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1091, 832)
        MainWindow.setMinimumSize(QSize(940, 670))
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"outline: none;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(0, 170, 255);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {	\n"
"	background-color: rgb(40, 44, 52);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"#reg_form .QFrame {\n"
"background-color: rgb(0, 170, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
""
                        "Left Menu */\n"
"#leftMenuBg {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#topLogo {\n"
"	background-color: rgb(33, 37, 43);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"#username_label {\n"
"color: rgb(0, 170, 255)\n"
"}\n"
"#titleLeftApp { font: 63 14pt \"Segoe UI Semibold\"; }\n"
"#titleLeftDescription { font: 8pt \"Segoe UI\"; color: rgb(0, 170, 255); }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Page Database */\n"
"#label_db { font: 63 12pt \"Segoe UI Semibold\"; }\n"
"\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#topMenu .QPushButton:pressed {	\n"
"	background-color: rgb(0, 170, "
                        "255);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#bottomMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {	\n"
"	background-color: rgb(0, 170, 255);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: rgb(37, 41, 48);\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: rgb(113, 126, 149);\n"
"}\n"
"#toggleButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#toggleButton:pressed {\n"
"	background-color: rgb(0, 170, 25"
                        "5);\n"
"}\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"#extraLeftBox {	\n"
"	background-color: rgb(44, 49, 58);\n"
"}\n"
"#extraTopBg{	\n"
"	background-color: rgb(0, 170, 255)\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/icons/images/icons/cil-comment-bubble.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(0, 170, 255); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: rgb(0, 170, 255); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#extraContent{\n"
"	border-top: 3px sol"
                        "id rgb(40, 44, 52);\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {	\n"
"	background-color: rgb(0, 170, 255);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#settingsTopBtn {\n"
"background-image: url(:/icons/images/icons/cil-user.png);\n"
"background-repeat: none;\n"
"background-position: center;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#contentBottom{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255"
                        ", 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-style: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: rgb(44, 49, 58); }\n"
"#themeSettingsTopDetail { background-color: rgb(0, 170, 255); }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: rgb(44, 49, 58); }\n"
"#bottomBar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"#contentSettings .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 24px;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"	backgroun"
                        "d-color: rgb(40, 44, 52);\n"
"}\n"
"#contentSettings .QPushButton:pressed {	\n"
"	background-color: rgb(0, 170, 255);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(90, 90, 90);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"	border-left: none;\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(0, 170, 255);\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(33, 37, 43);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHead"
                        "er {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 3px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(90, 90, 90);\n"
"}\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(0, 107, 200);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding:"
                        " 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(0, 170, 255);\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(0, 170, 255);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::handle:horizontal:hover {\n"
"	background-color: rgb(0, 221, 255);\n"
"}\n"
"QScrollBar::handle:horizontal:pressed {\n"
"	background-color: rgb(0, 107, 200);\n"
"}\n"
"QScrollBar::add-l"
                        "ine:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(0, 170, 255);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
""
                        " }\n"
" QScrollBar::handle:vertical:hover {	\n"
"	background-color: rgb(0, 221, 255);\n"
" }\n"
" QScrollBar::handle:vertical:pressed {	\n"
"	background-color: rgb(0, 107, 200);\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* ////////////////////////////////////////////////////////////////////////"
                        "/////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	background-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
""
                        "\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"    background-color: rgb(46, 51, 61);\n"
"    border: 2px solid rgb(22, 26, 35);\n"
"	border-radius: 4px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox:focus{\n"
"	border: 2px solid rgb(188, 188, 189);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox::drop-down:hover {\n"
"	background-color: rgb(74, 82, 97);\n"
" }\n"
"QComboBox QAbstractItemView {	\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(33, 37, 43);\n"
""
                        "	padding: 10px;\n"
"	selection-background-color: rgb(0, 170, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(0, 170, 255);\n"
"    border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"	background-color: rgb(0, 221, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"	background-color: rgb(0, 107, 200);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76)"
                        ";\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(0, 170, 255);\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"	background-color: rgb(0, 221, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"	background-color: rgb(0, 107, 200);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"QCommandLinkButton {	\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	color: rgb(0, 170, 255);\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(0, 210, 255);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(0, 110, 255);\n"
"	background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"#pagesContainer QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
""
                        "	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"")
        self.verticalLayout_19 = QVBoxLayout(self.styleSheet)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setFrameShape(QFrame.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Raised)
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(60, 9, 160, 20))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Semibold"])
        font1.setPointSize(14)
        font1.setBold(False)
        font1.setItalic(False)
        self.titleLeftApp.setFont(font1)
        self.titleLeftApp.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.username_label = QLabel(self.topLogoInfo)
        self.username_label.setObjectName(u"username_label")
        self.username_label.setGeometry(QRect(60, 28, 160, 24))
        self.username_label.setMinimumSize(QSize(0, 24))
        self.username_label.setMaximumSize(QSize(16777215, 15))
        self.username_label.setFont(font)
        self.username_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_3 = QLabel(self.topLogoInfo)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(6, 3, 51, 51))
        self.label_3.setStyleSheet(u"background-image: url(:/images/images/images/logo_1_44.png);\n"
"background-repeat: none;")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setFrameShape(QFrame.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy)
        self.toggleButton.setMinimumSize(QSize(0, 45))
        self.toggleButton.setFont(font)
        self.toggleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LeftToRight)
        self.toggleButton.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_menu.png);")

        self.verticalLayout_4.addWidget(self.toggleButton)


        self.verticalMenuLayout.addWidget(self.toggleBox)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setStyleSheet(u"QPushButton:disabled {\n"
"color: rgb(113, 126, 133);\n"
"}")
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.topMenu)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy)
        self.btn_home.setMinimumSize(QSize(0, 45))
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setLayoutDirection(Qt.LeftToRight)
        self.btn_home.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-home.png);")

        self.verticalLayout_8.addWidget(self.btn_home)

        self.btn_scan = QPushButton(self.topMenu)
        self.btn_scan.setObjectName(u"btn_scan")
        self.btn_scan.setEnabled(False)
        sizePolicy.setHeightForWidth(self.btn_scan.sizePolicy().hasHeightForWidth())
        self.btn_scan.setSizePolicy(sizePolicy)
        self.btn_scan.setMinimumSize(QSize(0, 45))
        self.btn_scan.setFont(font)
        self.btn_scan.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_scan.setLayoutDirection(Qt.LeftToRight)
        self.btn_scan.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-find-in-page.png);")

        self.verticalLayout_8.addWidget(self.btn_scan)

        self.btn_database = QPushButton(self.topMenu)
        self.btn_database.setObjectName(u"btn_database")
        self.btn_database.setEnabled(False)
        sizePolicy.setHeightForWidth(self.btn_database.sizePolicy().hasHeightForWidth())
        self.btn_database.setSizePolicy(sizePolicy)
        self.btn_database.setMinimumSize(QSize(0, 45))
        self.btn_database.setFont(font)
        self.btn_database.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_database.setLayoutDirection(Qt.LeftToRight)
        self.btn_database.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-layers.png);")

        self.verticalLayout_8.addWidget(self.btn_database)


        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignTop)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setFrameShape(QFrame.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.btn_help = QPushButton(self.bottomMenu)
        self.btn_help.setObjectName(u"btn_help")
        sizePolicy.setHeightForWidth(self.btn_help.sizePolicy().hasHeightForWidth())
        self.btn_help.setSizePolicy(sizePolicy)
        self.btn_help.setMinimumSize(QSize(0, 45))
        self.btn_help.setFont(font)
        self.btn_help.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_help.setLayoutDirection(Qt.LeftToRight)
        self.btn_help.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-chat-bubble.png);")

        self.verticalLayout_9.addWidget(self.btn_help)


        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignBottom)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.extraLeftBox = QFrame(self.bgApp)
        self.extraLeftBox.setObjectName(u"extraLeftBox")
        self.extraLeftBox.setMinimumSize(QSize(0, 0))
        self.extraLeftBox.setMaximumSize(QSize(0, 16777215))
        self.extraLeftBox.setFrameShape(QFrame.NoFrame)
        self.extraLeftBox.setFrameShadow(QFrame.Raised)
        self.extraColumLayout = QVBoxLayout(self.extraLeftBox)
        self.extraColumLayout.setSpacing(0)
        self.extraColumLayout.setObjectName(u"extraColumLayout")
        self.extraColumLayout.setContentsMargins(0, 0, 0, 0)
        self.extraTopBg = QFrame(self.extraLeftBox)
        self.extraTopBg.setObjectName(u"extraTopBg")
        self.extraTopBg.setMinimumSize(QSize(0, 50))
        self.extraTopBg.setMaximumSize(QSize(16777215, 50))
        self.extraTopBg.setFrameShape(QFrame.NoFrame)
        self.extraTopBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.extraTopBg)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.extraTopLayout = QGridLayout()
        self.extraTopLayout.setObjectName(u"extraTopLayout")
        self.extraTopLayout.setHorizontalSpacing(10)
        self.extraTopLayout.setVerticalSpacing(0)
        self.extraTopLayout.setContentsMargins(10, -1, 10, -1)
        self.extraIcon = QFrame(self.extraTopBg)
        self.extraIcon.setObjectName(u"extraIcon")
        self.extraIcon.setMinimumSize(QSize(20, 0))
        self.extraIcon.setMaximumSize(QSize(20, 20))
        self.extraIcon.setFrameShape(QFrame.NoFrame)
        self.extraIcon.setFrameShadow(QFrame.Raised)

        self.extraTopLayout.addWidget(self.extraIcon, 0, 0, 1, 1)

        self.extraLabel = QLabel(self.extraTopBg)
        self.extraLabel.setObjectName(u"extraLabel")
        self.extraLabel.setMinimumSize(QSize(150, 0))

        self.extraTopLayout.addWidget(self.extraLabel, 0, 1, 1, 1)

        self.extraCloseColumnBtn = QPushButton(self.extraTopBg)
        self.extraCloseColumnBtn.setObjectName(u"extraCloseColumnBtn")
        self.extraCloseColumnBtn.setMinimumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setMaximumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.extraCloseColumnBtn.setIcon(icon)
        self.extraCloseColumnBtn.setIconSize(QSize(20, 20))

        self.extraTopLayout.addWidget(self.extraCloseColumnBtn, 0, 2, 1, 1)


        self.verticalLayout_5.addLayout(self.extraTopLayout)


        self.extraColumLayout.addWidget(self.extraTopBg)

        self.extraContent = QFrame(self.extraLeftBox)
        self.extraContent.setObjectName(u"extraContent")
        self.extraContent.setFrameShape(QFrame.NoFrame)
        self.extraContent.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.extraContent)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.extraTopMenu = QFrame(self.extraContent)
        self.extraTopMenu.setObjectName(u"extraTopMenu")
        self.extraTopMenu.setFrameShape(QFrame.NoFrame)
        self.extraTopMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.extraTopMenu)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_12.addWidget(self.extraTopMenu, 0, Qt.AlignTop)

        self.extraCenter = QFrame(self.extraContent)
        self.extraCenter.setObjectName(u"extraCenter")
        self.extraCenter.setFrameShape(QFrame.NoFrame)
        self.extraCenter.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.extraCenter)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")

        self.verticalLayout_12.addWidget(self.extraCenter)

        self.extraBottom = QFrame(self.extraContent)
        self.extraBottom.setObjectName(u"extraBottom")
        self.extraBottom.setFrameShape(QFrame.NoFrame)
        self.extraBottom.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.extraBottom)


        self.extraColumLayout.addWidget(self.extraContent)


        self.appLayout.addWidget(self.extraLeftBox)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.settingsTopBtn = QPushButton(self.rightButtons)
        self.settingsTopBtn.setObjectName(u"settingsTopBtn")
        self.settingsTopBtn.setMinimumSize(QSize(28, 28))
        self.settingsTopBtn.setMaximumSize(QSize(28, 28))
        self.settingsTopBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.settingsTopBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.settingsTopBtn)

        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon1)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font2)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon2)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeAppBtn.setIcon(icon)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, 10, 10, 10)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.stackedWidget.setFrameShadow(QFrame.Plain)
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        self.home_page.setStyleSheet(u"#home_page {\n"
"background-image: url(:/images/images/images/logo_1_transperent.png);\n"
"background-repeat: none;\n"
"background-position: center;\n"
"}\n"
"")
        self.verticalLayout_18 = QVBoxLayout(self.home_page)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_3 = QFrame(self.home_page)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.frame_3, 0, 0, 1, 1)


        self.verticalLayout_18.addLayout(self.gridLayout)

        self.stackedWidget.addWidget(self.home_page)
        self.scan_page = QWidget()
        self.scan_page.setObjectName(u"scan_page")
        self.scan_page.setStyleSheet(u"#scan_page {\n"
"background-image: url(:/images/images/images/logo_1_transperent.png);\n"
"background-repeat: none;\n"
"background-position: center;\n"
"}\n"
"#scan_page QPushButton {\n"
"background-color: rgb(32, 36, 45);\n"
"background-repeat: none;\n"
"background-position: center left;\n"
"border: none;\n"
"font: 63 12pt \"Segoe UI Semibold\";\n"
"}\n"
"#scan_page QPushButton:hover {\n"
"background-color:qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0.0511364 rgba(0, 170, 255, 255), stop:0.0852273 rgb(32, 36, 45));\n"
"}\n"
"#scan_page QPushButton:pressed {\n"
"background-color: rgb(0, 170, 255);\n"
"}\n"
"QLineEdit {\n"
"background-color: rgb(46, 51, 61);\n"
"border: 2px solid rgb(22, 26, 35);\n"
"font: 63 13pt \"Segoe UI Semibold\";\n"
"}\n"
"QLineEdit:focus {\n"
"border: 2px solid rgb(188, 188, 189);\n"
"}\n"
"QLabel {\n"
"font: 63 10pt \"Segoe UI Semibold\";\n"
"}")
        self.verticalLayout = QVBoxLayout(self.scan_page)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 0)
        self.search_frame = QFrame(self.scan_page)
        self.search_frame.setObjectName(u"search_frame")
        self.search_frame.setMinimumSize(QSize(0, 80))
        self.search_frame.setMaximumSize(QSize(16777215, 80))
        self.search_frame.setCursor(QCursor(Qt.ArrowCursor))
        self.search_frame.setFrameShape(QFrame.StyledPanel)
        self.search_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.search_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SetMaximumSize)
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.search_line = QLineEdit(self.search_frame)
        self.search_line.setObjectName(u"search_line")
        self.search_line.setMinimumSize(QSize(0, 50))
        self.search_line.setMaximumSize(QSize(16777215, 50))

        self.horizontalLayout_3.addWidget(self.search_line)

        self.folder_open_button = QPushButton(self.search_frame)
        self.folder_open_button.setObjectName(u"folder_open_button")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.folder_open_button.sizePolicy().hasHeightForWidth())
        self.folder_open_button.setSizePolicy(sizePolicy1)
        self.folder_open_button.setMinimumSize(QSize(90, 35))
        self.folder_open_button.setBaseSize(QSize(0, 0))
        self.folder_open_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.folder_open_button.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.folder_open_button.setIcon(icon3)

        self.horizontalLayout_3.addWidget(self.folder_open_button)


        self.verticalLayout.addWidget(self.search_frame)

        self.data_passport_frame = QFrame(self.scan_page)
        self.data_passport_frame.setObjectName(u"data_passport_frame")
        self.data_passport_frame.setMinimumSize(QSize(0, 500))
        self.data_passport_frame.setFrameShape(QFrame.StyledPanel)
        self.data_passport_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.data_passport_frame)
        self.verticalLayout_17.setSpacing(8)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 8, 0, 0)
        self.f_i_o_frame = QFrame(self.data_passport_frame)
        self.f_i_o_frame.setObjectName(u"f_i_o_frame")
        self.f_i_o_frame.setFrameShape(QFrame.StyledPanel)
        self.f_i_o_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.f_i_o_frame)
        self.gridLayout_3.setSpacing(10)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.gridLayout_3.setContentsMargins(8, 0, 115, 0)
        self.label_i = QLabel(self.f_i_o_frame)
        self.label_i.setObjectName(u"label_i")

        self.gridLayout_3.addWidget(self.label_i, 0, 1, 1, 1)

        self.line_i = QLineEdit(self.f_i_o_frame)
        self.line_i.setObjectName(u"line_i")
        self.line_i.setMinimumSize(QSize(0, 40))
        self.line_i.setMaximumSize(QSize(16777215, 40))
        self.line_i.setMaxLength(16)

        self.gridLayout_3.addWidget(self.line_i, 1, 1, 1, 1)

        self.label_o = QLabel(self.f_i_o_frame)
        self.label_o.setObjectName(u"label_o")

        self.gridLayout_3.addWidget(self.label_o, 0, 2, 1, 1)

        self.line_o = QLineEdit(self.f_i_o_frame)
        self.line_o.setObjectName(u"line_o")
        self.line_o.setMinimumSize(QSize(0, 40))
        self.line_o.setMaximumSize(QSize(16777215, 40))
        self.line_o.setMaxLength(16)

        self.gridLayout_3.addWidget(self.line_o, 1, 2, 1, 1)

        self.label_f = QLabel(self.f_i_o_frame)
        self.label_f.setObjectName(u"label_f")
        self.label_f.setMinimumSize(QSize(0, 14))
        self.label_f.setMaximumSize(QSize(16777215, 14))

        self.gridLayout_3.addWidget(self.label_f, 0, 0, 1, 1)

        self.line_f = QLineEdit(self.f_i_o_frame)
        self.line_f.setObjectName(u"line_f")
        self.line_f.setMinimumSize(QSize(0, 40))
        self.line_f.setMaximumSize(QSize(16777215, 40))
        self.line_f.setMaxLength(16)

        self.gridLayout_3.addWidget(self.line_f, 1, 0, 1, 1)

        self.line_born_date = QLineEdit(self.f_i_o_frame)
        self.line_born_date.setObjectName(u"line_born_date")
        self.line_born_date.setMinimumSize(QSize(0, 40))
        self.line_born_date.setMaximumSize(QSize(16777215, 40))
        self.line_born_date.setMaxLength(16)

        self.gridLayout_3.addWidget(self.line_born_date, 3, 0, 1, 1)

        self.label_4 = QLabel(self.f_i_o_frame)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_3.addWidget(self.label_4, 2, 1, 1, 1)

        self.line_born_place = QLineEdit(self.f_i_o_frame)
        self.line_born_place.setObjectName(u"line_born_place")
        self.line_born_place.setMinimumSize(QSize(0, 40))
        self.line_born_place.setMaximumSize(QSize(16777215, 40))
        self.line_born_place.setMaxLength(16)

        self.gridLayout_3.addWidget(self.line_born_place, 3, 1, 1, 1)

        self.label_5 = QLabel(self.f_i_o_frame)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_3.addWidget(self.label_5, 2, 2, 1, 1)

        self.line_male = QLineEdit(self.f_i_o_frame)
        self.line_male.setObjectName(u"line_male")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.line_male.sizePolicy().hasHeightForWidth())
        self.line_male.setSizePolicy(sizePolicy2)
        self.line_male.setMinimumSize(QSize(0, 40))
        self.line_male.setMaximumSize(QSize(80, 40))
        self.line_male.setSizeIncrement(QSize(0, 0))
        self.line_male.setBaseSize(QSize(0, 0))
        self.line_male.setMaxLength(4)

        self.gridLayout_3.addWidget(self.line_male, 3, 2, 1, 1)

        self.label = QLabel(self.f_i_o_frame)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 14))
        self.label.setMaximumSize(QSize(16777215, 14))

        self.gridLayout_3.addWidget(self.label, 2, 0, 1, 1)


        self.verticalLayout_17.addWidget(self.f_i_o_frame)

        self.passport_frame = QFrame(self.data_passport_frame)
        self.passport_frame.setObjectName(u"passport_frame")
        self.passport_frame.setMaximumSize(QSize(16777215, 80))
        self.passport_frame.setFrameShape(QFrame.StyledPanel)
        self.passport_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.passport_frame)
        self.gridLayout_5.setSpacing(10)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.gridLayout_5.setContentsMargins(8, 0, 0, 0)
        self.label_serial = QLabel(self.passport_frame)
        self.label_serial.setObjectName(u"label_serial")
        self.label_serial.setMinimumSize(QSize(0, 14))
        self.label_serial.setMaximumSize(QSize(16777215, 14))

        self.gridLayout_5.addWidget(self.label_serial, 0, 0, 1, 1)

        self.label_number = QLabel(self.passport_frame)
        self.label_number.setObjectName(u"label_number")

        self.gridLayout_5.addWidget(self.label_number, 0, 1, 1, 1)

        self.label_given_code = QLabel(self.passport_frame)
        self.label_given_code.setObjectName(u"label_given_code")

        self.gridLayout_5.addWidget(self.label_given_code, 0, 3, 1, 1)

        self.label_given_date = QLabel(self.passport_frame)
        self.label_given_date.setObjectName(u"label_given_date")

        self.gridLayout_5.addWidget(self.label_given_date, 0, 2, 1, 1)

        self.line_number = QLineEdit(self.passport_frame)
        self.line_number.setObjectName(u"line_number")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.line_number.sizePolicy().hasHeightForWidth())
        self.line_number.setSizePolicy(sizePolicy3)
        self.line_number.setMinimumSize(QSize(20, 40))
        self.line_number.setMaximumSize(QSize(80, 40))
        self.line_number.setMaxLength(6)

        self.gridLayout_5.addWidget(self.line_number, 1, 1, 1, 1)

        self.line_given_date = QLineEdit(self.passport_frame)
        self.line_given_date.setObjectName(u"line_given_date")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.line_given_date.sizePolicy().hasHeightForWidth())
        self.line_given_date.setSizePolicy(sizePolicy4)
        self.line_given_date.setMinimumSize(QSize(20, 40))
        self.line_given_date.setMaximumSize(QSize(150, 40))
        self.line_given_date.setMaxLength(10)

        self.gridLayout_5.addWidget(self.line_given_date, 1, 2, 1, 1)

        self.line_serial = QLineEdit(self.passport_frame)
        self.line_serial.setObjectName(u"line_serial")
        sizePolicy3.setHeightForWidth(self.line_serial.sizePolicy().hasHeightForWidth())
        self.line_serial.setSizePolicy(sizePolicy3)
        self.line_serial.setMinimumSize(QSize(20, 40))
        self.line_serial.setMaximumSize(QSize(60, 40))
        self.line_serial.setMaxLength(4)

        self.gridLayout_5.addWidget(self.line_serial, 1, 0, 1, 1)

        self.line_given_code = QLineEdit(self.passport_frame)
        self.line_given_code.setObjectName(u"line_given_code")
        sizePolicy3.setHeightForWidth(self.line_given_code.sizePolicy().hasHeightForWidth())
        self.line_given_code.setSizePolicy(sizePolicy3)
        self.line_given_code.setMinimumSize(QSize(20, 40))
        self.line_given_code.setMaximumSize(QSize(125, 40))
        self.line_given_code.setMaxLength(7)

        self.gridLayout_5.addWidget(self.line_given_code, 1, 3, 1, 1)


        self.verticalLayout_17.addWidget(self.passport_frame)

        self.given_frame = QFrame(self.data_passport_frame)
        self.given_frame.setObjectName(u"given_frame")
        self.given_frame.setMaximumSize(QSize(16777215, 223))
        self.given_frame.setFrameShape(QFrame.StyledPanel)
        self.given_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.given_frame)
        self.verticalLayout_16.setSpacing(10)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_16.setContentsMargins(8, 0, 115, 0)
        self.given_label = QLabel(self.given_frame)
        self.given_label.setObjectName(u"given_label")
        self.given_label.setMaximumSize(QSize(16777215, 14))

        self.verticalLayout_16.addWidget(self.given_label)

        self.line_given = QLineEdit(self.given_frame)
        self.line_given.setObjectName(u"line_given")
        sizePolicy5 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.line_given.sizePolicy().hasHeightForWidth())
        self.line_given.setSizePolicy(sizePolicy5)
        self.line_given.setMinimumSize(QSize(0, 40))
        self.line_given.setMaximumSize(QSize(10000, 40))

        self.verticalLayout_16.addWidget(self.line_given)

        self.label_scan = QLabel(self.given_frame)
        self.label_scan.setObjectName(u"label_scan")
        self.label_scan.setMinimumSize(QSize(0, 14))
        self.label_scan.setMaximumSize(QSize(16777215, 14))
        self.label_scan.setStyleSheet(u"font: 10pt \"Segoe UI\";")

        self.verticalLayout_16.addWidget(self.label_scan, 0, Qt.AlignTop)

        self.scan_buttons_frame = QFrame(self.given_frame)
        self.scan_buttons_frame.setObjectName(u"scan_buttons_frame")
        self.scan_buttons_frame.setMinimumSize(QSize(0, 140))
        self.scan_buttons_frame.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(32, 36, 45);\n"
"border: none;\n"
"font: 63 12pt \"Segoe UI Semibold\";\n"
"padding: default;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0.0511364 rgba(0, 170, 255, 255), stop:0.0852273 rgb(32, 36, 45));\n"
"border: none;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color:qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0.0511364 rgb(0, 97, 145), stop:0.0852273 rgb(21, 24, 30));\n"
"color: rgb(72, 82, 100);\n"
"border: none;\n"
"}")
        self.scan_buttons_frame.setFrameShape(QFrame.StyledPanel)
        self.scan_buttons_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.scan_buttons_frame)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.space_1 = QFrame(self.scan_buttons_frame)
        self.space_1.setObjectName(u"space_1")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.space_1.sizePolicy().hasHeightForWidth())
        self.space_1.setSizePolicy(sizePolicy6)
        self.space_1.setMinimumSize(QSize(0, 0))
        self.space_1.setMaximumSize(QSize(10000, 10000))
        self.space_1.setFrameShape(QFrame.StyledPanel)
        self.space_1.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_8.addWidget(self.space_1)

        self.buttons = QFrame(self.scan_buttons_frame)
        self.buttons.setObjectName(u"buttons")
        sizePolicy6.setHeightForWidth(self.buttons.sizePolicy().hasHeightForWidth())
        self.buttons.setSizePolicy(sizePolicy6)
        self.buttons.setMinimumSize(QSize(500, 100))
        self.buttons.setMaximumSize(QSize(500, 100))
        self.buttons.setLayoutDirection(Qt.LeftToRight)
        self.buttons.setStyleSheet(u"QPushButton {\n"
"border-radius: 6px;\n"
"}\n"
"#buttons {\n"
"background-color: rgba(0, 0, 0, 40);\n"
"border-radius: 20px;\n"
"}")
        self.buttons.setFrameShape(QFrame.StyledPanel)
        self.buttons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.buttons)
        self.horizontalLayout_10.setSpacing(10)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setSizeConstraint(QLayout.SetFixedSize)
        self.horizontalLayout_10.setContentsMargins(20, 20, 20, 20)
        self.save_button = QPushButton(self.buttons)
        self.save_button.setObjectName(u"save_button")
        sizePolicy5.setHeightForWidth(self.save_button.sizePolicy().hasHeightForWidth())
        self.save_button.setSizePolicy(sizePolicy5)
        self.save_button.setMinimumSize(QSize(80, 50))
        self.save_button.setMaximumSize(QSize(80, 50))
        self.save_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.save_button.setStyleSheet(u"")

        self.horizontalLayout_10.addWidget(self.save_button)

        self.load_button = QPushButton(self.buttons)
        self.load_button.setObjectName(u"load_button")
        self.load_button.setMinimumSize(QSize(80, 50))
        self.load_button.setMaximumSize(QSize(80, 50))
        self.load_button.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_10.addWidget(self.load_button)

        self.clear_button = QPushButton(self.buttons)
        self.clear_button.setObjectName(u"clear_button")
        self.clear_button.setMinimumSize(QSize(80, 50))
        self.clear_button.setMaximumSize(QSize(80, 50))
        self.clear_button.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_10.addWidget(self.clear_button)

        self.scan_button = QPushButton(self.buttons)
        self.scan_button.setObjectName(u"scan_button")
        self.scan_button.setMinimumSize(QSize(150, 50))
        self.scan_button.setMaximumSize(QSize(150, 50))
        self.scan_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.scan_button.setStyleSheet(u"font-size: 28px;\n"
"text-align: center;\n"
"padding-bottom: 10px;")

        self.horizontalLayout_10.addWidget(self.scan_button)


        self.horizontalLayout_8.addWidget(self.buttons, 0, Qt.AlignTop)

        self.frame_4 = QFrame(self.scan_buttons_frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setLayoutDirection(Qt.LeftToRight)
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_8.addWidget(self.frame_4)


        self.verticalLayout_16.addWidget(self.scan_buttons_frame, 0, Qt.AlignTop)


        self.verticalLayout_17.addWidget(self.given_frame)

        self.frame_2 = QFrame(self.data_passport_frame)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy3.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy3)
        self.frame_2.setMinimumSize(QSize(0, 37))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.verticalLayout_17.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.data_passport_frame)

        self.stackedWidget.addWidget(self.scan_page)
        self.db_page = QWidget()
        self.db_page.setObjectName(u"db_page")
        self.db_page.setStyleSheet(u"#db_page {\n"
"background-image: url(:/images/images/images/logo_1_transperent.png);\n"
"background-repeat: none;\n"
"background-position: center;\n"
"}\n"
"")
        self.verticalLayout_20 = QVBoxLayout(self.db_page)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.grid_db = QGridLayout()
        self.grid_db.setObjectName(u"grid_db")
        self.grid_db.setHorizontalSpacing(10)
        self.grid_db.setVerticalSpacing(3)
        self.grid_db.setContentsMargins(0, -1, -1, -1)
        self.frame_5 = QFrame(self.db_page)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 50))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)

        self.grid_db.addWidget(self.frame_5, 2, 0, 1, 1)

        self.left_db_border = QFrame(self.db_page)
        self.left_db_border.setObjectName(u"left_db_border")
        self.left_db_border.setMinimumSize(QSize(2, 0))
        self.left_db_border.setMaximumSize(QSize(2, 16777215))
        self.left_db_border.setStyleSheet(u"background-color: transparent;")
        self.left_db_border.setFrameShape(QFrame.StyledPanel)
        self.left_db_border.setFrameShadow(QFrame.Raised)

        self.grid_db.addWidget(self.left_db_border, 1, 0, 1, 1)

        self.table_db = QTableWidget(self.db_page)
        if (self.table_db.columnCount() < 4):
            self.table_db.setColumnCount(4)
        if (self.table_db.rowCount() < 12):
            self.table_db.setRowCount(12)
        self.table_db.setObjectName(u"table_db")
        self.table_db.setStyleSheet(u"")
        self.table_db.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.table_db.setRowCount(12)
        self.table_db.setColumnCount(4)
        self.table_db.horizontalHeader().setVisible(False)
        self.table_db.horizontalHeader().setCascadingSectionResizes(False)
        self.table_db.horizontalHeader().setMinimumSectionSize(40)
        self.table_db.horizontalHeader().setDefaultSectionSize(50)
        self.table_db.horizontalHeader().setHighlightSections(False)
        self.table_db.horizontalHeader().setStretchLastSection(False)
        self.table_db.verticalHeader().setVisible(False)
        self.table_db.verticalHeader().setHighlightSections(False)
        self.table_db.verticalHeader().setStretchLastSection(False)

        self.grid_db.addWidget(self.table_db, 1, 1, 1, 1)

        self.right_db_border = QFrame(self.db_page)
        self.right_db_border.setObjectName(u"right_db_border")
        self.right_db_border.setMinimumSize(QSize(2, 0))
        self.right_db_border.setMaximumSize(QSize(2, 16777215))
        self.right_db_border.setFrameShape(QFrame.StyledPanel)
        self.right_db_border.setFrameShadow(QFrame.Raised)

        self.grid_db.addWidget(self.right_db_border, 1, 2, 1, 1)

        self.bottom_db_border = QFrame(self.db_page)
        self.bottom_db_border.setObjectName(u"bottom_db_border")
        self.bottom_db_border.setMinimumSize(QSize(0, 10))
        self.bottom_db_border.setFrameShape(QFrame.StyledPanel)
        self.bottom_db_border.setFrameShadow(QFrame.Raised)

        self.grid_db.addWidget(self.bottom_db_border, 3, 0, 1, 3)

        self.label_db = QLabel(self.db_page)
        self.label_db.setObjectName(u"label_db")
        self.label_db.setMaximumSize(QSize(16777215, 30))
        self.label_db.setStyleSheet(u"background-image: none;")

        self.grid_db.addWidget(self.label_db, 0, 0, 1, 2)

        self.combobox_frame = QFrame(self.db_page)
        self.combobox_frame.setObjectName(u"combobox_frame")
        self.combobox_frame.setFrameShape(QFrame.StyledPanel)
        self.combobox_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.combobox_frame)
        self.horizontalLayout_6.setSpacing(10)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, -1, -1, -1)
        self.db_combobox = QComboBox(self.combobox_frame)
        self.db_combobox.setObjectName(u"db_combobox")
        self.db_combobox.setMinimumSize(QSize(0, 40))
        self.db_combobox.setMaximumSize(QSize(16777215, 40))
        self.db_combobox.setCursor(QCursor(Qt.PointingHandCursor))
        self.db_combobox.setStyleSheet(u"background-color: rgb(46, 51, 61);\n"
"padding-left: 5px;\n"
"padding-bottom: 2px;\n"
"font: 12pt \"Segoe UI\";")
        self.db_combobox.setEditable(True)
        self.db_combobox.setFrame(True)

        self.horizontalLayout_6.addWidget(self.db_combobox)

        self.remove_button = QPushButton(self.combobox_frame)
        self.remove_button.setObjectName(u"remove_button")
        sizePolicy6.setHeightForWidth(self.remove_button.sizePolicy().hasHeightForWidth())
        self.remove_button.setSizePolicy(sizePolicy6)
        self.remove_button.setMinimumSize(QSize(100, 35))
        self.remove_button.setMaximumSize(QSize(100, 35))
        self.remove_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.remove_button.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(32, 36, 45);\n"
"font: 63 12pt \"Segoe UI Semibold\";\n"
"border: none;\n"
"padding-bottom: 2px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0.0511364 rgba(0, 170, 255, 255), stop:0.0852273 rgb(32, 36, 45));\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(0, 170, 255);\n"
"}\n"
"QPushButton:focus {\n"
"border: none;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/icons/cil-x-circle.png", QSize(), QIcon.Normal, QIcon.Off)
        self.remove_button.setIcon(icon4)
        self.remove_button.setIconSize(QSize(16, 16))

        self.horizontalLayout_6.addWidget(self.remove_button)


        self.grid_db.addWidget(self.combobox_frame, 2, 1, 1, 1)


        self.verticalLayout_20.addLayout(self.grid_db)

        self.stackedWidget.addWidget(self.db_page)
        self.reg_log_page = QWidget()
        self.reg_log_page.setObjectName(u"reg_log_page")
        sizePolicy6.setHeightForWidth(self.reg_log_page.sizePolicy().hasHeightForWidth())
        self.reg_log_page.setSizePolicy(sizePolicy6)
        self.reg_log_page.setStyleSheet(u"#reg_log_page {\n"
"background-image: url(:/images/images/images/logo_1_transperent.png);\n"
"background-repeat: none;\n"
"background-position: center;\n"
"}\n"
"")
        self.gridLayout_4 = QGridLayout(self.reg_log_page)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.reg_form = QFrame(self.reg_log_page)
        self.reg_form.setObjectName(u"reg_form")
        self.reg_form.setMinimumSize(QSize(323, 129))
        self.reg_form.setMaximumSize(QSize(220, 102))
        self.reg_form.setFrameShape(QFrame.Box)
        self.reg_form.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.reg_form)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(0)
        self.formLayout.setVerticalSpacing(6)
        self.formLayout.setContentsMargins(0, 13, 42, 0)
        self.label_login = QLabel(self.reg_form)
        self.label_login.setObjectName(u"label_login")
        self.label_login.setStyleSheet(u"padding-left: 24px;\n"
"padding-top: 3px;")
        self.label_login.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_login)

        self.login_line_edit = QLineEdit(self.reg_form)
        self.login_line_edit.setObjectName(u"login_line_edit")
        self.login_line_edit.setMinimumSize(QSize(0, 40))
        self.login_line_edit.setStyleSheet(u"#login_line_edit {\n"
"background-color: rgb(46, 51, 61);\n"
"border: 2px solid rgb(22, 26, 35);\n"
"}\n"
"#login_line_edit:focus {\n"
"border: 2px solid rgb(188, 188, 189);\n"
"}")
        self.login_line_edit.setInputMask(u"")
        self.login_line_edit.setMaxLength(16)
        self.login_line_edit.setFrame(False)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.login_line_edit)

        self.label_password = QLabel(self.reg_form)
        self.label_password.setObjectName(u"label_password")
        self.label_password.setStyleSheet(u"padding-top: 3 px;\n"
"margin-right: 5px;")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_password)

        self.password_line_edit = QLineEdit(self.reg_form)
        self.password_line_edit.setObjectName(u"password_line_edit")
        self.password_line_edit.setMinimumSize(QSize(0, 40))
        self.password_line_edit.setStyleSheet(u"#password_line_edit {\n"
"background-color: rgb(46, 51, 61);\n"
"border: 2px solid rgb(22, 26, 35);\n"
"}\n"
"#password_line_edit:focus {\n"
"border: 2px solid rgb(188, 188, 189);\n"
"}")
        self.password_line_edit.setInputMask(u"")
        self.password_line_edit.setMaxLength(16)
        self.password_line_edit.setFrame(False)
        self.password_line_edit.setEchoMode(QLineEdit.Password)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.password_line_edit)


        self.verticalLayout_21.addWidget(self.reg_form)

        self.frame = QFrame(self.reg_log_page)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(240, 0))
        self.frame.setMaximumSize(QSize(16777215, 200))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self._2 = QVBoxLayout(self.frame)
        self._2.setSpacing(10)
        self._2.setObjectName(u"_2")
        self._2.setContentsMargins(71, 0, 2, 169)
        self.reg_label = QLabel(self.frame)
        self.reg_label.setObjectName(u"reg_label")
        self.reg_label.setMinimumSize(QSize(0, 14))
        self.reg_label.setMaximumSize(QSize(206, 27))
        self.reg_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self._2.addWidget(self.reg_label)

        self.reg_log_button = QPushButton(self.frame)
        self.reg_log_button.setObjectName(u"reg_log_button")
        self.reg_log_button.setMinimumSize(QSize(0, 47))
        self.reg_log_button.setMaximumSize(QSize(206, 16777215))
        self.reg_log_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.reg_log_button.setStyleSheet(u"#reg_log_button {\n"
"background-color: rgb(32, 36, 45);\n"
"font: 63 12pt \"Segoe UI Semibold\";\n"
"border: none;\n"
"}\n"
"#reg_log_button:hover {\n"
"background-color:qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0.0511364 rgba(0, 170, 255, 255), stop:0.0852273 rgb(32, 36, 45));\n"
"}\n"
"#reg_log_button:pressed {\n"
"background-color:qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0.0511364 rgb(0, 97, 145), stop:0.0852273 rgb(21, 24, 30));\n"
"color: rgb(72, 82, 100);\n"
"}\n"
"#reg_log_button:focus {\n"
"border: none;\n"
"}\n"
"")

        self._2.addWidget(self.reg_log_button)


        self.verticalLayout_21.addWidget(self.frame)


        self.gridLayout_4.addLayout(self.verticalLayout_21, 0, 1, 1, 1)

        self.stackedWidget.addWidget(self.reg_log_page)

        self.verticalLayout_15.addWidget(self.stackedWidget)

        self.bottomBar = QFrame(self.pagesContainer)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(10000, 22))
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.bottomBar)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_5.addWidget(self.label_2)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(0, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 20))
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_15.addWidget(self.bottomBar)


        self.horizontalLayout_4.addWidget(self.pagesContainer)

        self.extraRightBox = QFrame(self.content)
        self.extraRightBox.setObjectName(u"extraRightBox")
        self.extraRightBox.setMinimumSize(QSize(0, 0))
        self.extraRightBox.setMaximumSize(QSize(0, 16777215))
        self.extraRightBox.setFrameShape(QFrame.NoFrame)
        self.extraRightBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.extraRightBox)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.themeSettingsTopDetail = QFrame(self.extraRightBox)
        self.themeSettingsTopDetail.setObjectName(u"themeSettingsTopDetail")
        self.themeSettingsTopDetail.setMaximumSize(QSize(16777215, 3))
        self.themeSettingsTopDetail.setFrameShape(QFrame.NoFrame)
        self.themeSettingsTopDetail.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.themeSettingsTopDetail)

        self.contentSettings = QFrame(self.extraRightBox)
        self.contentSettings.setObjectName(u"contentSettings")
        self.contentSettings.setFrameShape(QFrame.NoFrame)
        self.contentSettings.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.contentSettings)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.topMenus = QFrame(self.contentSettings)
        self.topMenus.setObjectName(u"topMenus")
        self.topMenus.setFrameShape(QFrame.NoFrame)
        self.topMenus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.topMenus)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.btn_rbox_log = QPushButton(self.topMenus)
        self.btn_rbox_log.setObjectName(u"btn_rbox_log")
        sizePolicy.setHeightForWidth(self.btn_rbox_log.sizePolicy().hasHeightForWidth())
        self.btn_rbox_log.setSizePolicy(sizePolicy)
        self.btn_rbox_log.setMinimumSize(QSize(0, 45))
        self.btn_rbox_log.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_rbox_log.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-exit-to-app.png);")

        self.verticalLayout_14.addWidget(self.btn_rbox_log)

        self.btn_rbox_reg = QPushButton(self.topMenus)
        self.btn_rbox_reg.setObjectName(u"btn_rbox_reg")
        sizePolicy.setHeightForWidth(self.btn_rbox_reg.sizePolicy().hasHeightForWidth())
        self.btn_rbox_reg.setSizePolicy(sizePolicy)
        self.btn_rbox_reg.setMinimumSize(QSize(0, 45))
        self.btn_rbox_reg.setFont(font)
        self.btn_rbox_reg.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_rbox_reg.setLayoutDirection(Qt.LeftToRight)
        self.btn_rbox_reg.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-user-follow.png);")

        self.verticalLayout_14.addWidget(self.btn_rbox_reg)


        self.verticalLayout_13.addWidget(self.topMenus, 0, Qt.AlignTop)


        self.verticalLayout_7.addWidget(self.contentSettings)


        self.horizontalLayout_4.addWidget(self.extraRightBox)


        self.verticalLayout_6.addWidget(self.content)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.verticalLayout_19.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)
#if QT_CONFIG(shortcut)
        self.label_login.setBuddy(self.label_login)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.toggleButton, self.btn_home)
        QWidget.setTabOrder(self.btn_home, self.btn_scan)
        QWidget.setTabOrder(self.btn_scan, self.btn_database)
        QWidget.setTabOrder(self.btn_database, self.settingsTopBtn)
        QWidget.setTabOrder(self.settingsTopBtn, self.closeAppBtn)
        QWidget.setTabOrder(self.closeAppBtn, self.maximizeRestoreAppBtn)
        QWidget.setTabOrder(self.maximizeRestoreAppBtn, self.minimizeAppBtn)
        QWidget.setTabOrder(self.minimizeAppBtn, self.folder_open_button)
        QWidget.setTabOrder(self.folder_open_button, self.search_line)
        QWidget.setTabOrder(self.search_line, self.line_f)
        QWidget.setTabOrder(self.line_f, self.line_i)
        QWidget.setTabOrder(self.line_i, self.line_o)
        QWidget.setTabOrder(self.line_o, self.line_born_date)
        QWidget.setTabOrder(self.line_born_date, self.line_born_place)
        QWidget.setTabOrder(self.line_born_place, self.table_db)
        QWidget.setTabOrder(self.table_db, self.line_male)
        QWidget.setTabOrder(self.line_male, self.line_serial)
        QWidget.setTabOrder(self.line_serial, self.line_number)
        QWidget.setTabOrder(self.line_number, self.line_given_date)
        QWidget.setTabOrder(self.line_given_date, self.line_given_code)
        QWidget.setTabOrder(self.line_given_code, self.line_given)
        QWidget.setTabOrder(self.line_given, self.scan_button)
        QWidget.setTabOrder(self.scan_button, self.clear_button)
        QWidget.setTabOrder(self.clear_button, self.load_button)
        QWidget.setTabOrder(self.load_button, self.save_button)
        QWidget.setTabOrder(self.save_button, self.login_line_edit)
        QWidget.setTabOrder(self.login_line_edit, self.password_line_edit)
        QWidget.setTabOrder(self.password_line_edit, self.reg_log_button)
        QWidget.setTabOrder(self.reg_log_button, self.btn_rbox_log)
        QWidget.setTabOrder(self.btn_rbox_log, self.btn_rbox_reg)
        QWidget.setTabOrder(self.btn_rbox_reg, self.btn_help)
        QWidget.setTabOrder(self.btn_help, self.extraCloseColumnBtn)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"Scanner", None))
        self.username_label.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.label_3.setText("")
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_scan.setText(QCoreApplication.translate("MainWindow", u"Scan", None))
        self.btn_database.setText(QCoreApplication.translate("MainWindow", u"Database", None))
        self.btn_help.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.extraLabel.setText(QCoreApplication.translate("MainWindow", u"help", None))
#if QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close left box", None))
#endif // QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setText("")
#if QT_CONFIG(tooltip)
        self.settingsTopBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.settingsTopBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.search_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Passport...", None))
        self.folder_open_button.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.label_i.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f", None))
        self.line_i.setText("")
        self.label_o.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.line_o.setText("")
        self.label_f.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f", None))
        self.line_f.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0441\u0442\u043e \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f", None))
        self.label_serial.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0435\u0440\u0438\u044f", None))
        self.label_number.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u043c\u0435\u0440", None))
        self.label_given_code.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u0434 \u043f\u043e\u0434\u0440\u0430\u0437\u0434\u0435\u043b\u0435\u043d\u0438\u044f", None))
        self.label_given_date.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u0432\u044b\u0434\u0430\u0447\u0438", None))
        self.line_number.setText("")
        self.line_serial.setText("")
        self.given_label.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0434\u0430\u043d", None))
        self.line_given.setText("")
        self.label_scan.setText("")
        self.save_button.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.load_button.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.clear_button.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.scan_button.setText(QCoreApplication.translate("MainWindow", u"Scan", None))
        self.label_db.setText(QCoreApplication.translate("MainWindow", u"Database", None))
        self.db_combobox.setCurrentText("")
        self.remove_button.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.label_login.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.label_password.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.reg_label.setText("")
        self.reg_log_button.setText(QCoreApplication.translate("MainWindow", u"Registration", None))
        self.label_2.setText("")
        self.btn_rbox_log.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.btn_rbox_reg.setText(QCoreApplication.translate("MainWindow", u"Registration", None))
    # retranslateUi

