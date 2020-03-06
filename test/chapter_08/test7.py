# toppings是一个空元组
def make_pizza(size, *toppings):
    print("\nMaking a " + str(size) +
          "-inch pizza with the following toppings:")
    for topping in toppings:
        print("-" + topping)


# 结合使用位置实参和任意数量实参，必须在函数定义中将接纳任意数量实参的形参放在最后
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
