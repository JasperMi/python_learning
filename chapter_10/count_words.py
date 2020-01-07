def count_words(file_name):
    with open(file_name) as file_object:
        contents = file_object.read()
        count = contents.count('the')
        print("'the' is found " + str(count) + " times.")


file_names = ['alice.txt', 'men.txt']
for file_name in file_names:
    count_words(file_name)
