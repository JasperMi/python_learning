file_name = 'guest_book.txt'
while True:
    guest_name = input("Please input your name: ")
    print("Hello " + guest_name + "!")
    with open(file_name, 'a') as file_object:
        file_object.write(guest_name + "\n")
