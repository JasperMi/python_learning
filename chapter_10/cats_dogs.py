def print_file(file_name):
    try:
        with open(file_name) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        # print("The file " + file_name + " is not found!")
        pass
    else:
        print(contents.rstrip())


file_names = ['cats.txt', 'dogs.txt']
for file_name in file_names:
    print_file(file_name)
