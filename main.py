import sqlite3
import sys
import os
import string
import random
import platform
import threading

from PySide6 import QtCore
from PySide6.QtWidgets import QHeaderView
from modules.ui_main import Ui_MainWindow, QMainWindow, QApplication, QIcon, QCoreApplication
from modules.app_settings import Settings
from modules.ui_functions import UIFunctions
from modules.style import Styles
from widgets import custom_grips
from database import Database

DEBUG = True


class MainWindow(QMainWindow, Database):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.functions = UIFunctions(self.ui, self)
        self.styles = Styles(self.functions, self)
        self.setWindowTitle(QCoreApplication.translate("MainWindow", u"Scanner", None))
        self.username = ''

        self.state = False

        if DEBUG:
            self.username = 'DEBUG'
            threading.Thread(target=self.functions.login, args=(self.username,)).start()
            self.functions.left_buttons(True)
            self.functions.toggle_left_menu(True)
            self.functions.left_buttons(True)
            self.functions.toggle_left_menu(True)
            self.ui.btn_scan.setStyleSheet(self.functions.select_menu(self.ui.btn_scan.styleSheet()))
            self.ui.btn_home.setStyleSheet(self.functions.deselect_menu(self.ui.btn_home.styleSheet()))
            self.ui.stackedWidget.setCurrentWidget(self.ui.scan_page)
        else:
            self.ui.reg_label.setText('')
            self.ui.btn_home.setStyleSheet(self.functions.select_menu(self.ui.btn_home.styleSheet()))
            self.ui.stackedWidget.setCurrentWidget(self.ui.reg_log_page)

        def move_window(event):
            if event.buttons() == QtCore.Qt.MouseButton.LeftButton:
                pos = self.pos()
                global_pos = event.globalPosition().toPoint()
                self.move(pos + global_pos - self.dragPos.toPoint())
                self.dragPos = event.globalPosition()
                event.accept()

        self.ui.contentTopBg.mouseMoveEvent = move_window

        self.ui.toggleButton.clicked.connect(lambda: self.functions.toggle_left_menu(self))

        self.functions.ui_definitions(self)
        Styles.set_shadow(self)

        # DATABASE TABLE
        # //////////////////////////////////////////////////////////////////////////////////////////////////////////////
        self.ui.table_db.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.table_db.setDisabled(True)

        # LEFT MENUS
        self.ui.btn_home.clicked.connect(self.button_click)
        self.ui.btn_scan.clicked.connect(self.button_click)
        self.ui.btn_database.clicked.connect(self.button_click)

        # LEFT BOX
        def open_close_left_box():
            self.functions.btn_help(True)
        self.ui.btn_help.clicked.connect(open_close_left_box)
        self.ui.extraCloseColumnBtn.clicked.connect(open_close_left_box)

        # EXTRA RIGHT BOX
        def open_close_right_box():
            self.functions.toggle_right_menu(True)
        self.ui.settingsTopBtn.clicked.connect(open_close_right_box)

        # RIGHT BOX BUTTONS
        self.ui.btn_rbox_log.clicked.connect(self.button_click)
        self.ui.btn_rbox_reg.clicked.connect(self.button_click)

        # REGISTRATION BUTTON
        self.ui.reg_log_button.clicked.connect(self.button_click)

        # SCAN BUTTONS
        self.ui.scan_button.clicked.connect(self.button_click)
        self.ui.clear_button.clicked.connect(self.button_click)
        self.ui.load_button.clicked.connect(self.button_click)
        self.ui.save_button.clicked.connect(self.button_click)
        self.ui.folder_open_button.clicked.connect(self.button_click)

        self.ui.remove_button.clicked.connect(self.button_click)

        # SHOW APP
        self.show()

    # BUTTONS CLICK
    def button_click(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btn_name = btn.objectName()

        # SHOW HOME PAGE
        if btn_name == "btn_home":
            self.functions.clear_menu()
            self.ui.stackedWidget.setCurrentWidget(self.ui.home_page)
            self.functions.reset_style(btn_name)
            btn.setStyleSheet(self.functions.select_menu(btn.styleSheet()))

        # SHOW WIDGETS PAGE
        if btn_name == "btn_scan":
            self.functions.clear_menu()
            self.ui.stackedWidget.setCurrentWidget(self.ui.scan_page)
            self.functions.reset_style(btn_name)
            btn.setStyleSheet(self.functions.select_menu(btn.styleSheet()))

        # SHOW NEW PAGE
        if btn_name == "btn_database":
            self.functions.clear_menu()
            self.ui.stackedWidget.setCurrentWidget(self.ui.db_page)
            self.functions.reset_style(btn_name)
            btn.setStyleSheet(self.functions.select_menu(btn.styleSheet()))

        if btn_name == "btn_rbox_log":
            self.functions.clear_menu()
            if self.ui.btn_rbox_log.text() == 'Logout':
                self.functions.logout()
                self.ui.btn_rbox_log.setText('Login')
                self.ui.username_label.setText('Logout')
            else:
                self.ui.reg_log_button.setText('Login')
            self.ui.stackedWidget.setCurrentWidget(self.ui.reg_log_page)

        if btn_name == "btn_rbox_reg":
            self.functions.clear_menu()
            self.ui.stackedWidget.setCurrentWidget(self.ui.reg_log_page)
            self.ui.reg_log_button.setText('Registration')

        if btn_name == "reg_log_button":
            login = self.ui.login_line_edit.text()
            password = self.ui.login_line_edit.text()

            if ' ' in login or ' ' in password:
                self.ui.reg_label.setText('*неверный ввод')
            else:
                if 4 < len(login) < 17 and 4 < len(password) < 17:
                    if self.functions.filter_string(login):
                        self.username = login
                        self.functions.authorization()
                else:
                    self.ui.reg_label.setText('*от 5 до 16 символов')

        if btn_name == 'scan_button':
            self.functions.start_scan()

        if btn_name == 'folder_open_button':
            self.functions.open_folder()

        if btn_name == 'clear_button':
            self.functions.clear()

        if btn_name == 'save_button':
            self.functions.save(self.username)

        if btn_name == 'load_button':
            self.functions.load()

        if btn_name == 'remove_button':
            self.functions.remove()

    def resizeEvent(self, event):
        self.styles.resize_grips()

    def mousePressEvent(self, event):
        self.dragPos = event.globalPosition()


def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


ico = resource_path("icon.ico")
app = QApplication(sys.argv)
app.setWindowIcon(QIcon(ico))
window = MainWindow()
sys.exit(app.exec())
