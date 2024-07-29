from hashlib import sha256
import json
from factories import UserFactory

class Signup:
    def signup(self, username, password: str, password_conf, number):
        if self.check_password(password, password_conf):
            hashed_password = sha256(password.encode('UTF-8')).hexdigest()
            query = f"INSERT INTO users (username, password, phone_number, borrowed_books, permission, creation_date) VALUES (%s, %s, %s,{json.dumps([])},2, CURRENT_DATE)"
            return query, (username, hashed_password, number)

    @staticmethod
    def check_password(password, password_conf):
        return password == password_conf

class Login:
    def login(self, username, password):
        user = UserFactory()
