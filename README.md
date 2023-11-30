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
![scanner-1](http://95.216.65.93:13617/static/images/github/scanner-1@0,75x.png)
___
![scanner-2](http://95.216.65.93:13617/static/images/github/scanner-2@0,75x-2.png)
___
![scanner-3](http://95.216.65.93:13617/static/images/github/scanner-3@0,75x.png)
