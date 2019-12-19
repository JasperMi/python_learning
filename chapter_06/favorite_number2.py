favorite_numbers = {
    'bob': [2, 8],
    'sarah': [1, 6],
    'martin': [1, 6, 8],
    'katy': [1, 5, 6, 8, 9],
    'tom': [10],
}

for name, favorite_number in favorite_numbers.items():
    print("\nname: " + name)
    for number in favorite_number:
        print("number:" + str(number))
