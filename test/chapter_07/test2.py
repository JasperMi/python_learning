responses = {}
flag = True
while flag:
    name = input("What's your name? ")
    response = input("If you could visit one place in the world, where would you go? ")
    responses[name] = response
    repeat = input("Other people?Input yes/no. ")
    if repeat == 'no':
        flag = False

for name, response in responses.items():
    print("\n" + name + ":" + response)
