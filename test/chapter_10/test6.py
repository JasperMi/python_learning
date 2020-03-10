# 打开文件时，可指定读取模式（'r'）、写入模式（'w'）、附加模式（'a'）或让你能够读取和写入文件的模式（'r+'），默认只读模式
# Python只能将字符串写入文本文件
# 写入空文件
filename = 'programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love programming.")
