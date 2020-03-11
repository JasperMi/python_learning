import json

filename = 'numbers.json'
with open(filename) as f_obj:
    # json.load()加载信息
    numbers = json.load(f_obj)
print(numbers)
