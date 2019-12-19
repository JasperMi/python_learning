sandwich_orders = ['pastrami', 'chicken sandwich', 'extra cheese sandwich', 'pastrami', 'pastrami', 'tuna sandwich']
finished_sanwiches = []

print("Pastrami has been sold out.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("I made your " + sandwich + ".")
    finished_sanwiches.append(sandwich)

print("\nAll sandwiches have been finished:")
for finished_sandwich in finished_sanwiches:
    print("\t" + finished_sandwich)
