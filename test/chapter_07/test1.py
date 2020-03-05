sandwich_orders = ['cheese sandwich', 'fish sandwich', 'pastrami', 'pastrami', 'banana sandwich', 'apple sandwich',
                   'pastrami']
finished_sandwiches = []
print("Pastrami has been sold out.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
while sandwich_orders:
    current_sandwich_order = sandwich_orders.pop()
    print("I made your " + current_sandwich_order + ".")
    finished_sandwiches.append(current_sandwich_order)
print("Here are all the finished sandwiches:")
for finished_sandwich in finished_sandwiches:
    print("\t" + finished_sandwich)
