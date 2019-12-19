favorite_places = {
    'Martin': ['Qingdao', 'Shanghai', 'Beijing'],
    'Lucy': ['Qingdao', 'Chengdu'],
    'Mark': ['Xian'],
}

for name, favorite_place in favorite_places.items():
    print("\nname: " + name)
    for place in favorite_place:
        print("places: " + place)
