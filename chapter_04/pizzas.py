pizzas = ['seafood pizza', 'cheese pizza', 'beef pizza']
# 创建副本
friends_pizzas = pizzas[:]

pizzas.append('chicken pizza')
friends_pizzas.append('corn pizza')

# for pizza in pizzas:
#     print("I like " + pizza)

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("\nMy friends favorite pizzas are:")
for pizza in friends_pizzas:
    print(pizza)
# print("I really love pizza!")
