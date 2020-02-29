cars = ['bmw', 'audi', 'toyota', 'subaru']
# 按照字母顺序进行排序，临时排序
print(sorted(cars))
print(cars)
# 按照字母逆序进行排序，临时排序
print(sorted(cars, reverse=True))
print(cars)
# 将列表中各元素顺序反转，永久性反转
cars.reverse()
print(cars)
# 计算列表长度
print(len(cars))
