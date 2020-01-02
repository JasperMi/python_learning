from collections import OrderedDict

vocabulary = OrderedDict()
vocabulary['if'] = 'if'
vocabulary['elif'] = 'elif'
vocabulary['else'] = 'else'
vocabulary['True'] = 'True'
vocabulary['False'] = 'False'

for word, meaning in vocabulary.items():
    print(word + "'s meaning is " + meaning)
