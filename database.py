import json
import socket
from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')
ip = config.get('SERVER', 'ip')
port = config.getint('SERVER', 'port')


class Database:

    @classmethod
    def __connection(cls, func: str, *args):
        """Connect to database server"""

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            try:
                params_str = ' '.join(args)
                msg = {'func': func, 'params': params_str}
                msg = json.dumps(msg)

                client.connect((ip, port))
                client.send(msg.encode('utf-8'))
                response = client.recv(4096).decode('utf-8')
                return response
            except ConnectionRefusedError:
                return False

    @classmethod
    def add_passport(cls, username: str, name_f: str, name_i: str, name_o: str, born_date: str, born_place: str,
                     male: str, given_date: str, given_code: str, given: str, serial: str, number: str):

        cls.__connection('add_passport',
                         username, name_f, name_i, name_o, born_date, born_place,
                         male, given_date, given_code, given, serial, number
                         )

    @classmethod
    def remove_passport(cls, username: str, serial: str, number: str):
        cls.__connection('remove_passport', username, serial, number)

    @classmethod
    def update_passport(cls, username: str, name_f: str, name_i: str, name_o: str, born_date: str, born_place: str,
                        male: str, given_date: str, given_code: str, given: str, serial: str, number: str):

        cls.__connection('update_passport',
                         username, name_f, name_i, name_o, born_date, born_place,
                         male, given_date, given_code, given, serial, number
                         )

    @classmethod
    def load_passport(cls, username: str, name_f: str, name_i: str, name_o: str) -> str or False:
        return cls.__connection('load_passport', username, name_f, name_i, name_o)

    @classmethod
    def load_for_db(cls, username: str) -> str or False:
        return cls.__connection('load_for_db', username)

    @classmethod
    def load_serials(cls, username: str) -> str or False:
        return cls.__connection('load_serials', username)

    @classmethod
    def add_user(cls, username: str, password: str, date: str):
        cls.__connection('add_user', username, password, date)

    @classmethod
    def get_user(cls, username: str) -> str or False:
        return cls.__connection('get_user', username)

    @classmethod
    def is_user_exist(cls, username: str, password: str) -> str or False:
        return cls.__connection('is_user_exist', username, password)




