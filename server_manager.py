from main.server import Server


class ServerManager:
    def __init__(self) -> None:
        self.__server = Server


if __name__ == '__main__':
    server_manager = ServerManager()
