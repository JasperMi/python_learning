from chapter_09.privileges import Privileges
from chapter_09.user import User


class Admin2(User):
    def __init__(self, first_name, last_name, gender):
        super().__init__(first_name, last_name, gender)
        self.privileges = Privileges()


admin = Admin2('Jack', 'Frank', 'male')
admin.privileges.show_privileges()
