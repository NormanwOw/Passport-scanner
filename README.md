# Passport-scanner
![](https://img.shields.io/badge/Python-v3.9-green) ![](https://img.shields.io/badge/PySide-v6.6.0-blue) ![](https://img.shields.io/badge/Qt-Designer-yellow) 
![](https://img.shields.io/badge/Pytesseract-v0.3.10-red) ![](https://img.shields.io/badge/SQLite-v3-white)

## About
Desktop application for scan passport (RU) with GUI, remote server and database

## Install
1. unzip `Tesseract-OCR.rar` into the `modules` folder
2. `pip install -r requirements.txt`
3. `python server.py`
4. `python main.py`

or

1. unzip `Tesseract-OCR.rar` into the `client` folder
2. run `Server.exe`
3. run `Scanner.exe`

## Config
```
[SERVER]
ip - local or public IP  
port - default 12345

[APP] 
DEBUG - 1 or 0
```
* **DEBUG mode is state without authorisation, registration and scan functions**

## GUI
![scanner-1@0,75x](https://github.com/NormanwOw/Passport-scanner/assets/118648914/f4748301-ca82-4cc4-a352-498bd6d1d53d)
___
![scanner-2@0,75x](https://github.com/NormanwOw/Passport-scanner/assets/118648914/80444969-8b13-4ea8-a149-8dcac8221fda)
___
![scanner-3@0,75x](https://github.com/NormanwOw/Passport-scanner/assets/118648914/43e2bb65-a182-468f-9916-1b4b9f5cf544)

