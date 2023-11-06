import hashlib
import socket
import sqlite3
import json
import datetime
import time

from configparser import ConfigParser

import keyboard


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

    @staticmethod
    def __unpack_request(request: tuple) -> tuple:
        return tuple([None if item == 'None' else item for item in request])

    @classmethod
    def add_passport(cls, request: tuple):
        username, name_f, name_i, name_o, born_date, born_place, \
        male, given_date, given_code, given, serial, number = cls.__unpack_request(request)

        with cls.connection:
            cls.connection.cursor().execute(
                "INSERT INTO passports (username, name_f, name_i, name_o, born_date, born_place, male, "
                "given_date, given_code, given, serial, number) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (username, name_f, name_i, name_o, born_date, born_place, male,
                 given_date, given_code, given, serial, number)
            )

    @classmethod
    def remove_passport(cls, request: tuple):
        username, serial, number = cls.__unpack_request(request)
        with cls.connection:
            cls.connection.cursor().execute(
                "DELETE FROM passports WHERE username = ? AND serial = ? AND number = ?",
                (username, serial, number)
            )

    @classmethod
    def update_passport(cls, request: tuple):
        username, name_f, name_i, name_o, born_date, born_place, \
        male, given_date, given_code, given, serial, number = cls.__unpack_request(request)
        with cls.connection:
            cls.connection.cursor().execute(
                "UPDATE passports SET name_f = ?, name_i = ?, name_o = ?, born_date = ?, born_place = ?, "
                "male = ?, given_date = ?, given_code = ?, given = ? WHERE username = ? AND serial = ? AND number = ?",
                (
                    name_f, name_i, name_o, born_date, born_place, male, given_date,
                    given_code, given, username, serial, number
                )
            )

    @classmethod
    def load_passport(cls, request: tuple) -> tuple:
        if request:
            username, name_f, name_i, name_o = cls.__unpack_request(request)
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
        username, password, reg_date = cls.__unpack_request(request)
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
    def user_connected(cls, request: tuple):
        username = request[0]
        cls.console(f'{username} connected')


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    config = ConfigParser()
    config.read('config.ini')
    ip = config.get('SERVER', 'ip')
    port = config.getint('SERVER', 'port')

    try:
        server.bind((ip, port))
    except socket.gaierror:
        ip = socket.gethostbyname(socket.gethostname())
        server.bind((ip, port))

    server.listen()
    server.setblocking(False)
    Database.console(f'start server on {ip}:{port}')

    while True:
        try:
            try:
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

            except BlockingIOError:
                if keyboard.is_pressed('ctrl+c'):
                    quit()
        except KeyboardInterrupt:
            quit()
