import sys
import datetime
sys.path.append('database')
from database import Database

class Server:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self) -> None:
        self.__db = Database()
        self._date = datetime.date.today()
    
    
    def grant_permission(user):
        return True if user['permission'] >= 2 else False

server = Server()