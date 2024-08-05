from hashlib import sha256
import json
from server_manager import server_manager


# class Signup:
#     def signup(self, username, password: str, password_conf, number):
#         if self.check_password(password, password_conf):
#             hashed_password = sha256(password.encode('UTF-8')).hexdigest()
#             query = f"INSERT INTO users (username, password, phone_number, borrowed_books, permission, creation_date) VALUES (%s, %s, %s,{json.dumps([])},2, CURRENT_DATE)"
#             return query, (username, hashed_password, number)
#
#     @staticmethod
#     def check_password(password, password_conf):
#         return password == password_conf

class Login:
    def __init__(self):
        self.__server_access = server_manager.server

    def login(self, username, password):
        query = "SELECT * FROM users WHERE username = %s"
        values = (username,)
        user_info = self.__server_access.get_query(query, values)
        if user_info[0][2] == sha256(password.encode('UTF-8')).hexdigest():
            return self.__server_access.factory.create_user(*user_info[0])
        return False