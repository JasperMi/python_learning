file_name = "love_programming.txt"
while True:
    reason = input("Please input the reason(input 'exit' to exit): ")
    if reason == 'exit':
        break
    with open(file_name, 'a') as file_object:
        file_object.write(reason + "\n")
