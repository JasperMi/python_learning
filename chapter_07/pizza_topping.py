prompt = "\nPlease input your pizza toppings:"
prompt += "\nEnter 'quit' to end the program. "
pizza_topping = ""

while pizza_topping != 'quit':
    pizza_topping = input(prompt)

    if pizza_topping != 'quit':
        print("We'll add " + pizza_topping + ".")
