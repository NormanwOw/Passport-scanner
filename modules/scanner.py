import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = '..\\Tesseract-OCR\\tesseract.exe'


class Scanner:

    def __init__(self, ui):
        self.data = 'asd'
        self.ui = ui
        self.config = r'--oem 3 --psm 1'
        self.config_2 = r'--oem 3 --psm 4'

    @staticmethod
    def __find_date(data: str) -> str:
        """Find passport date by pattern XX.XX.XXXX"""

        return re.search(r'\d{2}\s?[.]\s?\d{2}\s?[.]\s?\d{4}', data, re.ASCII).group(0).replace(' ', '')

    @staticmethod
    def __date_index(data: str) -> int:
        """Find date index by pattern XX.XX.XXXX"""

        return re.search(r'\d{2}\s?[.]\s?\d{2}\s?[.]\s?\d{4}', data, re.ASCII).end()

    @staticmethod
    def __find_serial(data: str) -> int:
        """Find passport serial number"""

        s_number = data[:re.search(r'\d{6}', data, re.ASCII).start()].replace(' ', '')
        if len(s_number) == 4:
            return s_number
        else:
            data = data[re.search(r'\d{6}', data, re.ASCII).end():]
            s_number = data[:re.search(r'\d{6}', data, re.ASCII).start()].replace(' ', '')
            return s_number

    @staticmethod
    def __find_number(data: str) -> str:
        """Find passport number"""

        number_list = re.findall(r'\d{6}', data, re.ASCII)
        if number_list[0] != number_list[1]:
            self.ui.label_scan.setText('*Номер | Возможно: ' + number_list[0])

        return re.findall(r'\d{6}', data, re.ASCII)[1]

    def scan(self):
        img = Image.open(self.ui.search_line.text().replace('/', '\\'))
        result = pytesseract.image_to_string(img, lang='rus', config=self.config)
        result = "".join(result).replace('\n', ' ').replace('  ', ' ')
        result_serial = pytesseract.image_to_string(img, config=self.config_2)
        result_serial = " ".join(re.findall(r'\d+', result_serial, re.ASCII)).replace('  ', ' ')
        given = " ".join(re.findall(r'[А-Я]+', result[:self.__date_index(result)], re.ASCII))
        if 'ГОР ' in given:
            given = given.replace('ГОР ', 'ГОР.')

        given_date = self.__find_date(result)
        given_code = re.search(r'\d{3}\s?—\s?\d{3}', result).group(0)
        born_date = self.__find_date(result[self.__date_index(result):])
        name_list = re.findall(r'[А-Я]{3,}', result[self.__date_index(result):], re.ASCII)
        name_f, name_i, name_o = name_list[0], name_list[1], name_list[2]

        temp = result[self.__date_index(result):]
        male = temp[self.__date_index(temp) - 20:self.__date_index(temp) - 10]
        if 'МУ' in male:
            male = 'МУЖ.'
        else:
            male = 'ЖЕН.'
        born_place = temp[self.__date_index(temp):self.__date_index(temp) + 25]
        born_place = " ".join(re.findall(r'[А-Я]{3,}', born_place, re.ASCII))
        if 'ГОР ' in born_place:
            born_place = born_place.replace('ГОР ', 'ГОР.')

        serial = int(self.__find_serial(result_serial))
        number = int(self.__find_number(result_serial))

        return serial, number, given, given_code, given_date, name_f, name_i, name_o, male, born_date, born_place
