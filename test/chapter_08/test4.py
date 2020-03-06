def build_person(first_name, last_name):
    person = {'first_name': first_name, 'last_name': last_name}
    return person


musician = build_person('jimi', 'hendrix')
print(musician)
