filename = 'alice.txt'
try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    print("Sorry, the file " + filename + "does not exist.")
else:
    # split()以空格为分隔符将字符串分拆成多个部分，并将这些部分都存储到一个列表中
    words = contents.split()
    num_words = len(words)
    print("The file " + filename + " has about " + str(num_words) + " words.")
