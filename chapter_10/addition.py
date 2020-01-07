print("Give me two numbers, I'll add them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("Please input first number: ")
    if first_number == 'q':
        break
    second_number = input("Please input second number:")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) + int(second_number)
    except ValueError:
        print("Please input number!")
    else:
        print(answer)
