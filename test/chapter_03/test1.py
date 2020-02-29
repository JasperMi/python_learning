motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
# 在列表末尾添加元素
motorcycles.append('ducati')
print(motorcycles)
# 在列表中指定索引处插入元素，其后面的元素将各自向后移动一个位置
motorcycles.insert(0, 'motorcycle')
print(motorcycles)
# 删除列表中指定索引处的元素，删除后，该元素就无法访问了
del motorcycles[0]
print(motorcycles)
# 删除列表中最后一个元素，删除后，该元素能够继续使用
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
# 删除列表中指定索引处的元素，删除后，该元素能够继续使用
popped_motorcycle = motorcycles.pop(2)
print(motorcycles)
print(popped_motorcycle)
# 删除列表中指定值的元素，删除后，该元素能够继续使用，只删除第一个指定元素
too_expensive_motorcycle = 'yamaha'
motorcycles.remove(too_expensive_motorcycle)
print(motorcycles)
print(too_expensive_motorcycle)
