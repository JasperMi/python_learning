prompt = "\nPlease input your pizza toppings:"
prompt += "\nEnter 'quit' to end the program. "
active = True

while active:
    pizza_topping = input(prompt)

    if pizza_topping == 'quit':
        active = False
    else:
        print("We'll add " + pizza_topping + ".")
