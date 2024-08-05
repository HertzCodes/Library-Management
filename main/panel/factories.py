from main.objects.user import Owner, Librarian, Student


class UserFactory:
    def create_user(self, student_id, username, password, number, date, borrowed_books, permission):
        print(permission)
        if permission == 0:
            return OwnerFactory().create_user(student_id, username, password, number, date, borrowed_books, permission)

        elif permission == 1:
            return LibrarianFactory().create_user(student_id, username, password, number, date, borrowed_books, permission)

        else:
            return StudentFactory().create_user(student_id, username, password, number, date, borrowed_books, permission)


class OwnerFactory(UserFactory):
    @staticmethod
    def create_user(*args):
        return Owner(*args)


class LibrarianFactory(UserFactory):
    @staticmethod
    def create_user(*args):
        return Librarian(*args)


class StudentFactory(UserFactory):
    @staticmethod
    def create_user(*args):
        return Student(*args)
