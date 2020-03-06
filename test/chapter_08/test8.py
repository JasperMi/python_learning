# user_info是一个空字典
def buile_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


# 使用任意数量的关键字实参
user_profile = buile_profile("albert", "einstein",
                             location='princeton',
                             field='physics')
print(user_profile)
