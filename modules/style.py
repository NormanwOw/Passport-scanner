from PySide6.QtWidgets import QGraphicsDropShadowEffect
from PySide6.QtGui import QColor
from modules.app_settings import Settings


class Styles:
    def __init__(self, functions, main_window):
        self.functions = functions
        self.main_window = main_window

    def __my_shadow(self, widget):
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setOffset(0, 2)
        shadow.setBlurRadius(8)
        shadow.setColor(QColor(0, 0, 0))
        widget.setGraphicsEffect(shadow)

    def set_shadow(self):
        for widget in [
            self.ui.password_line_edit, self.ui.login_line_edit, self.ui.reg_log_button, self.ui.scan_button,
            self.ui.clear_button, self.ui.load_button, self.ui.save_button, self.ui.folder_open_button,
            self.ui.search_line, self.ui.line_f, self.ui.line_i, self.ui.line_o, self.ui.line_serial,
            self.ui.line_number, self.ui.line_born_place, self.ui.line_born_date, self.ui.line_male,
            self.ui.line_given, self.ui.line_given_code, self.ui.line_given_date, self.ui.remove_button,
            self.ui.db_combobox
        ]:
            Styles.__my_shadow(self, widget)

    def resize_grips(self):
        if Settings.ENABLE_CUSTOM_TITLE_BAR:
            self.functions.left_grip.setGeometry(0, 10, 10, self.main_window.height())
            self.functions.right_grip.setGeometry(self.main_window.width() - 10, 10, 10, self.main_window.height())
            self.functions.top_grip.setGeometry(0, 0, self.main_window.width(), 10)
            self.functions.bottom_grip.setGeometry(0, self.main_window.height() - 10, self.main_window.width(), 10)



