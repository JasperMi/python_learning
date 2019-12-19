prompt = "\nHow old are you? "
active = True

while active:
    message = input(prompt)
    message = int(message)

    if message < 3:
        cost = 0
    elif message <= 12:
        cost = 10
    else:
        cost = 15

    print("The ticket is $" + str(cost) + ".")
