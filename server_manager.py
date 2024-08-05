from main.server import Server


class ServerManager:
    def __init__(self) -> None:
        self.server = Server()


server_manager = ServerManager()
