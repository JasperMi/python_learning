sandwich_orders = ['mushrooms sandwich', 'cheese sandwich', 'chicken sandwich']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("I made your " + sandwich + ".")
    finished_sandwiches.append(sandwich)

print("All sandwiches have been finished.")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)
