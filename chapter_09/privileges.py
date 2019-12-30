class Privileges():
    def __init__(self, privileges=['can add post', 'can delete post', 'can ban user']):
        self.privileges = privileges

    def show_privileges(self):
        print("Here are all the privileges:")
        for privilege in self.privileges:
            print(privilege)
