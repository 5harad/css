"""
Solution for Exercise 2 of the python crash course

@author: Jongbin Jung
"""

# 1. 
names = ['Harry', 'Ron', 'Hermione']
verbs = ['likes', 'hates', 'eats']
objects = ['pie', 'owls', 'the snitch']

combos = [(name, verb, obj) 
    for name in names for verb in verbs for obj in objects]


# 2.
for combo in combos:
    name, verb, obj = combo
    if name == 'Harry' and verb == 'eats':
        print ' '.join(combo) + '.'

# 3. 
words = {}
with open('two_cities.txt', 'r') as text:
    for line in text:
        for word in line.lower().split():
            try:
                words[word] += 1
            except KeyError:
                words[word] = 1
                

# 4.
min, max = 500, 700
for k,v in words.iteritems():
    if v >= min and v <= max:
        print k, ':', v