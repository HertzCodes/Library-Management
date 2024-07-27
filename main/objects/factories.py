from abc import ABC , abstractmethod
from user import Owner , Librarian , Client

class UserFactory(ABC):
    @abstractmethod
    def create_user():
        pass

class OwnerFactory(UserFactory):
    def create_user():
        return Owner(username , password , password_confirmation , number)

class LibrarianFactory(UserFactory):
    def create_user():
        return Librarian(username , password , password_confirmation , number)

class ClientFactory(UserFactory):
    def create_user():
        return Client(username , password , password_confirmation , number)