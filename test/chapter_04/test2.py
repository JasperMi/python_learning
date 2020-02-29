# range(1,6)：生成1-5的数字
for value in range(1, 6):
    print(value)
# list()：将其中的值转换为列表
numbers = list(range(1, 6))
print(numbers)
# 生成1-10之间的偶数
even_numbers = list(range(2, 11, 2))
print(even_numbers)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# 获得数字列表中的最大值
print(max(numbers))
# 获得数字列表中的最小值
print(min(numbers))
# 获得数字列表的和
print(sum(numbers))
