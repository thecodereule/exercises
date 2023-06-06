abc = 'With three words'
stuff = abc.split()
print(stuff)

'''['With', 'three', 'words]'''
print(len(stuff))

'''3'''
print(stuff[0])

'''With'''
print(stuff)

'''['With', 'three', 'words]'''
for word in stuff:
    print(word)

'''
With
three
words
'''
# Split breaks a string into parts and produces a list of strings. We think of these as words. We can access a particular word or loop through all the words

