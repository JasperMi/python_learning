from chapter_09.privileges import Privileges
from chapter_09.user import User


class Admin(User):
    def __init__(self, first_name, last_name, gender):
        super().__init__(first_name, last_name, gender)
        self.privileges = Privileges()

    def show_privileges(self):
        print("Here are all the privileges:")
        for privilege in self.privileges:
            print(privilege)


admin = Admin('Jack', 'Frank', 'male')
admin.privileges.show_privileges()
