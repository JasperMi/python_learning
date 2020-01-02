from random import randint


class Die():
    def __init__(self, slides=6):
        self.slides = slides

    def roll_die(self):
        random_number = randint(1, self.slides)
        print(random_number)


six = Die()
print("six:")
x = 0
while x < 10:
    six.roll_die()
    x += 1

ten = Die(10)
print("ten:")
x = 0
while x < 10:
    ten.roll_die()
    x += 1

twenty = Die(20)
print("twenty:")
x = 0
while x < 10:
    twenty.roll_die()
    x += 1
