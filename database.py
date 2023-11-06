import json
import socket
from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')


class Database:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        self.ip = config.get('SERVER', 'ip')
        self.port = config.getint('SERVER', 'port')

    def __connection(self, func: str, *args):
        """Connect to database server"""

        params = ['None' if arg == '' else arg for arg in args]

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            try:
                params_str = ' '.join(params)
                msg = {'func': func, 'params': params_str}
                msg = json.dumps(msg)

                client.connect((self.ip, self.port))

                client.send(msg.encode('utf-8'))
                response = client.recv(4096).decode('utf-8')
                return response
            except ConnectionRefusedError:
                return False
            except socket.gaierror:
                self.get_local_ip()

    def get_local_ip(self):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
                client.connect((self.ip, self.port))
        except socket.gaierror:
            self.ip = socket.gethostbyname(socket.gethostname())

    def add_passport(self, username: str, name_f: str, name_i: str, name_o: str, born_date: str, born_place: str,
                     male: str, given_date: str, given_code: str, given: str, serial: str, number: str):

        self.__connection(
            'add_passport', username, name_f, name_i, name_o, born_date, born_place, male, given_date,
            given_code, given, serial, number
        )

    def remove_passport(self, username: str, serial: str, number: str):
        self.__connection('remove_passport', username, serial, number)

    def update_passport(self, username: str, name_f: str, name_i: str, name_o: str, born_date: str, born_place: str,
                        male: str, given_date: str, given_code: str, given: str, serial: str, number: str):

        self.__connection(
            'update_passport', username, name_f, name_i, name_o, born_date, born_place, male, given_date,
            given_code, given, serial, number
        )

    def load_passport(self, username: str, name_f: str, name_i: str, name_o: str) -> str or False:
        return self.__connection('load_passport', username, name_f, name_i, name_o)

    def load_for_db(self, username: str) -> str or False:
        return self.__connection('load_for_db', username)

    def load_serials(self, username: str) -> str or False:
        return self.__connection('load_serials', username)

    def add_user(self, username: str, password: str, date: str):
        self.__connection('add_user', username, password, date)

    def get_user(self, username: str) -> str or False or None:
        res = self.__connection('get_user', username)
        return None if res == 'None' else res

    def user_connected(self, username: str) -> str or False:
        self.__connection('user_connected', username)