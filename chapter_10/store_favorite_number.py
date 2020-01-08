import json

favorite_number = input("Please input your favorite number: ")
file_name = 'favorite_number.json'
with open(file_name, 'w') as file_object:
    json.dump(favorite_number, file_object)
