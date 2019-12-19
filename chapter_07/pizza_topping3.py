prompt = "\nPlease input your pizza toppings:"
prompt += "\nEnter 'quit' to end the program. "
message = ""

while True:
    pizza_topping = input(prompt)

    if pizza_topping == 'quit':
        break
    else:
        print("We'll add " + pizza_topping + ".")
