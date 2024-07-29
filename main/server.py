import datetime
from database.database import Database




class Server:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self) -> None:
        self.__db = Database()
        self._date = datetime.date.today()

    @staticmethod
    def grant_permission(user):
        return True if user['permission'] >= 1 else False

    def send_query(self, user, query):
        if self.grant_permission(user):
            self.__db.run_query(query)
            return True
        return False

