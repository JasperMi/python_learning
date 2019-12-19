pets = []
cat = {
    'breed': 'American Shorthair',
    'host': 'Jasper'
}
dog = {
    'breed': 'Golden Retriever',
    'host': 'Alice'
}

pets.append(cat)
pets.append(dog)

for pet in pets:
    print("breed: " + pet['breed'])
    print("host: " + pet['host'] + "\n")
