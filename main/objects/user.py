class User:
    def __init__(
        self,
        student_id,
        username: str,
        password: str,
        number: str,
        date,
        borrowed_books,
        permission,
    ) -> None:
        self.student_id = student_id
        self.username = username
        self.password = password
        self.number = number
        self.permission = permission
        self.date_created = date
        self.borrowed_books = borrowed_books
        self.logged_in = True


class Owner(User):
    def __init__(self, student_id, username, password, number, date, borrowed_books, permission):
        super().__init__(student_id, username, password, number, date, borrowed_books, permission)


class Librarian(User):
    def __init__(self, student_id, username, password, number, date, borrowed_books, permission):
        super().__init__(student_id, username, password, number, date, borrowed_books, permission)


class Student(User):
    def __init__(self, student_id, username, password, number, date, borrowed_books, permission):
        super().__init__(student_id, username, password, number, date, borrowed_books, permission)