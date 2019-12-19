number = input("Please input a number: ")
number = int(number)

if number % 10 == 0:
    print("The number " + str(number) + " is 10 times.")
else:
    print("The number " + str(number) + " isn't 10 times.")
