from chapter_09.user import User


class Privileges():
    def __init__(self, privileges=['can add post', 'can delete post', 'can ban user']):
        self.privileges = privileges

    def show_privileges(self):
        print("Here are all the privileges:")
        for privilege in self.privileges:
            print(privilege)


class Admin(User):
    def __init__(self, first_name, last_name, gender):
        super().__init__(first_name, last_name, gender)
        self.privileges = Privileges()
