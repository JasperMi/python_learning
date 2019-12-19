people = []
person_0 = {
    'first_name': 'Jack',
    'last_name': 'Ma',
}
person_1 = {
    'first_name': 'Mary',
    'last_name': 'Sun'
}
person_2 = {
    'first_name': 'Martin',
    'last_name': 'Li'
}

people.append(person_0)
people.append(person_1)
people.append(person_2)

for person in people:
    for first_name, last_name in person.items():
        print(first_name + " " +
              last_name)
