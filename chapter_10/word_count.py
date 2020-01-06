def count_words(filename):
    """计算一个文件大致包含多少个单词"""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        # msg = "Sorry, the file " + filename + " does not exits."
        # print(msg)
        pass
    else:
        # 计算文件大概包含多少个单词
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")


# filename = 'alice.txt'
# count_words(filename)

filenames = ['alice.txt', 'python.txt', 'programming.txt', 'pi_million_digits.txt']
for filename in filenames:
    count_words(filename)
