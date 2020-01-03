file_name = "learning_python.txt"
with open(file_name) as file_object:
    contents = file_object.read()
print(contents)

with open(file_name) as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.rstrip())
