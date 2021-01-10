class NoAdminError(Exception):
    pass


class User(NoAdminError):
    def __init__(self, name, admin):
        self.name = name
        self.admin = admin

    def delete_post(self):
        if self.admin:
            print("Deleted posts")
        else:
            raise NoAdminError("Not allowed!")


user1 = User("John", True)
user2 = User("Jim", False)

user1.delete_post()
user2.delete_post()

