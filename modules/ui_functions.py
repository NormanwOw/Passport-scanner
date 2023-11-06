import sqlite3
import datetime
import json
import os
import re
import string
import threading
import hashlib
import socket
from configparser import ConfigParser

from PySide6.QtGui import QIcon, QColor
from PySide6.QtCore import QPropertyAnimation, QEasingCurve, QParallelAnimationGroup, Qt
from PySide6.QtWidgets import QTableWidgetItem, QGraphicsDropShadowEffect, QSizeGrip, QPushButton, QFileDialog
from PySide6.QtTest import QTest

from modules.app_settings import Settings
from modules.scanner import Scanner
from widgets import *
from database import Database

GLOBAL_STATE = False
GLOBAL_TITLE_BAR = True

config = ConfigParser()
config.read('config.ini')
DEBUG = config.getint('APP', 'DEBUG')


class UIFunctions:

    def __init__(self, ui, main_window):
        super().__init__()
        self.ui = ui
        self.db = Database()
        self.main_window = main_window

        self.state_window = False

        self.name_f = self.name_i = self.name_o = self.born_date = self.born_place = self.male\
            = self.given_date = self.given_code = self.given = self.serial = self.number = None

        self.username = ''

        self.state_server = False
        self.ip = config.get('SERVER', 'ip')
        self.port = config.getint('SERVER', 'port')

        self.exit = threading.Event()

        threading.Thread(target=self.check_connection).start()

    def check_connection(self):
        while not self.exit.is_set():

            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:

                try:
                    client.connect((self.ip, self.port))
                    self.state_server = True
                except socket.gaierror:
                    try:
                        client.connect((socket.gethostbyname(socket.gethostname()), self.port))
                        self.state_server = True
                    except ConnectionRefusedError:
                        self.state_server = False

            self.exit.wait(10)

    def maximize_restore(self):
        """Maximize and restore window application"""

        if not self.state_window:
            self.main_window.showMaximized()
            self.state_window = True
            self.ui.maximizeRestoreAppBtn.setToolTip("Restore")
            self.ui.maximizeRestoreAppBtn.setIcon(QIcon(u":/icons/images/icons/icon_restore.png"))
            self.ui.frame_size_grip.hide()
            self.left_grip.hide()
            self.right_grip.hide()
            self.top_grip.hide()
            self.bottom_grip.hide()
        else:
            self.state_window = False
            self.main_window.showNormal()
            self.ui.maximizeRestoreAppBtn.setToolTip("Maximize")
            self.ui.maximizeRestoreAppBtn.setIcon(QIcon(u":/icons/images/icons/icon_maximize.png"))
            self.ui.frame_size_grip.show()
            self.left_grip.show()
            self.right_grip.show()
            self.top_grip.show()
            self.bottom_grip.show()

    def logout(self):
        self.ui.reg_log_button.setText('Login')
        self.ui.btn_rbox_reg.setVisible(True)
        self.ui.btn_rbox_log.setStyleSheet("background-image: url(:/icons/images/icons/cil-exit-to-app.png);")
        self.ui.username_label.setText('Logout')
        self.ui.reg_label.setText('')
        self.ui.btn_scan.setDisabled(True)
        self.ui.btn_database.setDisabled(True)
        self.group_toggle_menu(False, False)
        self.left_buttons(False)

    def login(self, username):
        self.ui.btn_rbox_log.setText('Logout')
        self.ui.btn_rbox_reg.setVisible(False)
        self.ui.btn_rbox_log.setStyleSheet("background-image: url(:/icons/images/icons/cil-account-logout.png);")
        self.ui.username_label.setText(username)
        self.ui.stackedWidget.setCurrentWidget(self.ui.home_page)
        self.ui.reg_label.setText('')
        self.left_buttons(True)
        self.group_toggle_menu(True, False)
        self.clear_database()
        self.load_database(username)
        self.db.user_connected(username)

    def left_buttons(self, state: bool):
        if state:
            state = False
            self.ui.btn_home.setStyleSheet(self.select_menu(self.ui.btn_home.styleSheet()))
        else:
            state = True
            self.ui.btn_scan.setStyleSheet(self.deselect_menu(self.ui.btn_scan.styleSheet()))
            self.ui.btn_home.setStyleSheet(self.deselect_menu(self.ui.btn_home.styleSheet()))
            self.ui.btn_database.setStyleSheet(self.deselect_menu(self.ui.btn_database.styleSheet()))

        self.ui.btn_scan.setDisabled(state)
        self.ui.btn_database.setDisabled(state)
        self.ui.btn_home.setDisabled(state)

    def authorization(self):
        login = self.ui.login_line_edit.text()
        password = self.ui.password_line_edit.text()

        if not self.state_server:
            return self.ui.reg_label.setText('Сервер не отвечает')

        user = self.db.get_user(login)

        if not 4 < len(login) < 17 or not 4 < len(password) < 17:
            return self.ui.reg_label.setText('*от 5 до 16 символов')

        if not self.filter_string(login) or not self.filter_string(password):
            return self.ui.reg_label.setText('*неверный ввод')

        if self.ui.reg_log_button.text() == 'Registration':
            if user is None:
                self.db.add_user(
                    login, password, datetime.datetime.now().strftime('%d.%m.%Y')
                )
                self.login(login)
                self.username = login
            else:
                self.ui.reg_label.setText('Пользователь уже существует')

        elif self.ui.reg_log_button.text() == 'Login':
            if user is None:
                self.ui.reg_label.setText('Пользователь не найден')
                return

            user_list = user.split(', ')
            user = user_list[1].replace('\'', '')

            pw_hash = str(hashlib.sha256(password.encode('utf-8')).hexdigest())
            password = user_list[2].replace('\'', '')

            if login != user or pw_hash != password:
                self.ui.reg_label.setText('Неверный логин или пароль')
            else:
                self.login(login)
                self.username = login

    @staticmethod
    def filter_string(input_str: str):
        for char in input_str:
            if char not in string.printable or char == ' ':
                return False

        return True

    def clear_menu(self):
        self.ui.login_line_edit.setText('')
        self.ui.password_line_edit.setText('')
        self.ui.reg_label.setText('')

    def open_folder(self):
        self.ui.label_scan.setText('')
        exp_list = ('*.jpg', '*.png', '*.jpeg', '*.pdf', '*.gif', '*.bmp')
        res = QFileDialog.getOpenFileName(self.main_window, 'Выбор файла', '', f'Images {" ".join(exp_list)}')

        self.ui.search_line.setText(res[0])

    def start_scan(self):
        if DEBUG:
            return self.ui.label_scan.setText('DEBUG')

        path = self.ui.search_line.text()
        if '/' in path:
            self.name_f, self.name_i, self.name_o, self.serial, self.number, self.born_date = Scanner.scan(path)
            self.set_data()
        else:
            self.ui.label_scan.setText('Выберите файл')

    def update_db_table(self):
        self.clear_database()
        self.ui.db_combobox.clear()
        self.load_database(self.username)

    def remove(self):
        if self.ui.db_combobox.currentText() != '' and self.state_server:
            data = self.ui.db_combobox.currentText()
            serial = re.search(r'\s\d{4}', data).group()[1:]
            number = re.search(r'\s\d{6}', data).group()[1:]
            self.db.remove_passport(self.username, serial, number)
            self.update_db_table()

    def apply_data(self):
        """Get data from input fields to variables"""

        self.name_f = self.ui.line_f.text().upper()
        self.name_i = self.ui.line_i.text().upper()
        self.name_o = self.ui.line_o.text().upper()
        self.born_date = self.ui.line_born_date.text()
        self.born_place = self.ui.line_born_place.text().upper()
        self.male = self.ui.line_male.text().upper()
        self.serial = self.ui.line_serial.text()
        self.number = self.ui.line_number.text()
        self.given_date = self.ui.line_given_date.text()
        self.given_code = self.ui.line_given_code.text()
        self.given = self.ui.line_given.text().upper()

    def set_data(self):
        """Set data to input fields from variables"""

        self.ui.line_f.setText(self.name_f)
        self.ui.line_i.setText(self.name_i)
        self.ui.line_o.setText(self.name_o)
        self.ui.line_born_date.setText(self.born_date)
        self.ui.line_serial.setText(f'{self.serial}')
        self.ui.line_number.setText(f'{self.number}')

    def save(self):
        if DEBUG:
            return self.ui.label_scan.setText('DEBUG')

        if not self.state_server:
            return self.ui.label_scan.setText('Сервер не отвечает')

        serial = self.ui.line_serial.text()
        number = self.ui.line_number.text()

        if len(serial) != 4 or len(number) != 6:
            self.ui.label_scan.setText('Поля заполнены неверно')
            return

        self.apply_data()
        if serial + ' ' + number == self.db.load_serials(self.username):
            self.db.update_passport(
                self.username, self.name_f, self.name_i, self.name_o, self.born_date, self.born_place,
                self.male, self.given_date, self.given_code, self.given, self.serial, self.number
            )
        else:
            self.db.add_passport(
                self.username, self.name_f, self.name_i, self.name_o, self.born_date, self.born_place,
                self.male, self.given_date, self.given_code, self.given, self.serial, self.number
            )
        self.ui.label_scan.setText('Сохранено')
        self.update_db_table()

    def load(self):
        if DEBUG:
            return self.ui.label_scan.setText('DEBUG')

        self.name_f = self.ui.line_f.text().upper()
        self.name_i = self.ui.line_i.text().upper()
        self.name_o = self.ui.line_o.text().upper()

        if all([self.name_f, self.name_f, self.name_f]):
            user = self.db.load_passport(self.ui.username_label.text(), self.name_f, self.name_i, self.name_o)

            if user is None:
                return self.ui.label_scan.setText('Запись не найдена')

            self.name_f, self.name_i, self.name_o, self.born_date, self.born_place, \
                self.male, self.given_date, self.given_code, self.given, self.serial, self.number = user[1:]
            self.set_data()
            self.ui.label_scan.setText('')
        else:
            self.ui.label_scan.setText('Введите ФИО')

    def clear(self):
        for obj in [
            self.ui.label_scan, self.ui.line_f, self.ui.line_i, self.ui.line_o, self.ui.line_born_date,
            self.ui.line_born_place, self.ui.line_male, self.ui.line_serial, self.ui.line_number,
            self.ui.line_given_date, self.ui.line_given_code, self.ui.line_given, self.ui.search_line
        ]:
            obj.setText('')

    def load_database(self, username):
        database = self.db.load_for_db(username)
        if database:
            self.ui.db_combobox.clear()
            for ch in ['[', ']', '(', ')', ',', '\'']:
                database = database.replace(ch, '')
            database = database.split()
            data_for_combobox = ''
            for i, data in enumerate(database):
                data_for_combobox += f'{data} '
                self.ui.table_db.setItem(0, i, QTableWidgetItem(data))
                if (i + 1) % 7 == 0:
                    self.ui.db_combobox.addItem(data_for_combobox)
                    data_for_combobox = ''

            self.ui.db_combobox.update()
            self.ui.db_combobox.clearEditText()

    def clear_database(self):
        self.ui.table_db.clear()
        self.ui.table_db.setColumnCount(7)
        self.ui.table_db.horizontalHeader().setVisible(True)

        db_fields_list = [
            'Фамилия', 'Имя', 'Отчество', 'Дата рождения',
            'Место рождения', 'Серия', 'Номер'
        ]

        for i, field_name in enumerate(db_fields_list):
            self.ui.table_db.setHorizontalHeaderItem(i, QTableWidgetItem(field_name))

    # TOGGLE MENUS
    # ////////////////////////////////////////////////////////////////////////////////////////////

    def toggle_left_menu(self, enable):
        self.clear_menu()
        if enable:
            width = self.ui.leftMenuBg.width()
            max_extend = Settings.MENU_WIDTH
            standard = 60
            if width == 60:
                width_extended = max_extend
            else:
                width_extended = standard

            # ANIMATION
            self.animation = QPropertyAnimation(self.ui.leftMenuBg, b"minimumWidth")
            self.animation.setDuration(Settings.TIME_ANIMATION)
            self.animation.setStartValue(width)
            self.animation.setEndValue(width_extended)
            self.animation.setEasingCurve(QEasingCurve.InOutQuart)
            self.animation.start()

    # TOGGLE MENU BY SELECT
    def toggle_menu(self, state: bool, menu):
        min_ex = 0
        max_ex = 0
        toggle_obj = None
        if menu == 'left':
            max_ex = Settings.MENU_WIDTH
            min_ex = 60
            toggle_obj = self.ui.leftMenuBg
        if menu == 'right':
            max_ex = Settings.RIGHT_BOX_WIDTH
            min_ex = 0
            toggle_obj = self.ui.extraRightBox
            color = Settings.BTN_RIGHT_BOX_COLOR
            style = self.ui.settingsTopBtn.styleSheet()
            self.ui.settingsTopBtn.setStyleSheet(style + color)
        self.animation = QPropertyAnimation(toggle_obj, b"minimumWidth")
        self.animation.setDuration(Settings.TIME_ANIMATION)
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        if state:
            if toggle_obj.width() == min_ex:
                self.animation.setStartValue(min_ex)
                self.animation.setEndValue(max_ex)
        else:
            if toggle_obj.width() == max_ex:
                self.animation.setStartValue(max_ex)
                self.animation.setEndValue(min_ex)
        self.animation.start()

    # GROUP TOGGLE MENU
    def group_toggle_menu(self, left_menu: bool, right_menu: bool):
        if left_menu:
            if self.ui.leftMenuBg.width() == 60:
                self.left_box = QPropertyAnimation(self.ui.leftMenuBg, b"minimumWidth")
                self.left_box.setDuration(Settings.TIME_ANIMATION)
                self.left_box.setStartValue(60)
                self.left_box.setEndValue(Settings.MENU_WIDTH)
                self.left_box.setEasingCurve(QEasingCurve.InOutQuart)
            else:
                self.left_box = QPropertyAnimation(None)
        else:
            if self.ui.leftMenuBg.width() == Settings.MENU_WIDTH:
                color = Settings.BTN_RIGHT_BOX_COLOR
                style = self.ui.settingsTopBtn.styleSheet()
                self.ui.settingsTopBtn.setStyleSheet(style + color)
                self.left_box = QPropertyAnimation(self.ui.leftMenuBg, b"minimumWidth")
                self.left_box.setDuration(Settings.TIME_ANIMATION)
                self.left_box.setStartValue(Settings.MENU_WIDTH)
                self.left_box.setEndValue(60)
                self.left_box.setEasingCurve(QEasingCurve.InOutQuart)
            else:
                self.left_box = QPropertyAnimation(None)

        if right_menu:
            if self.ui.extraRightBox.width() == 0:
                self.right_box = QPropertyAnimation(self.ui.extraRightBox, b"minimumWidth")
                self.right_box.setDuration(Settings.TIME_ANIMATION)
                self.right_box.setStartValue(0)
                self.right_box.setEndValue(Settings.RIGHT_BOX_WIDTH)
                self.right_box.setEasingCurve(QEasingCurve.InOutQuart)
            else:
                self.right_box = QPropertyAnimation(None)
        else:
            if self.ui.extraRightBox.width() == Settings.RIGHT_BOX_WIDTH:
                self.right_box = QPropertyAnimation(self.ui.extraRightBox, b"minimumWidth")
                self.right_box.setDuration(Settings.TIME_ANIMATION)
                self.right_box.setStartValue(Settings.RIGHT_BOX_WIDTH)
                self.right_box.setEndValue(0)
                self.right_box.setEasingCurve(QEasingCurve.InOutQuart)
            else:
                self.right_box = QPropertyAnimation(None)

        # GROUP ANIMATION MENU
        self.group = QParallelAnimationGroup()
        self.group.addAnimation(self.left_box)
        self.group.addAnimation(self.right_box)
        color = Settings.BTN_RIGHT_BOX_COLOR
        style = self.ui.settingsTopBtn.styleSheet()
        self.ui.settingsTopBtn.setStyleSheet(style.replace(color, ''))
        self.group.start()

    def btn_help(self, enable):
        if enable:
            width = self.ui.extraLeftBox.width()
            width_right_box = self.ui.extraRightBox.width()
            color = Settings.BTN_LEFT_BOX_COLOR

            # GET BTN STYLE
            btn_style = self.ui.btn_help.styleSheet()

            # SET MAX WIDTH
            if width == 0:
                self.ui.btn_help.setStyleSheet(btn_style + color)
                if width_right_box != 0:
                    self.ui.settingsTopBtn.setStyleSheet(style.replace(Settings.BTN_RIGHT_BOX_COLOR, ''))
            else:
                # RESET BTN
                self.ui.btn_help.setStyleSheet(btn_style.replace(color, ''))

            self.start_box_animation(width, width_right_box, "left")

    def toggle_right_menu(self, enable):
        if enable:
            width = self.ui.extraRightBox.width()
            width_left_box = self.ui.extraLeftBox.width()
            color = Settings.BTN_RIGHT_BOX_COLOR

            # GET BTN STYLE
            btn_style = self.ui.settingsTopBtn.styleSheet()

            if width == 0:
                self.ui.settingsTopBtn.setStyleSheet(btn_style + color)
                if width_left_box != 0:
                    self.ui.btn_help.setStyleSheet(style.replace(Settings.BTN_LEFT_BOX_COLOR, ''))
            else:
                # RESET BTN
                self.ui.settingsTopBtn.setStyleSheet(btn_style.replace(color, ''))

            self.start_box_animation(width_left_box, width, "right")

    def start_box_animation(self, left_box_width, right_box_width, direction):
        # Check values
        if left_box_width == 0 and direction == "left":
            left_width = Settings.LEFT_BOX_WIDTH
        else:
            left_width = 0
        # Check values
        if right_box_width == 0 and direction == "right":
            right_width = Settings.RIGHT_BOX_WIDTH
        else:
            right_width = 0

            # ANIMATION LEFT BOX
        self.left_box = QPropertyAnimation(self.ui.extraLeftBox, b"minimumWidth")
        self.left_box.setDuration(Settings.TIME_ANIMATION)
        self.left_box.setStartValue(left_box_width)
        self.left_box.setEndValue(left_width)
        self.left_box.setEasingCurve(QEasingCurve.InOutQuart)

        # ANIMATION RIGHT BOX
        self.right_box = QPropertyAnimation(self.ui.extraRightBox, b"minimumWidth")
        self.right_box.setDuration(Settings.TIME_ANIMATION)
        self.right_box.setStartValue(right_box_width)
        self.right_box.setEndValue(right_width)
        self.right_box.setEasingCurve(QEasingCurve.InOutQuart)

        # GROUP ANIMATION
        self.group = QParallelAnimationGroup()
        self.group.addAnimation(self.left_box)
        self.group.addAnimation(self.right_box)
        self.group.start()

    @staticmethod
    def select_menu(new_style):
        return new_style + Settings.MENU_SELECTED_STYLESHEET

    @staticmethod
    def deselect_menu(new_style):
        return new_style.replace(Settings.MENU_SELECTED_STYLESHEET, "")

    def reset_style(self, widget):
        for w in self.ui.topMenu.findChildren(QPushButton):
            if w.objectName() != widget:
                w.setStyleSheet(UIFunctions.deselect_menu(w.styleSheet()))

    def close(self):
        self.exit.set()
        self.main_window.close()

    def ui_definitions(self, main_window):
        main_window.setWindowFlags(Qt.FramelessWindowHint)
        main_window.setAttribute(Qt.WA_TranslucentBackground)

        if Settings.ENABLE_CUSTOM_TITLE_BAR:

            # CUSTOM GRIPS
            self.left_grip = CustomGrip(main_window, Qt.LeftEdge, True)
            self.right_grip = CustomGrip(main_window, Qt.RightEdge, True)
            self.top_grip = CustomGrip(main_window, Qt.TopEdge, True)
            self.bottom_grip = CustomGrip(main_window, Qt.BottomEdge, True)
        else:
            # self.ui.appMargins.setContentsMargins(0, 0, 0, 0)
            self.ui.minimizeAppBtn.hide()
            self.ui.maximizeRestoreAppBtn.hide()
            self.ui.closeAppBtn.hide()
            self.ui.frame_size_grip.hide()

        # DROP SHADOW
        self.shadow = QGraphicsDropShadowEffect(main_window)
        self.shadow.setBlurRadius(17)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 150))
        self.ui.bgApp.setGraphicsEffect(self.shadow)

        # RESIZE WINDOW
        self.sizegrip = QSizeGrip(self.ui.frame_size_grip)
        self.sizegrip.setStyleSheet("width: 20px; height: 20px; margin 0px; padding: 0px;")

        # MINIMIZE WINDOW
        self.ui.minimizeAppBtn.clicked.connect(lambda: self.main_window.showMinimized())

        # MAXIMIZE/RESTORE WINDOW
        self.ui.maximizeRestoreAppBtn.clicked.connect(lambda: self.maximize_restore())

        # CLOSE APPLICATION
        self.ui.closeAppBtn.clicked.connect(lambda: self.close())
