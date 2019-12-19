def order_sandwich(*sandwiches):
    print("\nAdd to your sandwich:")
    for sandwich in sandwiches:
        print("- " + sandwich)


order_sandwich('egg')
order_sandwich('cheese', 'egg')
order_sandwich('cheese', 'jam', 'egg')
