class User():
    """用户类"""

    def __init__(self, first_name, last_name, gender, login_attempts=0):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.login_attempts = login_attempts

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

    def describe_user(self):
        print("first_name:" + self.first_name.title())
        print("last_name:" + self.last_name.title())
        print("sex:" + self.gender)

    def greet_user(self):
        print("Hello " + self.first_name.title() + "!")


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
