import json


def get_stored_username():
    """如果存储了用户名，就获取它"""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """提示用户输入用户名"""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username


def judge_username(username):
    """判断用户名是否是正确的"""
    while True:
        flag = input("Is this your username, " + username + "?(Enter Y/N) ")
        if flag == 'Y':
            return True
            break
        elif flag == 'N':
            return False
            break
        else:
            print("Please input 'Y/N'.")


def greet_user():
    """问候用户，并指出其名字"""
    username = get_stored_username()
    if username:
        flag = judge_username(username)
        if flag:
            print("Welcome back, " + username + "!")
        else:
            username = get_new_username()
            print("We'll remember you when you come back, " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")


greet_user()
