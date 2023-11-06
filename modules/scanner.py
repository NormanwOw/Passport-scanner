import imutils
from imutils.contours import sort_contours
import numpy as np
import pytesseract
import sys
import cv2
import re
import string


rus = [(lambda c: chr(c))(i) for i in range(1040, 1072)]
rus.insert(6, 'Ё')
eng = ['A', 'B', 'V', 'G', 'D', 'E', '2', 'J', 'Z', 'I', 'Q', 'K', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'T', 'U', 'F',
       'H', 'C', '3', '4', 'W', 'X', 'Y', '9', '6', '7', '8']

pytesseract.pytesseract.tesseract_cmd = r'Tesseract-OCR\tesseract.exe'


class Scanner:

    @staticmethod
    def __resize(image: str) -> list:
        img = cv2.imread(image)
        final_wide = 1400
        r = float(final_wide) / img.shape[1]
        dim = (final_wide, int(img.shape[0] * r))
        img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (3, 3), 0)
        thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
        morph = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
        morph = cv2.morphologyEx(morph, cv2.MORPH_CLOSE, kernel)
        contours = cv2.findContours(morph, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contours = contours[0] if len(contours) == 2 else contours[1]
        area_thresh = 0
        big_contour = 0

        for c in contours:
            area = cv2.contourArea(c)
            if area > area_thresh:
                area_thresh = area
                big_contour = c

        page = np.zeros_like(img)
        cv2.drawContours(page, [big_contour], 0, (255, 255, 255), -1)
        peri = cv2.arcLength(big_contour, True)
        corners = cv2.approxPolyDP(big_contour, 0.04 * peri, True)
        polygon = img.copy()
        cv2.polylines(polygon, [corners], True, (0, 0, 255), 3, cv2.LINE_AA)
        nr = np.empty((0, 2), dtype="int32")

        for a in corners:
            for b in a:
                nr = np.vstack([nr, b])

        y_arr = [i[0] for i in nr]
        x_arr = [i[1] for i in nr]

        x = min(y_arr)
        p_X = max(y_arr)
        y = min(x_arr)
        p_Y = max(x_arr)

        return img[y:p_Y, x:p_X]

    @staticmethod
    def __passport_read(photo: list) -> tuple:
        gray = cv2.cvtColor(photo, cv2.COLOR_BGR2GRAY)
        H, W = gray.shape
        rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (25, 7))
        sq_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (21, 21))
        gray = cv2.GaussianBlur(gray, (3, 3), 0)
        black_hat = cv2.morphologyEx(gray, cv2.MORPH_BLACKHAT, rect_kernel)
        grad = cv2.Sobel(black_hat, ddepth=cv2.CV_32F, dx=1, dy=0, ksize=-1)
        grad = np.absolute(grad)
        min_val, maxVal = np.min(grad), np.max(grad)
        grad = (grad - min_val) / (maxVal - min_val)
        grad = (grad * 255).astype("uint8")
        grad = cv2.morphologyEx(grad, cv2.MORPH_CLOSE, rect_kernel)
        thresh = cv2.threshold(grad, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
        thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, sq_kernel)
        thresh = cv2.erode(thresh, None, iterations=2)
        contours = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contours = imutils.grab_contours(contours)
        contours = sort_contours(contours, method="bottom-to-top")[0]
        mrz_box = None

        for c in contours:
            (x, y, w, h) = cv2.boundingRect(c)
            percent_width = w / float(W)
            percent_height = h / float(H)
            if percent_width > 0.28 and percent_height > 0.005:
                mrz_box = (x, y, w, h)
                break

        (x, y, w, h) = mrz_box
        p_x = int((x + w) * 0.03)
        p_y = int((y + h) * 0.1)
        x, y = x - p_x, y - p_y
        w, h = w + (p_x * 2), h + (p_y * 2)

        mrz = photo[y:y + h, x:x + w]
        config = f' --oem 3 --psm 6 -c tessedit_char_whitelist={string.ascii_uppercase + string.digits}><'
        mrz_text = pytesseract.image_to_string(mrz, lang='eng', config=config)
        mrz_text = mrz_text.replace(" ", "")
        mrz_text = mrz_text.split()
        if mrz_text[0][0:1] != 'P':
            del mrz_text[0]
        el1 = mrz_text[0]
        el2 = mrz_text[1]
        el1 = el1.replace('1', 'I')
        el2 = el2.replace('O', '0')
        el1 = el1[5:]
        el1 = re.split("<<|<|\n", el1)
        el2 = re.split("RUS|<", el2)
        el1 = list(filter(None, el1))
        el1 = list(map(list, el1))
        el1 = el1[0:3]
        el2 = list(filter(None, el2))
        for i in el1:
            for j, ch in enumerate(i):
                ind = eng.index(str(ch))
                i[j] = rus[ind]

        name_f = ''.join(el1[0])
        name_i = ''.join(el1[1])
        name_o = ''.join(el1[2])
        serial = el2[0][0:3] + el2[2][0:1]
        number = el2[0][3:9]
        date = el2[1][0:6]

        replace_dict = {'I': '1', 'T': '1', 'S': '2', 'B': '8', 'O': '0'}

        for char, num in replace_dict.items():
            date = date.replace(char, num)

        if int(date[0:1]) > 2:
            date = '19' + date
        else:
            date = '20' + date
        date = date[6:8] + '.' + date[4:6] + '.' + date[0:4]

        return name_f, name_i, name_o, serial, number, date

    @classmethod
    def scan(cls, image: str) -> tuple:
        photo = cls.__resize(image)
        return cls.__passport_read(photo)
