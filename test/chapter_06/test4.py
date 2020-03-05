favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}
# 遍历字典中的所有值
for language in favorite_languages.values():
    print(language)
# 遍历字典中的所有值，使用set()找出惟一的元素
for language in set(favorite_languages.values()):
    print(language)
