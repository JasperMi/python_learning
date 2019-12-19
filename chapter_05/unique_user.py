current_users = ['bob', 'jack', 'admin', 'tom', 'jerry']
new_users = ['jack', 'martin', 'admin', 'katy', 'harry']
lower_current_users = []

for current_user in current_users:
    lower_current_users.append(current_user.lower())
# print(lower_current_users)

for new_user in new_users:
    if new_user.lower() in lower_current_users:
        print("Please input other username, this username: " + new_user + " has been used.")
    else:
        print("This username is not been used.")
