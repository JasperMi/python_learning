class User():
    """用户类"""

    def __init__(self, first_name, last_name, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.login_attempts = 0

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


user = User('Jack', 'Bob', 'male')
user2 = User('Lucy', 'Katy', 'female')

user.describe_user()
user.greet_user()
user2.describe_user()
user2.greet_user()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print("login_attempts:" + str(user.login_attempts))
user.reset_login_attempts()
print("login_attempts:" + str(user.login_attempts))
