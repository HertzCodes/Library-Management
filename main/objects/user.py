from hashlib import sha256


class User:
    def __init__(
        self,
        username: str,
        password: str,
        password_confirmation,
        number: str,
        date,
        permission=3,
    ) -> None:
        self.username = username
        self.set_password(password, password_confirmation)
        self.number = number
        self.permission = permission
        self.date_created = date

    def set_password(self, password, password_confirmation):
        if password == password_confirmation:
            self.password = sha256(password.encode("utf-8")).hexdigest()
            return True
        return False


class Admin(User):
    def __init__(
        self,
        username: str,
        password: str,
        password_confirmation,
        number: str,
        date,
        permission=1,
    ) -> None:
        super().__init__(
            username, password, password_confirmation, number, date, permission
        )


class Owner(Admin):
    def __init__(
        self, username: str, password: str, password_confirmation, date, number: str
    ) -> None:
        super().__init__(
            username, password, password_confirmation, number, date, permission=0
        )


class Librarian(Admin):
    def __init__(
        self,
        username: str,
        password: str,
        password_confirmation,
        date,
        number: str,
        permission,
    ) -> None:
        super().__init__(
            username, password, password_confirmation, number, date, permission
        )


class Client(User):
    def __init__(
        self,
        username: str,
        password: str,
        password_confirmation,
        date,
        number: str,
        permission=3,
    ) -> None:
        super().__init__(
            username, password, password_confirmation, number, date, permission
        )
