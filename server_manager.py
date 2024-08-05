import os
os.system('pip install -r requirements.txt')

from main.server import Server


class ServerManager:
    def __init__(self) -> None:
        self.server = Server()


server_manager = ServerManager()
