vocabulary = {
    'if': 'if',
    'elif': 'elif',
    'else': 'else',
    'True': 'True',
    'False': 'False'
}

for keyword, meaning in vocabulary.items():
    print(keyword + " : " + meaning)

vocabulary['for'] = 'for'
vocabulary['while'] = 'while'
vocabulary['in'] = 'in'

for keyword, meaning in vocabulary.items():
    print(keyword + " : " + meaning)
