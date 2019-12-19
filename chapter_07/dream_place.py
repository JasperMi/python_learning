dream_places = {}
respond_active = True

while respond_active:
    name = input("What is your name? ")
    dream_place = input("If you could visit one place in the world, where would you go? ")
    dream_places[name] = dream_place
    repeat = input("\nAnybody else?(Y/N) ")

    if repeat == 'N':
        respond_active = False

print("-- survey result --")
for name, dream_place in dream_places.items():
    print("name: " + name + "\tdream_place: " + dream_place)
