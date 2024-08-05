from hashlib import sha256
from server_manager import server_manager
import json


class AdminPanel:
    def __init__(self, admin):
        self.__server_access = server_manager.server
        self.__admin = admin

    def add_user(self, username, password: str, password_conf, number):
        if (username,) not in self.__get_all_usernames():
            if self.__check_password(password, password_conf):
                hashed_password = sha256(password.encode('UTF-8')).hexdigest()
                query = f"INSERT INTO users (username, password, phone_number, borrowed_books, permission, creation_date) VALUES (%s, %s, %s,%s,2, CURRENT_DATE)"
                self.__server_access.send_query(self.__admin, query, (username, hashed_password, number, json.dumps([])))
        else:
            return "Username already taken!"

    @staticmethod
    def __check_password(password, password_conf):
        return password == password_conf

    def __get_all_usernames(self):
        query = 'SELECT username FROM users'
        return self.__server_access.get_query(query)
