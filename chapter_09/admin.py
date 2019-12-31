from chapter_09.user import User


class Admin(User):
    def __init__(self, first_name, last_name, gender, privileges=['can add post', 'can delete post', 'can ban user']):
        super().__init__(first_name, last_name, gender)
        self.privileges = privileges

    def show_privileges(self):
        print("Here are all the privileges:")
        for privilege in self.privileges:
            print(privilege)


admin = Admin('Jack', 'Frank', 'male')
admin.show_privileges()
