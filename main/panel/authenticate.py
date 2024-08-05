from hashlib import sha256
from server_manager import server_manager


class Login:
    def __init__(self):
        self.__server_access = server_manager.server

    def login(self, username, password):
        query = "SELECT * FROM users WHERE username = %s"
        values = (username,)
        user_info = self.__server_access.get_query(query, values)
        try:
            if user_info[0][2] == sha256(password.encode('UTF-8')).hexdigest():
                return self.__server_access.factory.create_user(*user_info[0])
            return "Invalid Credentials"
        except IndexError:
            return "Username Not Found"
