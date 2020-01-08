import json


def get_stored_favorite_number(file_name):
    """获取存储的喜欢的数字"""
    try:
        with open(file_name) as file_object:
            favorite_number = json.load(file_object)
    except FileNotFoundError:
        return None
    else:
        return favorite_number


def input_favorite_number(file_name):
    """提示用户输入喜欢的数字"""
    favorite_number = input("Please input your favorite number: ")
    with open(file_name, 'w') as file_object:
        json.dump(favorite_number, file_object)


def remember_favorite_number():
    """记住喜欢的数字"""
    file_name = 'favorite_number.json'
    favorite_number = get_stored_favorite_number(file_name)
    if favorite_number:
        print("I know your favorite number. It's " + favorite_number + ".")
    else:
        print("I'll remember your favorite number next time.")


remember_favorite_number()
