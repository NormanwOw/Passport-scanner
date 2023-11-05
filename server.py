import hashlib
import socket
import sqlite3
import json
import datetime
import time

from configparser import ConfigParser


class Database:
    connection = sqlite3.connect('database.db')

    @classmethod
    def __message_wrapper(cls, message: str) -> str:
        """Add time to massage for console"""

        now = datetime.datetime.now()
        time = now.strftime('%d.%m.%Y %H:%M:%S')
        return f'[{time}]: {message}'

    @classmethod
    def console(cls, message: str) -> print:
        return print(cls.__message_wrapper(message))

    @classmethod
    def add_passport(cls, request: tuple):
        username, name_f, name_i, name_o, born_date, born_place, \
        male, given_date, given_code, given, serial, number = request

        with cls.connection:
            cls.connection.cursor().execute(
                "INSERT INTO passports (username, name_f, name_i, name_o, born_date, born_place, male, "
                "given_date, given_code, given, serial, number) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (username, name_f, name_i, name_o, born_date, born_place, male,
                 given_date, given_code, given, serial, number)
            )

    @classmethod
    def remove_passport(cls, request: tuple):
        username, serial, number = request
        with cls.connection:
            cls.connection.cursor().execute(
                "DELETE FROM passports WHERE serial = ? AND number = ?",
                (serial, number)
            )

    @classmethod
    def update_passport(cls, request: tuple):
        username, name_f, name_i, name_o, born_date, born_place, \
        male, given_date, given_code, given, serial, number = request
        with cls.connection:
            cls.connection.cursor().execute(
                "UPDATE passports SET name_f = ?, name_i = ?, name_o = ?, born_date = ?, born_place = ?, "
                "male = ?, given_date = ?, given_code = ?, given = ? WHERE serial = ? AND number = ?",
                (name_f, name_i, name_o, born_date, born_place, male, given_date, given_code, given, serial, number)
            )

    @classmethod
    def load_passport(cls, request: tuple) -> tuple:
        if request:
            username, name_f, name_i, name_o = request
            with cls.connection:
                return cls.connection.cursor().execute(
                    "SELECT * FROM passports WHERE username = ? AND name_f = ? AND name_i = ? AND name_o = ?",
                    (username, name_f, name_i, name_o)
                ).fetchone()

    @classmethod
    def load_for_db(cls, request: tuple) -> list:
        username = request[0]
        with cls.connection:
            return cls.connection.cursor().execute(
                "SELECT name_f, name_i, name_o, born_date, born_place, serial, "
                "number FROM passports WHERE username = ?", (username,)
            ).fetchall()

    @classmethod
    def load_serials(cls, request: tuple) -> str:
        username = request[0]
        with cls.connection:
            serial_and_number = cls.connection.cursor().execute(
                "SELECT serial, number FROM passports WHERE username = ?", (username,)
            ).fetchone()
            if serial_and_number:
                return f'{serial_and_number[0]} {serial_and_number[1]}'

    @classmethod
    def add_user(cls, request: tuple):
        username, password, reg_date = request
        password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        with cls.connection:
            cls.connection.cursor().execute(
                "INSERT INTO users (username, password, reg_date) VALUES (?, ?, ?)", (username, password, reg_date)
            )

    @classmethod
    def get_user(cls, request: tuple) -> tuple:
        username = request[0]
        with cls.connection:
            return cls.connection.cursor().execute(
                "SELECT * FROM users WHERE username == ?", (username,)
            ).fetchone()

    @classmethod
    def is_user_exist(cls, request: tuple) -> str:
        username, password = request
        password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        with cls.connection:
            resp = cls.connection.cursor().execute(
                "SELECT username, password FROM users WHERE username == ? AND password == ?", (username, password)
            ).fetchone()
            if resp:
                cls.console(f'{resp[0]} connected')
            return '1' if resp else '0'


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    config = ConfigParser()
    config.read('config.ini')
    ip = config.get('SERVER', 'ip')
    port = config.getint('SERVER', 'port')

    server.bind((ip, port))
    server.listen()

    Database.console('start server...')

    while True:
        client, address = server.accept()
        handle = client.recv(4096).decode('utf-8')

        if handle:
            data = json.loads(handle)
            data_params = tuple(data['params'].split())

            if data_params:
                response = getattr(Database, data['func'])(data_params)
            else:
                response = getattr(Database, data['func'])()

            client.send(str(response).encode('utf-8'))
