guests = ['A', 'B', 'C']
print("Welcome, " + guests[0] + "!")
print("Welcome, " + guests[1] + "!")
print("Welcome, " + guests[-1] + "!")
print(guests[1])
guests[1] = 'D'
print("Welcome, " + guests[0] + "!")
print("Welcome, " + guests[1] + "!")
print("Welcome, " + guests[-1] + "!")
print("big table")
guests.insert(0, 'E')
guests.insert(3, "F")
guests.append("G")
print(len(guests))
print("Welcome, " + guests[0] + "!")
print("Welcome, " + guests[1] + "!")
print("Welcome, " + guests[2] + "!")
print("Welcome, " + guests[3] + "!")
print("Welcome, " + guests[4] + "!")
print("Welcome, " + guests[-1] + "!")
print("only 2 guests")
popped_guest1 = guests.pop()
print("Sorry, " + popped_guest1)
popped_guest2 = guests.pop()
print("Sorry, " + popped_guest2)
popped_guest3 = guests.pop()
print("Sorry, " + popped_guest3)
popped_guest4 = guests.pop()
print("Sorry, " + popped_guest4)
print("Welcome, " + guests[0])
print("Welcome, " + guests[1])
del guests[0]
del guests[0]
print(guests)