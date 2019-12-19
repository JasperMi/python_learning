def show_magicians(magicians):
    for magician in magicians:
        print(magician[:4] + magician[4:].title())


def make_great(magicians):
    great_magicians = []
    while magicians:
        great_magician = "the Great " + magicians.pop()
        great_magicians.append(great_magician)
    return great_magicians


magicians = ['john', 'jack', 'lucy']
great_magicians = make_great(magicians)
show_magicians(great_magicians)
